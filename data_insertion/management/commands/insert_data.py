from django.core.management.base import BaseCommand
from data_insertion.models import Users, Products, Orders
from concurrent.futures import ThreadPoolExecutor
import threading
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Insert data concurrently into distributed databases'

    def handle(self, *args, **options):
        # Data to insert
        users_data = [
                            {'name': 'Alice', 'email': 'alice@example.com'},
                            {'name': 'Bob', 'email': 'bob@example.com'},
                            {'name': 'Charlie', 'email': 'charlie@example.com'},
                            {'name': 'David', 'email': 'david@example.com'},
                            {'name': 'Eve', 'email': 'eve@example.com'},
                            {'name': 'Frank', 'email': 'frank@example.com'},
                            {'name': 'Grace', 'email': 'grace@example.com'},
                            {'name': 'Alice', 'email': 'alice@example.com'},  # Should fail - duplicate
                            {'name': 'Henry', 'email': 'henry@example.com'},
                            {'email': 'jane@example.com'}# Should fail - missing name

                              ]
        products_data = [
                            {'name': 'Laptop', 'price': 1000.00},
                            {'name': 'Smartphone', 'price': 700.00},
                            {'name': 'Headphones', 'price': 150.00},
                            {'name': 'Monitor', 'price': 300.00},
                            {'name': 'Keyboard', 'price': 50.00},
                            {'name': 'Mouse', 'price': 30.00},
                            {'name': 'Laptop', 'price': 1000.00}, # Should fail - duplicate
                            {'name': 'Smartwatch', 'price': 250.00},
                            {'name': 'Gaming Chair', 'price': 500.00},
                            {'name': 'Earbuds', 'price': -50.00}  # Should fail - negative price
                              ]

        orders_data = [
                            {'user_id': 1, 'product_id': 1, 'quantity': 2},
                            {'user_id': 2, 'product_id': 2, 'quantity': 1},
                            {'user_id': 3, 'product_id': 3, 'quantity': 5},
                            {'user_id': 4, 'product_id': 4, 'quantity': 1},
                            {'user_id': 5, 'product_id': 5, 'quantity': 3},
                            {'user_id': 6, 'product_id': 6, 'quantity': 4},
                            {'user_id': 7, 'product_id': 7, 'quantity': 2},
                            {'user_id': 8, 'product_id': 8, 'quantity': 0},   # Should fail - zero quantity
                            {'user_id': 9, 'product_id': 1, 'quantity': -1},   # Should fail - negative quantity
                            {'user_id': 10, 'product_id': 11, 'quantity': 2}   # Should fail - invalid product_id
                            ]

        def insert_user(data):
            try:
                if 'name' not in data or not data['name']:
                    logger.warning(f"Invalid user - missing name: {data}")
                    return
                if '@' not in data.get('email', ''):
                    logger.warning(f"Invalid email: {data}")
                    return
                # Check for duplicates
                if Users.objects.filter(email=data['email']).exists():
                    logger.warning(f"Duplicate email: {data['email']}")
                    return
                Users.objects.get_or_create(**data)
                logger.info(f"Inserted user: {data.get('name', 'Unknown')}")
            except Exception as e:
                 logger.error(f"Error inserting user: {e}")

        def insert_product(data):
            try:
                if data['price'] < 0:
                    logger.warning(f"Invalid price: {data['price']}")
                    return
                # Check for duplicates (same name and price)
                if Products.objects.filter(name=data['name'], price=data['price']).exists():
                    logger.warning(f"Duplicate product: {data['name']}")
                    return
                Products.objects.get_or_create(**data)
                logger.info(f"Inserted product: {data['name']}")
            except Exception as e:
                logger.error(f"Error inserting product: {e}")
        
        def insert_order(data):
            try:
                if data['quantity'] <= 0:
                    logger.warning(f"Invalid quantity: {data['quantity']}")
                    return
                # Check if product exists
                if not Products.objects.filter(id=data['product_id']).exists():
                    logger.warning(f"Invalid product_id: {data['product_id']}")
                    return
                Orders.objects.create(**data)
                logger.info(f"Inserted order for user_id: {data['user_id']}")
            except Exception as e:
                logger.error(f"Error inserting order: {e}")

         # Concurrent insertion using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=1) as executor:  # Changed from 10 to 1
              # Process each type sequentially
            for user in users_data:
                executor.submit(insert_user, user)
            for product in products_data:
                executor.submit(insert_product, product)
            for order in orders_data:
                executor.submit(insert_order, order)
        #Concurrrent Execution
            # executor.map(insert_user, users_data)
            # executor.map(insert_product, products_data)
            # executor.map(insert_order, orders_data)

        self.stdout.write(self.style.SUCCESS('Data insertion completed'))