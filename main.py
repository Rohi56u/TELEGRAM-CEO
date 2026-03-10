import logging
import os
import sqlite3
import time
import random
from enhanced_scraper import EnhancedForumScraper
from dark_web_scraper import DarkWebScraper
from ai_enhancer import AIEnhancer
from image_generator import ImageGenerator
from video_generator import VideoGenerator
from engagement_bot import EngagementBot
from malware_analyzer import MalwareAnalyzer
from growth_hacker import GrowthHacker
from market_intelligence import MarketIntelligence
from global_reach import GlobalReach
from giveaway_bot import GiveawayBot
from cross_promotion_bot import CrossPromotionBot
from trend_predictor import TrendPredictor
from osint_module import OSINTModule
from ghost_mirror import GhostMirror
from zeroday_scanner import ZeroDayScanner
from hacker_economy import HackerEconomy
from satellite_monitor import SatelliteMonitor
from ai_tools_creator import AIToolsCreator
from growth_engine import GrowthEngine
from autonomous_ghost import AutonomousGhost

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def escape_markdown(text):
    """Escapes special Markdown characters to prevent Telegram parse errors."""
    if not text:
        return ""
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in special_chars:
        text = text.replace(char, f'\\{char}')
    return text

class UltimateCosmicBot:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        self.channel_id = os.getenv("CHANNEL_ID")
        self.backup_channel_id = os.getenv("BACKUP_CHANNEL_ID", "@hackerclob_backup")
        self.db_path = "posted_threads.db"
        
        # --- Omnipotent Core Modules ---
        self.surface_scraper = EnhancedForumScraper()
        self.dark_scraper = DarkWebScraper()
        self.enhancer = AIEnhancer()
        self.image_gen = ImageGenerator()
        self.video_gen = VideoGenerator()
        self.bot = EngagementBot(self.token, self.channel_id)
        self.malware_analyzer = MalwareAnalyzer()
        self.growth_hacker = GrowthHacker(self.channel_id)
        self.market_intel = MarketIntelligence()
        self.global_reach = GlobalReach()
        self.giveaway_bot = GiveawayBot(self.token, self.channel_id)
        self.cross_promo = CrossPromotionBot(self.token, self.channel_id)
        self.trend_predictor = TrendPredictor()
        self.osint = OSINTModule()
        self.ghost_mirror = GhostMirror(self.token, self.channel_id, self.backup_channel_id)
        self.zeroday_scanner = ZeroDayScanner()
        self.economy = HackerEconomy()
        self.satellite_monitor = SatelliteMonitor()
        
        # --- Cosmic-Singularity Advanced Modules ---
        self.tools_creator = AIToolsCreator()
        self.growth_engine = GrowthEngine()
        self.autonomous_ghost = AutonomousGhost()
        
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (link TEXT PRIMARY KEY)''')
        conn.commit()
        conn.close()

    def is_posted(self, link):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM posts WHERE link = ?", (link,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def mark_as_posted(self, link):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (link) VALUES (?)", (link,))
        conn.commit()
        conn.close()

    def run_cycle(self):
        logging.info("Starting Ultimate Cosmic-Singularity Level Bot Cycle...")
        
        # 1. Market Intelligence, Satellite & Honeypot Briefing (Once per day)
        if random.random() < 0.1:
            alerts = self.market_intel.get_crypto_alerts()
            if alerts:
                self.bot.bot.send_message(self.channel_id, escape_markdown(alerts), parse_mode='Markdown')
            
            sat_intel = self.satellite_monitor.get_live_flight_intelligence()
            if sat_intel:
                self.bot.bot.send_message(self.channel_id, escape_markdown(sat_intel), parse_mode='Markdown')
            
            honeypot_report = self.autonomous_ghost.get_honeypot_report()
            self.bot.bot.send_message(self.channel_id, escape_markdown(honeypot_report), parse_mode='Markdown')
        
        # 2. AI Trend Prediction, Leaderboard & Persona Briefing (Once per day)
        if random.random() < 0.05:
            recent_leaks = self.surface_scraper.get_all_latest()[:5]
            prediction = self.trend_predictor.predict_upcoming_leaks(recent_leaks)
            if prediction:
                safe_prediction = escape_markdown(prediction)
                self.bot.bot.send_message(self.channel_id, f"🧠 *AI Intelligence Prediction:* 🧠\n\n{safe_prediction}", parse_mode='Markdown')
            
            leaderboard = self.growth_engine.get_leaderboard()
            self.bot.bot.send_message(self.channel_id, escape_markdown(leaderboard), parse_mode='Markdown')
            
            persona_briefing = self.autonomous_ghost.get_ai_persona_briefing()
            self.bot.bot.send_message(self.channel_id, escape_markdown(persona_briefing), parse_mode='Markdown')
        
        # 3. Leak-Drop Countdown & IoT Alerts (Once per day)
        if random.random() < 0.05:
            countdown = self.growth_engine.generate_leak_drop_countdown("Elite Database Leak (Fresh)")
            self.bot.bot.send_message(self.channel_id, escape_markdown(countdown), parse_mode='Markdown')
            
            iot_alert = self.autonomous_ghost.scan_unsecured_iot()
            if iot_alert:
                self.bot.bot.send_message(self.channel_id, escape_markdown(iot_alert), parse_mode='Markdown')
        
        # 4. Aggregate Content (Surface + Dark Web + Zero-Day)
        threads = self.surface_scraper.get_all_latest()
        threads.extend(self.dark_scraper.get_all_dark_leaks())
        threads.extend(self.zeroday_scanner.scan_github_for_exploits())
        
        new_posts_count = 0
        
        for t in threads:
            if not self.is_posted(t['link']):
                logging.info(f"New content found: {t['title']} from {t['source']}")
                
                # 5. AI Tool Creation (If it's a vulnerability/exploit)
                if t['category'] in ['Exploits', 'Vulnerabilities']:
                    custom_tool = self.tools_creator.generate_custom_tool(t['title'], t['category'])
                    if custom_tool:
                        # ✅ FIX: custom_tool को escape किया — यही line 140 crash करती थी
                        safe_custom_tool = escape_markdown(custom_tool)
                        self.bot.bot.send_message(self.channel_id, f"🛠️ *AI\-Generated Hacking Tool:* 🛠️\n\n{safe_custom_tool}", parse_mode='Markdown')
                
                # 6. AI Enhancement (Groq)
                ai_data = self.enhancer.optimize_content(t['title'], t['source'], t['category'])
                
                # 7. Malware Analysis & Safety Score
                safety_score = self.malware_analyzer.calculate_safety_score(t['source'])
                safety_badge = self.malware_analyzer.get_safety_badge(safety_score)
                
                # 8. Growth Hacking (SEO & Join-to-Unlock)
                hashtags, seo_text = self.growth_hacker.generate_seo_keywords(t['title'], t['category'], t['source'])
                unlock_link = self.growth_hacker.generate_join_to_unlock_link(t['link'])
                
                # 9. Media Generation (Image + Video Preview)
                image_url = self.image_gen.generate_thumbnail(ai_data['optimized_title'], t['category'])
                video_preview_url = self.video_gen.generate_video_preview(ai_data['optimized_title'], t['category'])
                
                # 10. Send Enhanced Post
                if self.bot.send_enhanced_post(
                    ai_data['optimized_title'],
                    ai_data['summary'],
                    t['link'],
                    t['source'],
                    hashtags,
                    image_url,
                    safety_score,
                    safety_badge,
                    seo_text,
                    video_preview_url=video_preview_url,
                    unlock_link=unlock_link
                ):
                    self.mark_as_posted(t['link'])
                    new_posts_count += 1
                    
                    # 11. Ghost Mirroring (Auto-backup)
                    self.ghost_mirror.mirror_post(
                        t['link'], 
                        ai_data['optimized_title'], 
                        photo=image_url, 
                        animation=video_preview_url
                    )
                    
                    time.sleep(10) # Rate limiting
                    
        logging.info(f"Cycle complete. Posted {new_posts_count} new threads.")

def main():
    if not os.getenv("BOT_TOKEN") or not os.getenv("CHANNEL_ID"):
        logging.error("BOT_TOKEN and CHANNEL_ID must be set in environment variables.")
        return

    bot = UltimateCosmicBot()
    bot.run_cycle()

if __name__ == "__main__":
    main()