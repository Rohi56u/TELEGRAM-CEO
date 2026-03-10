import os
import logging
import requests
import json
from datetime import datetime, timedelta

class TrendPredictor:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def predict_upcoming_leaks(self, recent_leaks):
        """
        Analyzes recent leaks and forum chatter to predict future breaches.
        """
        if not self.api_key:
            logging.error("GROQ_API_KEY not found. Skipping prediction.")
            return None

        # Prepare the context for the AI
        context = "\n".join([f"- {l['title']} ({l['source']})" for l in recent_leaks[:10]])
        
        prompt = f"""
        You are a high-level Cyber Intelligence Analyst. Based on the following recent leaks and forum activity, 
        predict 3 potential upcoming breaches or trends in the hacking world for the next 7 days.
        
        Recent Activity:
        {context}
        
        For each prediction, provide:
        1. Target/Trend Name
        2. Probability (0-100%)
        3. Reason for prediction (based on patterns)
        4. Estimated Date
        
        Format your response as a professional intelligence briefing.
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert in cyber threat intelligence and predictive analysis."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 800
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=20)
            if response.status_code == 200:
                prediction = response.json()['choices'][0]['message']['content']
                return prediction
            else:
                logging.error(f"Groq API error in trend predictor: {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Trend prediction failed: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # tp = TrendPredictor()
    # test_leaks = [{'title': 'Major Bank Leak', 'source': 'BreachForums'}, {'title': 'New Ransomware Variant', 'source': 'XSS.is'}]
    # print(tp.predict_upcoming_leaks(test_leaks))
