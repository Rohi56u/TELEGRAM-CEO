import os
import logging
import requests

class AIEnhancer:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile" # High-performance free model on Groq
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def optimize_content(self, title, source, category):
        """
        Uses Groq AI to optimize the title and generate a short, engaging summary.
        """
        if not self.api_key:
            logging.error("GROQ_API_KEY not found. Using fallback.")
            return self._fallback(title, source, category)

        prompt = f"""
        You are a professional content curator for a high-end hacking and cracking Telegram channel.
        Your goal is to make the content look extremely professional, elite, and "click-worthy".

        Original Title: {title}
        Source: {source}
        Category: {category}

        Please provide:
        1. An optimized, catchy, and elite-sounding title (use emojis).
        2. A 2-3 sentence summary that highlights the value of this content.
        3. 3-5 relevant hashtags.

        Format your response as:
        TITLE: [Optimized Title]
        SUMMARY: [Summary]
        HASHTAGS: [Hashtags]
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert in cybersecurity and underground forum content curation."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 300
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=15)
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                
                # Simple parsing of the AI response
                lines = content.split('\n')
                optimized_title = title
                summary = ""
                hashtags = ""

                for line in lines:
                    if line.startswith("TITLE:"):
                        optimized_title = line.replace("TITLE:", "").strip()
                    elif line.startswith("SUMMARY:"):
                        summary = line.replace("SUMMARY:", "").strip()
                    elif line.startswith("HASHTAGS:"):
                        hashtags = line.replace("HASHTAGS:", "").strip()

                return {
                    'optimized_title': optimized_title,
                    'summary': summary,
                    'hashtags': hashtags
                }
            else:
                logging.error(f"Groq API error: {response.status_code} - {response.text}")
                return self._fallback(title, source, category)

        except Exception as e:
            logging.error(f"AI Enhancement failed: {e}")
            return self._fallback(title, source, category)

    def _fallback(self, title, source, category):
        return {
            'optimized_title': f"🔥 {title} 🔥",
            'summary': f"New premium content available from {source} in the {category} category.",
            'hashtags': f"#{source.replace('.', '')} #Hacking #Leaks"
        }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Test with placeholder key
    # os.environ["GROQ_API_KEY"] = "YOUR_KEY"
    # enhancer = AIEnhancer()
    # test_data = enhancer.optimize_content("Free Netflix Premium Accounts 2026", "OneHack", "Accounts")
    # print(test_data)
