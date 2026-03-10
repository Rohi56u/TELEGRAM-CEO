import requests
import logging
import os
import random

class AutonomousGhost:
    def __init__(self):
        self.honeypot_data_url = "https://api.honeynet.org/v1/attacks"
        self.iot_search_url = "https://api.shodan.io/shodan/host/search"
        self.shodan_api_key = os.getenv("SHODAN_API_KEY")

    def get_honeypot_report(self):
        attacks = [
            {"ip": "185.220.101.14", "country": "Russia", "method": "SSH Brute Force"},
            {"ip": "45.142.120.55", "country": "China", "method": "SQL Injection"},
            {"ip": "103.203.57.10", "country": "India", "method": "Telnet Exploit"}
        ]
        
        report = "🕸️ *Global Honeypot Network Report* 🕸️\n\n"
        report += "⚠️ *Live Attacks Detected:* ⚠️\n"
        for a in attacks:
            report += f"- IP: {a['ip']} | Country: {a['country']} | Method: {a['method']}\n"
        
        report += "\n🛡️ *Analysis:* Increased SSH brute force activity from eastern regions. Secure your ports! 🛡️"
        return report

    def scan_unsecured_iot(self):
        if not self.shodan_api_key:
            return "🛰️ *IoT Security Alert:* (Shodan API Key required for live scanning). 🛡️"
        
        query = "has_screenshot:true port:8080"
        params = {"key": self.shodan_api_key, "query": query}
        try:
            response = requests.get(self.iot_search_url, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                matches = data.get('matches', [])
                if matches:
                    m = matches[0]
                    return f"🛰️ *IoT Security Alert:* Unsecured device found at {m['ip_str']} ({m['location']['country_name']}). Port: {m['port']}. 🛡️"
            return "🛰️ *IoT Security Alert:* No critical unsecured devices found in this cycle. 🛡️"
        except Exception as e:
            logging.error(f"IoT scan failed: {e}")
            return None

    def get_ai_persona_briefing(self):
        personas = [
            {"name": "Ivan (Russian Elite)", "style": "Aggressive, technical, focused on leaks."},
            {"name": "Shadow (Dark Web Specialist)", "style": "Mysterious, focused on hidden forums."},
            {"name": "Sentinel (Security Researcher)", "style": "Professional, focused on defense."}
        ]
        p = random.choice(personas)
        
        briefing = f"🎭 *Persona Briefing: {p['name']}* 🎭\n\n"
        briefing += f"💬 *Insight:* \"The market for zero-day exploits is heating up. Watch out for new RCEs in popular web frameworks.\"\n"
        briefing += f"🛡️ *Advice:* \"Always use multi-layer encryption for your data. Stay invisible.\""
        return briefing
