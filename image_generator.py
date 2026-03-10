import logging
import urllib.parse

class ImageGenerator:
    def __init__(self):
        # Pollinations.ai is a free, no-key-required image generation service
        self.base_url = "https://pollinations.ai/p/"

    def generate_thumbnail(self, title, category):
        """
        Generates a relevant thumbnail image for the post using Pollinations.ai.
        """
        prompt = f"Futuristic cybersecurity hacking digital art, {title}, {category}, neon cyberpunk aesthetic, high resolution, 4k, professional thumbnail"
        
        # URL encode the prompt
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Construct the final image URL
        # Pollinations.ai generates the image on-the-fly when the URL is accessed
        image_url = f"{self.base_url}{encoded_prompt}?width=1024&height=1024&seed={hash(title)}&nologo=true"
        
        logging.info(f"Generated free thumbnail URL: {image_url}")
        return image_url

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generator = ImageGenerator()
    test_image_url = generator.generate_thumbnail("Free Netflix Premium Accounts 2026", "Accounts")
    print(f"Generated Image URL: {test_image_url}")
