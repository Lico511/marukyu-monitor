import requests

URL = "https://www.marukyu-koyamaen.co.jp/english/shop/products/1141020c1"

response = requests.get(URL)

if "Out of stock" in response.text:
    print("❌ Still out of stock")
else:
    print("✅ Product may be in stock!")
