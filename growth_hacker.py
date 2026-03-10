import os
import logging
import urllib.parse

class GrowthHacker:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.bot_username = os.getenv("BOT_USERNAME", "hackerclob_bot")

    def generate_join_to_unlock_link(self, original_link):
        """
        Generates a "Join-to-Unlock" link using a bot-mediated URL.
        """
        # Note: This requires a bot that handles the /start command with a parameter
        # Example: https://t.me/hackerclob_bot?start=L3Rlc3QtbGluaw==
        # The bot will check if the user is a member of @hackerclob before showing the link.
        
        # Base64 encode the original link for safety
        import base64
        encoded_link = base64.b64encode(original_link.encode()).decode()
        
        # Construct the bot-mediated link
        unlock_link = f"https://t.me/{self.bot_username}?start={encoded_link}"
        
        logging.info(f"Generated Join-to-Unlock link: {unlock_link}")
        return unlock_link

    def generate_seo_keywords(self, title, category, source):
        """
        Generates a list of trending keywords for Telegram search optimization.
        """
        # Common high-traffic keywords for hacking/cracking
        base_keywords = ["Hacking", "Cracking", "Leaks", "Premium", "Free", "Accounts", "Tools", "Tutorials"]
        
        # Source-specific keywords
        source_keywords = [source.replace('.', ''), f"{source.replace('.', '')}Leaks"]
        
        # Category-specific keywords
        category_keywords = [category, f"Free{category}", f"Premium{category}"]
        
        # Combine and deduplicate
        all_keywords = list(set(base_keywords + source_keywords + category_keywords))
        
        # Format as hashtags for the post
        hashtags = " ".join([f"#{kw}" for kw in all_keywords[:10]])
        
        # Format as hidden keywords for SEO (invisible to users but searchable)
        # Note: Telegram search indexes the entire message text
        seo_text = f"\n\n🔍 *Search Keywords:* {', '.join(all_keywords)}"
        
        return hashtags, seo_text

    def generate_referral_link(self, user_id):
        """
        Generates a unique referral link for a user.
        """
        # Example: https://t.me/hackerclob_bot?start=ref_123456789
        return f"https://t.me/{self.bot_username}?start=ref_{user_id}"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    gh = GrowthHacker("@hackerclob")
    hashtags, seo = gh.generate_seo_keywords("Free Netflix Premium Accounts 2026", "Accounts", "OneHack")
    print(f"Hashtags: {hashtags}")
    print(f"SEO Text: {seo}")
    unlock_link = gh.generate_join_to_unlock_link("https://onehack.us/t/netflix/123")
    print(f"Unlock Link: {unlock_link}")
