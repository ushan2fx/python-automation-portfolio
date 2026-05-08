"""
Web Scraper Template - Portfolio Project 2
Author: Vajira L.
Description: Ethical scraper for public listings (demo)
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_products(base_url, pages=2):
    headers = {'User-Agent': 'Mozilla/5.0 (Portfolio Demo)'}
    all_data = []
    
    for page in range(1, pages+1):
        url = f"{base_url}/catalogue/page-{page}.html"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        products = soup.find_all('article', class_='product_pod')
        for p in products:
            title = p.h3.a['title']
            price = p.find('p', class_='price_color').text
            all_data.append({'Title': title, 'Price': price})
        
        time.sleep(1)
    
    df = pd.DataFrame(all_data)
    df.to_csv('scraped_products.csv', index=False)
    return df

if __name__ == "__main__":
    scrape_products("https://books.toscrape.com", pages=3)
