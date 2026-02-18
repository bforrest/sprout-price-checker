import json
from pathlib import Path
from datetime import date

class PriceTracker:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.data = self._load()

    def _load(self):
        if not self.file_path.exists():
            return {}
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def append_price(self, product_name, price):
        today = str(date.today())

        if product_name not in self.data:
            self.data[product_name] = []

        self.data[product_name] = [
            entry for entry in self.data[product_name]
            if entry["date"] != today
        ]

        self.data[product_name].append({
            "date": today,
            "price": float(price)
        })

        self._save()
