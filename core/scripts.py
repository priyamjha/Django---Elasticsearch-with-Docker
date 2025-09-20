import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from products.models import Products

def load_data_from_csv(file_path):
    """Load data from a CSV file into the Products model."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    try:
        with open(file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            products = []
            
            for row in reader:
                product_name = row.get('product_name')
                product_brand = row.get('brand')
                product_price = row.get('price')
                
                if not product_name or not product_brand:
                    print(f"Skipping row with missing data: {row}")
                    continue
                
                products.append(Products(
                    product_name=product_name,
                    product_brand=product_brand,
                    product_price=product_price
                ))
                
            Products.objects.bulk_create(products)
            print(f"Successfully loaded {len(products)} products.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

    
if __name__ == "__main__":
    csv_file_path = "MOCK_DATA.csv"
    load_data_from_csv(csv_file_path)