import requests
import logging
import os
import time

class ZeroDayScanner:
    def __init__(self):
        self.github_api_url = "https://api.github.com/search/repositories"
        self.github_token = os.getenv("GITHUB_TOKEN")

    def scan_github_for_exploits(self):
        """
        Scans GitHub for new PoC exploits and zero-day vulnerabilities.
        """
        # Search for repositories with 'exploit' or 'poc' in the name/description
        # and created in the last 24 hours.
        query = "exploit OR poc OR zero-day OR cve-2026"
        params = {
            "q": query,
            "sort": "created",
            "order": "desc",
            "per_page": 10
        }
        headers = {}
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"

        try:
            response = requests.get(self.github_api_url, params=params, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])
                results = []
                for i in items:
                    results.append({
                        'title': f"⚡ [ZERO-DAY] {i['name']} ⚡",
                        'link': i['html_url'],
                        'source': "GitHub (Live Exploit)",
                        'category': "Exploits",
                        'summary': i['description'] or "New PoC exploit discovered on GitHub."
                    })
                return results
            else:
                logging.error(f"GitHub API error in zero-day scanner: {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Zero-day scan failed: {e}")
            return []

    def scan_packetstorm(self):
        """
        Placeholder for Packet Storm RSS/Scraper logic.
        """
        # Packet Storm is a great source for new exploits and tools.
        return []

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # scanner = ZeroDayScanner()
    # print(scanner.scan_github_for_exploits())
