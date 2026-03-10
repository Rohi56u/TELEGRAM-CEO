import os
import logging
import requests

class AIToolsCreator:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate_custom_tool(self, vulnerability_desc, target_type):
        if not self.api_key:
            logging.error("GROQ_API_KEY not found. Skipping tool generation.")
            return None

        prompt = f"""
        You are an elite cybersecurity researcher. Based on the following vulnerability description, 
        generate a high-quality, educational Python script (exploit PoC) to demonstrate the vulnerability.
        
        Vulnerability: {vulnerability_desc}
        Target Type: {target_type}
        
        The script should be well-commented, use professional libraries (like requests, scapy), 
        and include a disclaimer that it is for educational purposes only.
        
        Format your response as:
        TOOL_NAME: [Name of the tool]
        DESCRIPTION: [Short description of what it does]
        CODE: [The Python code block]
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert in writing cybersecurity tools and exploit PoCs."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 1500
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                return content
            else:
                logging.error(f"Groq API error in tools creator: {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Tool generation failed: {e}")
            return None
