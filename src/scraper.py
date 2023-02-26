import requests
from bs4 import BeautifulSoup
from utils import column_list as urls
import os
from dotenv import load_dotenv
import re

load_dotenv()

log_file = os.getenv('DEBUG_LOG_FILE')

import logging

logging.basicConfig(filename=log_file, level=logging.DEBUG)

# Define an empty list to store the content structures
content_structures = []

for i in range(1):
    if not urls[i].startswith("http://") and not urls[i].startswith("https://"):
        urls[i] = "https://" + urls[i]

# Loop through the URLs and collect the content structures
for url in urls[:1]:
    try:
        # Send a request to the URL and get the HTML content
        response = requests.get(url)
        html_content = response.content
        
        # Use BeautifulSoup to parse the HTML content and extract the content structure
        soup = BeautifulSoup(html_content, 'html.parser')
        content_structure = soup.get_text()
        
        # Append the content structure to the list
        content_structures.append(content_structure)

    except requests.exceptions.SSLError as e:
        # Handle the SSL error here
        logging.error(f"Skipping {url}: {e}")
        continue 

# Now, content_structures contains only the readable text from the websites
cleaned_structure = re.sub(r'\n+', '\n', content_structure)


print(repr(cleaned_structure[:100]))
