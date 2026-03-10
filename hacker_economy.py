import sqlite3
import logging
import os

class HackerEconomy:
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
        conn.commit()
        conn.close()

    def get_user(self, user_id, username=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        if not user and username:
            cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
            conn.commit()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()
        conn.close()
        return user

    def add_coins(self, user_id, amount):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        conn.commit()
        conn.close()

    def spend_coins(self, user_id, amount):
        user = self.get_user(user_id)
        if user and user[2] >= amount:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET balance = balance - ? WHERE user_id = ?", (amount, user_id))
            conn.commit()
            conn.close()
            return True
        return False

    def add_referral(self, referrer_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET referrals = referrals + 1, balance = balance + 10 WHERE user_id = ?", (referrer_id,))
        conn.commit()
        conn.close()

    def get_rank(self, balance):
        if balance >= 1000: return "God-Mode 🛰️"
        if balance >= 500: return "Elite Hacker 💻"
        if balance >= 100: return "Pro Cracker 🛠️"
        return "Newbie 🛡️"

    def update_rank(self, user_id):
        user = self.get_user(user_id)
        if user:
            new_rank = self.get_rank(user[2])
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET rank = ? WHERE user_id = ?", (new_rank, user_id))
            conn.commit()
            conn.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    economy = HackerEconomy()
    economy.get_user(12345, "test_user")
    economy.add_coins(12345, 50)
    print(economy.get_user(12345))
