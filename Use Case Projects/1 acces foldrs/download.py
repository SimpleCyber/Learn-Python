import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set the URL of the web page and the target folder
url = 'https://www.seaart.ai/?ad=INGGH1SEARCH&gad_source=1&gclid=CjwKCAjwiaa2BhAiEiwAQBgyHnAH6h86iXdAvr-zJ81NI1TQ13UKGH0htP5CScqMhRKG-180PJ9PgxoC0ywQAvD_BwE'  # Replace this with the actual webpage URL
target_folder = r'R:\oooi'

# Ensure the target folder exists
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Fetch the web page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags
img_tags = soup.find_all('img')

# Filter and download the images
for img_tag in img_tags:
    img_url = urljoin(url, img_tag.get('src'))
    if img_url.endswith('.webp'):
        # Get the image
        img_data = requests.get(img_url, stream=True)
        img_size = int(img_data.headers.get('Content-Length', 0))
        
        # Check if the image size is greater than 120 KB (120 * 1024 bytes)
        if img_size > 120 * 1024:
            img_name = os.path.join(target_folder, os.path.basename(img_url))
            
            # Save the image
            with open(img_name, 'wb') as img_file:
                img_data.raw.decode_content = True
                img_file.write(img_data.content)
            print(f"Downloaded {img_name} ({img_size/1024:.2f} KB)")

print("Download complete!")
