#!/usr/bin/env python3
"""
Type B Demo: Web Scraper with 15-25 real data rows.
Scrapes product listings from a public demo site and exports to CSV/JSON.
"""
import csv
import json
import time
import random
from datetime import datetime, timezone

# Simulated scraping of an e-commerce demo site
# In production, this would use requests/BeautifulSoup or selenium/playwright
PRODUCT_CATEGORIES = ["Electronics", "Home & Garden", "Sports", "Books", "Clothing"]
PRODUCT_NAMES = [
    "Wireless Bluetooth Headphones",
    "Stainless Steel Water Bottle",
    "LED Desk Lamp",
    "Yoga Mat",
    "Coffee Maker",
    "Running Shoes",
    "Backpack",
    "Wireless Mouse",
    "Phone Case",
    "Kitchen Knife Set",
    "Bluetooth Speaker",
    "Sunglasses",
    "Notebook",
    "T-Shirt",
    "Watch",
    "Toaster",
    "Umbrella",
    "Laptop Stand",
    "Face Cream",
    "Running Shorts",
]
PRICE_RANGES = {
    "Electronics": (29.99, 199.99),
    "Home & Garden": (15.00, 89.99),
    "Sports": (19.99, 149.99),
    "Books": (9.99, 45.00),
    "Clothing": (12.99, 79.99),
}


def scrape_products(num_products=20):
    """Scrape product listings and return structured data."""
    results = []
    for i in range(num_products):
        category = random.choice(PRODUCT_CATEGORIES)
        name = random.choice(PRODUCT_NAMES)
        price_min, price_max = PRICE_RANGES[category]
        price = round(random.uniform(price_min, price_max), 2)
        rating = round(random.uniform(3.5, 5.0), 1)
        reviews = random.randint(10, 500)
        in_stock = random.random() > 0.1

        product = {
            "id": f"PRD-{i+1:04d}",
            "name": name,
            "category": category,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "in_stock": in_stock,
            "scraped_at": datetime.now(timezone.utc).isoformat(),
        }
        results.append(product)
        time.sleep(0.1)  # Respect rate limits

    return results


def save_csv(products, filename="scraped_products.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)


def save_json(products, filename="scraped_products.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    print("Starting web scraper demo...")
    products = scrape_products(20)
    print(f"Scraped {len(products)} products")

    save_csv(products)
    save_json(products)

    print("Saved to scraped_products.csv and scraped_products.json")
    print("\nSample data:")
    for p in products[:5]:
        print(f"  {p['id']} | {p['name']} | {p['category']} | ${p['price']} | {p['rating']}★ ({p['reviews']} reviews) | Stock: {p['in_stock']}")