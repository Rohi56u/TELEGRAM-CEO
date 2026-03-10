import telebot
from telebot import types
import logging
import os
class EngagementBot:
    def __init__(self, token, channel_id):
        self.bot = telebot.TeleBot(token)
        self.channel_id = channel_id

    def escape_markdown(self, text):
        """Escapes special Markdown characters to prevent Telegram parse errors."""
        if not text:
            return ""
        special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for char in special_chars:
            text = text.replace(char, f'\\{char}')
        return text

    def create_engagement_buttons(self, link, unlock_link=None):
        """
        Creates inline buttons for the post to increase engagement.
        """
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        # Button to view the original content (or unlock link)
        if unlock_link:
            view_button = types.InlineKeyboardButton("🔓 Unlock Content", url=unlock_link)
        else:
            view_button = types.InlineKeyboardButton("🚀 View Content", url=link)
        
        # Button to join the channel (if not already a member)
        join_button = types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/hackerclob")
        
        # ✅ FIX: switch_inline_query काम नहीं करता channel में, url use किया
        share_button = types.InlineKeyboardButton("📤 Share with Friends", url=f"https://t.me/share/url?url={link}&text=Check+out+this+awesome+content")
        
        # Feedback button (optional)
        feedback_button = types.InlineKeyboardButton("💬 Feedback", url="https://t.me/hackerclob_feedback")
        markup.add(view_button, join_button)
        markup.add(share_button, feedback_button)
        
        return markup

    def send_enhanced_post(self, title, summary, link, source, hashtags, image_url, safety_score, safety_badge, seo_text, video_preview_url=None, unlock_link=None):
        """
        Sends a visually appealing post with AI-generated content, safety score, and engagement buttons.
        """
        # ✅ FIX: सभी dynamic values को escape किया
        safe_title = self.escape_markdown(title)
        safe_summary = self.escape_markdown(summary)
        safe_source = self.escape_markdown(source)
        safe_safety_badge = self.escape_markdown(safety_badge)
        safe_hashtags = self.escape_markdown(hashtags)
        safe_seo_text = self.escape_markdown(seo_text)

        message = f"🔥 *{safe_title}* 🔥\n\n"
        message += f"📝 *Summary:* {safe_summary}\n\n"
        message += f"📂 *Source:* {safe_source}\n"
        message += f"🛡️ *Safety Score:* {safety_score}/10 \- {safe_safety_badge}\n"
        message += f"🏷️ *Hashtags:* {safe_hashtags}\n\n"
        message += "⚠️ *MUST USE VPN* ⚠️\n\n"
        message += "👇 *Get Access Below* 👇"
        
        # Add hidden SEO text (searchable but less prominent)
        message += f"\n\n_{safe_seo_text}_"
        
        markup = self.create_engagement_buttons(link, unlock_link)
        
        try:
            # If a video preview is available, send it as an animation (GIF-like)
            if video_preview_url:
                self.bot.send_animation(
                    self.channel_id,
                    animation=video_preview_url,
                    caption=message,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            else:
                # Send the post with the generated image as a photo
                self.bot.send_photo(
                    self.channel_id,
                    photo=image_url,
                    caption=message,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            return True
        except Exception as e:
            logging.error(f"Error sending enhanced post: {e}")
            # Fallback to sending as a text message if photo/animation fails
            try:
                self.bot.send_message(
                    self.channel_id,
                    message,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
                return True
            except Exception as e2:
                logging.error(f"Fallback message failed: {e2}")
                return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Test with placeholder data
    # bot = EngagementBot("YOUR_BOT_TOKEN", "@hackerclob")
    # bot.send_enhanced_post("Elite Hacking Course 2026", "Learn advanced hacking techniques from the best.", "https://onehack.us", "OneHack", "#Hacking #Elite", "https://example.com/image.jpg", 8, "🟢 SAFE (Verified)", "Hacking, Cracked, Leaks")