import sqlite3
import logging
import os
import time
import random

class GrowthEngine:
    def __init__(self, db_path="hacker_economy.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT,
                            balance INTEGER DEFAULT 0,
                            referrals INTEGER DEFAULT 0,
                            rank TEXT DEFAULT 'Newbie'
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS share_unlocks (
                            user_id INTEGER,
                            post_id TEXT,
                            share_count INTEGER DEFAULT 0,
                            PRIMARY KEY (user_id, post_id)
                        )''')
        conn.commit()
        conn.close()

    def get_leaderboard(self, limit=10):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT username, balance, referrals FROM users ORDER BY balance DESC LIMIT ?", (limit,))
        leaderboard = cursor.fetchall()
        conn.close()
        
        text = "🏆 *Global Hacker Leaderboard* 🏆\n\n"
        for i, (user, bal, ref) in enumerate(leaderboard, 1):
            text += f"{i}. *{user}* - {bal} Coins | {ref} Refs\n"
        return text

    def generate_leak_drop_countdown(self, leak_name, hours=2):
        text = f"💎 *ULTRA-PREMIUM LEAK DROP* 💎\n\n"
        text += f"📂 *Content:* {leak_name}\n"
        text += f"⏳ *Countdown:* {hours} Hours Remaining!\n\n"
        text += "⚠️ *Only for the first 500 subscribers who stay active!* ⚠️\n"
        text += "🚀 *Stay tuned and keep notifications ON!* 🚀"
        return text

    def get_private_vault_access(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT referrals FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        
        if result and result[0] >= 10:
            return "🔓 *Access Granted!* Welcome to the Secret Private Vault: [Link to Vault]"
        else:
            refs_needed = 10 - (result[0] if result else 0)
            return f"🔒 *Access Denied!* You need {refs_needed} more referrals to unlock the Private Vault. 🚀"
