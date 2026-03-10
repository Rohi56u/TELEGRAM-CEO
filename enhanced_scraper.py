import requests
from bs4 import BeautifulSoup
import logging
import time
import random

class EnhancedForumScraper:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
        ]
        self.headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    def _get_request(self, url, params=None):
        try:
            # Rotate User-Agent for each request
            self.headers['User-Agent'] = random.choice(self.user_agents)
            response = requests.get(url, headers=self.headers, params=params, timeout=20)
            if response.status_code == 200:
                return response
            else:
                logging.error(f"Failed to fetch {url}: Status {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def fetch_onehack(self):
        url = "https://onehack.us/latest.json"
        response = self._get_request(url)
        if response:
            try:
                data = response.json()
                topics = data.get('topic_list', {}).get('topics', [])
                results = []
                for t in topics[:15]:
                    results.append({
                        'title': t.get('title'),
                        'link': f"https://onehack.us/t/{t.get('slug')}/{t.get('id')}",
                        'source': 'OneHack',
                        'category': 'Tutorials/Accounts'
                    })
                return results
            except Exception as e:
                logging.error(f"Error parsing OneHack JSON: {e}")
        return []

    def fetch_cracked_io(self):
        # Note: Cracked.io often has Cloudflare, might need more advanced handling in production
        url = "https://cracked.io/forumdisplay.php?fid=2" # Example: Premium Leaks
        response = self._get_request(url)
        if response:
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
                threads = soup.select('.thread_title a')
                results = []
                for t in threads[:10]:
                    results.append({
                        'title': t.text.strip(),
                        'link': f"https://cracked.io/{t['href']}",
                        'source': 'Cracked.io',
                        'category': 'Leaks/Tools'
                    })
                return results
            except Exception as e:
                logging.error(f"Error parsing Cracked.io: {e}")
        return []

    def fetch_nulled_to(self):
        url = "https://www.nulled.to/forum/12-cracked-programs/" # Example: Cracked Programs
        response = self._get_request(url)
        if response:
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
                threads = soup.select('.topic_title')
                results = []
                for t in threads[:10]:
                    link_tag = t.find('a')
                    if link_tag:
                        results.append({
                            'title': link_tag.text.strip(),
                            'link': link_tag['href'],
                            'source': 'Nulled.to',
                            'category': 'Cracked Software'
                        })
                return results
            except Exception as e:
                logging.error(f"Error parsing Nulled.to: {e}")
        return []

    def fetch_babiato(self):
        url = "https://babiato.co/whats-new/posts/"
        response = self._get_request(url)
        if response:
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
                threads = soup.select('.structItem-title a')
                results = []
                for t in threads[:10]:
                    if '/threads/' in t['href']:
                        results.append({
                            'title': t.text.strip(),
                            'link': f"https://babiato.co{t['href']}",
                            'source': 'Babiato',
                            'category': 'Nulled Scripts/Themes'
                        })
                return results
            except Exception as e:
                logging.error(f"Error parsing Babiato: {e}")
        return []

    def get_all_latest(self):
        all_content = []
        logging.info("Starting multi-source scraping...")
        
        all_content.extend(self.fetch_onehack())
        time.sleep(random.uniform(1, 3)) # Random delay to avoid detection
        
        all_content.extend(self.fetch_cracked_io())
        time.sleep(random.uniform(1, 3))
        
        all_content.extend(self.fetch_nulled_to())
        time.sleep(random.uniform(1, 3))
        
        all_content.extend(self.fetch_babiato())
        
        logging.info(f"Scraping complete. Found {len(all_content)} total threads.")
        return all_content

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = EnhancedForumScraper()
    data = scraper.get_all_latest()
    for item in data:
        print(f"[{item['source']}] {item['title']} - {item['link']}")
