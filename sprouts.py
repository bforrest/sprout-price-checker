import requests
import os
from bs4 import BeautifulSoup
import json
from datetime import date
from pathlib import Path
from price_tracker import PriceTracker
import smtplib
from email.message import EmailMessage
from plot_prices import plot_price_history

FILE_PATH = "prices.json"
PRODUCT_NAME = "Sprouts Whey Protein Chocolate 32 oz"


def send_email(subject, body, to_email, attachment_path=None):
    sender_email = "bforrest30@gmail.com"
    app_password = os.getenv("SPROUTS_APP_PASSWORD")

    print(f"app password {app_password}")
    
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach file if provided
    if attachment_path:
        file_path = Path(attachment_path)
        with open(file_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype="image",
                subtype="png",
                filename=file_path.name
            )

    # Connect and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Email sent successfully.")
    
    
today = str(date.today())

URL = "https://shop.sprouts.com/store/sprouts/products/17859053-sprouts-whey-protein-chocolate-32-oz"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find price element on Sprouts product page
price_element = soup.select_one("div[class='e-4vupfk']")  # example selector
sale_price_element = soup.select_one("span[class='e-vdvio']")  # example selector
    
if price_element:
    price_text = price_element.span.get_text(strip=True)
    price = float(price_text.replace("$", ""))
    print("Current price:", price)
    
    tracker = PriceTracker("prices.json")
    tracker.append_price(PRODUCT_NAME, price)
    plot_price_history()
else:
    print("Price not found")
    
if sale_price_element:
  print("🚨 Sale price:", sale_price_element.get_text(strip=True))
  app_password = os.getenv("SPROUTS_APP_PASSWORD")
  send_email(
    subject="🚨 Whey Protein Price Update 💪",
    body="Here is the latest price chart.",
    to_email="bforrest30+sprouts@gmail.com",
    attachment_path=f"price_history.png"
  )
