import json
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date

FILE_PATH = "prices.json"
PRODUCT_NAME = "Sprouts Whey Protein Chocolate 32 oz"

def plot_price_history():
    # Load JSON data
    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    entries = data[PRODUCT_NAME]

    # Convert dates to datetime objects
    dates = [datetime.strptime(e["date"], "%Y-%m-%d") for e in entries]
    prices = [e["price"] for e in entries]

    # Plot
    plt.figure()
    plt.plot(dates, prices)
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title(f"Price History: {PRODUCT_NAME}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"price_history.png")
    # plt.show()
# Load JSON data
with open(FILE_PATH, "r") as f:
    data = json.load(f)

entries = data[PRODUCT_NAME]

# Convert dates to datetime objects
dates = [datetime.strptime(e["date"], "%Y-%m-%d") for e in entries]
prices = [e["price"] for e in entries]

# Plot
plt.figure()
plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title(f"Price History: {PRODUCT_NAME}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"price_history.png")
# plt.show()

if __name__ == "__main__":
    plot_price_history()
