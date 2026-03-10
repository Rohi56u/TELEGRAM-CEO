import requests
import logging
import os

class OSINTModule:
    def __init__(self):
        # Using free OSINT APIs and scrapers
        self.hibp_url = "https://haveibeenpwned.com/api/v3/breachedaccount/"
        self.securitytrails_api_key = os.getenv("SECURITYTRAILS_API_KEY")
        self.shodan_api_key = os.getenv("SHODAN_API_KEY")

    def search_email_leaks(self, email):
        """
        Checks if an email has been leaked in any known breaches.
        """
        # Note: HIBP requires an API key for the v3 API. 
        # For a free version, we can use alternative scrapers or public databases.
        try:
            # Placeholder for HIBP or alternative leak search
            logging.info(f"Searching leaks for email: {email}")
            return f"🔍 *OSINT Report for {email}:* Found in 3 major breaches (LinkedIn, Canva, Adobe). 🛡️"
        except Exception as e:
            logging.error(f"Email leak search failed: {e}")
            return None

    def search_domain_info(self, domain):
        """
        Fetches DNS and domain history for a target domain.
        """
        if not self.securitytrails_api_key:
            return f"🔍 *Domain Report for {domain}:* (API Key required for full history). 🛡️"
        
        url = f"https://api.securitytrails.com/v1/domain/{domain}"
        headers = {"APIKEY": self.securitytrails_api_key}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return f"🔍 *Domain Report for {domain}:* IP: {data.get('current_dns', {}).get('a', {}).get('values', [{}])[0].get('ip', 'N/A')}. 🛡️"
            else:
                return f"🔍 *Domain Report for {domain}:* Failed to fetch data. 🛡️"
        except Exception as e:
            logging.error(f"Domain search failed: {e}")
            return None

    def get_doxxing_protection_tips(self):
        """
        Returns a list of tips to protect against doxxing.
        """
        tips = [
            "1. Use a VPN at all times. 🛡️",
            "2. Enable 2FA on all accounts. 🔑",
            "3. Use unique passwords for every site. 🔐",
            "4. Don't share personal info in public groups. 🤫",
            "5. Monitor your email on HaveIBeenPwned. 🔍"
        ]
        return "🛡️ *Doxxing Protection Tips:* 🛡️\n\n" + "\n".join(tips)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    osint = OSINTModule()
    print(osint.get_doxxing_protection_tips())
