import os
import logging
import requests

class GlobalReach:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def translate_and_summarize(self, text, target_language="English"):
        """
        Translates and summarizes content from Russian, Chinese, or Spanish.
        Uses Groq AI for high-quality translation and summarization.
        """
        if not self.api_key:
            logging.error("GROQ_API_KEY not found. Skipping translation.")
            return text

        prompt = f"""
        You are a professional translator and cybersecurity expert.
        Translate the following text into {target_language} and provide a concise summary.
        If the text is already in {target_language}, just summarize it.
        Focus on key technical details, leaks, or exploits mentioned.

        Text: {text}

        Format your response as:
        TRANSLATION: [Translated Title/Summary]
        SUMMARY: [Summary]
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert in translating underground forum content."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=15)
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                
                # Simple parsing of the AI response
                lines = content.split('\n')
                translation = text
                summary = ""

                for line in lines:
                    if line.startswith("TRANSLATION:"):
                        translation = line.replace("TRANSLATION:", "").strip()
                    elif line.startswith("SUMMARY:"):
                        summary = line.replace("SUMMARY:", "").strip()

                return {
                    'translation': translation,
                    'summary': summary
                }
            else:
                logging.error(f"Groq API error in translation: {response.status_code}")
                return {'translation': text, 'summary': "Translation failed."}

        except Exception as e:
            logging.error(f"Translation failed: {e}")
            return {'translation': text, 'summary': "Translation failed."}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # gr = GlobalReach()
    # test_data = gr.translate_and_summarize("Привет, это новый слив базы данных.", "English")
    # print(test_data)
