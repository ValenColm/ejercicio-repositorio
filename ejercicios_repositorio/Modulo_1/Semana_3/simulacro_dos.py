inventory = [
    {"product_name": "A54 5G SMARTPHONE", "brand":"SAMSUNG", "category":"PHONES", "unit_price": 1200000, "stock_quantity": 35, "warranty_months": 12},
    {"product_name": "ideapad 3 15 laptop", "brand": "lenovo", "category": "computer", "unit_price": 230000, "stock_quantity": 23, "warranty_months": 12},
    {"product_name": "55-inch 4k uhd tv", "brand": "LG", "category": "tvs", "unit_price": 2800000, "stock_quantity": 23, "warrnty_months": 12},
    {"product_name": "airdots tws wireless earbuds", "brand": "xiaomi", "category": "audio", "unit_price": 100000, "stock_quantity": 32, "warranty_months": 3 },
    {"product_name": "playStation 5 console", "brand": "sony", "category": "gaming", "unit_price": 3000000, "stock_quantity": 10, "warranty_months": 12},
]

def show_inventory():
    print("=======inventary of product=======")
    for product_name in inventory:
            print(f"product_name: {product_name['product_name']}, : brand {product_name['brand']}, category: {product_name['category']}, unit_price: {product_name["unit_price"]}, stock_quantity: {product_name["stock_quantity"]}, warranty_months: {product_name["warranty_months"]}")



def register_product():
    