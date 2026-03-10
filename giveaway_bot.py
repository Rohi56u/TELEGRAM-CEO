import telebot
import logging
import random
import time

class GiveawayBot:
    def __init__(self, token, channel_id):
        self.bot = telebot.TeleBot(token)
        self.channel_id = channel_id

    def create_daily_poll(self):
        """
        Creates a daily poll to increase channel engagement.
        """
        question = "🔥 *What should we leak next?* 🔥"
        options = ["Netflix Premium Accounts 🍿", "Elite Hacking Courses 💻", "Major Database Leaks 📂", "Cracked Software Tools 🛠️"]
        
        try:
            self.bot.send_poll(
                self.channel_id,
                question,
                options,
                is_anonymous=False,
                allows_multiple_answers=True
            )
            return True
        except Exception as e:
            logging.error(f"Error sending poll: {e}")
            return False

    def start_giveaway(self, prize_name):
        """
        Starts a daily giveaway in the channel.
        """
        message = f"🎁 *DAILY GIVEAWAY ALERT!* 🎁\n\n"
        message += f"🏆 *Prize:* {prize_name}\n\n"
        message += "👇 *How to Enter:* 👇\n"
        message += "1. Join @hackerclob (if not already)\n"
        message += "2. Click the button below to enter!\n\n"
        message += "⏳ *Winner will be announced in 24 hours!* ⏳"
        
        markup = telebot.types.InlineKeyboardMarkup()
        enter_button = telebot.types.InlineKeyboardButton("🎟️ Enter Giveaway", callback_data="enter_giveaway")
        markup.add(enter_button)
        
        try:
            self.bot.send_message(
                self.channel_id,
                message,
                parse_mode='Markdown',
                reply_markup=markup
            )
            return True
        except Exception as e:
            logging.error(f"Error starting giveaway: {e}")
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # bot = GiveawayBot("YOUR_BOT_TOKEN", "@hackerclob")
    # bot.create_daily_poll()
    # bot.start_giveaway("Netflix Premium Account (1 Month)")
