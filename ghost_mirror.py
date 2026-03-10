import telebot
import logging
import os
import json

class GhostMirror:
    def __init__(self, token, main_channel_id, backup_channel_id):
        self.bot = telebot.TeleBot(token)
        self.main_channel_id = main_channel_id
        self.backup_channel_id = backup_channel_id
        self.mirror_file = "mirror_data.json"

    def mirror_post(self, message_id, text, photo=None, animation=None, markup=None):
        """
        Clones a post from the main channel to the backup channel.
        """
        try:
            if photo:
                self.bot.send_photo(
                    self.backup_channel_id,
                    photo=photo,
                    caption=text,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            elif animation:
                self.bot.send_animation(
                    self.backup_channel_id,
                    animation=animation,
                    caption=text,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            else:
                self.bot.send_message(
                    self.backup_channel_id,
                    text,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            logging.info(f"Post {message_id} mirrored to backup channel.")
            return True
        except Exception as e:
            logging.error(f"Mirroring failed for post {message_id}: {e}")
            return False

    def generate_onion_mirror(self, posts):
        """
        Generates a static HTML file for a Tor-hosted (.onion) mirror.
        """
        html_content = "<html><head><title>HackerClob Ghost Mirror</title></head><body>"
        html_content += "<h1>HackerClob Elite Leaks Mirror</h1>"
        for p in posts[:20]:
            html_content += f"<div><h3>{p['title']}</h3><p>{p['summary']}</p><a href='{p['link']}'>View Content</a></div><hr>"
        html_content += "</body></html>"
        
        with open("onion_mirror.html", "w") as f:
            f.write(html_content)
        
        logging.info("Onion mirror HTML generated.")
        return "onion_mirror.html"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # gm = GhostMirror("YOUR_BOT_TOKEN", "@hackerclob", "@hackerclob_backup")
    # gm.generate_onion_mirror([{'title': 'Test Leak', 'summary': 'Test Summary', 'link': 'https://onehack.us'}])
