import os
import logging
import requests
import telebot

class InteractiveChatbot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def handle_user_query(self, message):
        """
        Handles user queries in the channel comments or direct messages.
        Uses Groq AI to provide helpful, hacker-style responses.
        """
        user_text = message.text
        user_id = message.from_user.id
        
        # System prompt to make the bot sound like an elite hacker admin
        system_prompt = """
        You are the 'HackerClob Elite Admin' bot. You are an expert in hacking, cracking, and cybersecurity.
        Your tone is cool, professional, and helpful. You use emojis like 🚀, 🔥, 🛡️, 💻.
        When users ask for help with tools or leaks, provide concise and accurate advice.
        Always remind them to use a VPN for safety.
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=15)
            if response.status_code == 200:
                ai_reply = response.json()['choices'][0]['message']['content']
                self.bot.reply_to(message, ai_reply)
                return True
            else:
                logging.error(f"Groq API error in chatbot: {response.status_code}")
                self.bot.reply_to(message, "⚠️ System busy, try again later. Stay safe! 🛡️")
                return False
        except Exception as e:
            logging.error(f"Chatbot failed: {e}")
            return False

    def setup_handlers(self):
        """
        Sets up the message handlers for the bot.
        """
        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            # Only respond if the bot is mentioned or it's a direct message
            if message.chat.type == 'private' or (message.reply_to_message and message.reply_to_message.from_user.is_bot):
                self.handle_user_query(message)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # bot = InteractiveChatbot("YOUR_BOT_TOKEN")
    # bot.setup_handlers()
    # bot.bot.polling()
