import json
from product_app.models import Product

def import_products():
    try:
        with open('products.json') as f:
            data = json.load(f)
        for item in data:
            Product.objects.get_or_create(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                price=item['price'],
                stock_quantity=item['stock_quantity'] if 'stock_quantity' in item else 0
            )

        print("Products imported successfully!")

    except Exception as e:
        print(f"Error: {e}")
