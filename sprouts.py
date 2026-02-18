import requests
from bs4 import BeautifulSoup
import json
from datetime import date
from pathlib import Path
from price_tracker import PriceTracker

FILE_PATH = "prices.json"
PRODUCT_NAME = "Sprouts Whey Protein Chocolate 32 oz"

today = str(date.today())

URL = "https://shop.sprouts.com/store/sprouts/products/17859053-sprouts-whey-protein-chocolate-32-oz"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find price element on Sprouts product page
price_element = soup.select_one("div[class='e-4vupfk']")  # example selector

    
if price_element:
    price_text = price_element.span.get_text(strip=True)
    price = float(price_text.replace("$", ""))
    print("Current price:", price)
    
    tracker = PriceTracker("prices.json")
    tracker.append_price(PRODUCT_NAME, price)
else:
    print("Price not found")
