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
                            {'name': 'Alice', 'email': 'alice@example.com'},  # Duplicate
                            {'name': 'Henry', 'email': 'henry@example.com'},
                            {'name': 'Jane', 'email': 'jane@example.com'}
                              ]
        products_data = [
                            {'name': 'Laptop', 'price': 1000.00},
                            {'name': 'Smartphone', 'price': 700.00},
                            {'name': 'Headphones', 'price': 150.00},
                            {'name': 'Monitor', 'price': 300.00},
                            {'name': 'Keyboard', 'price': 50.00},
                            {'name': 'Mouse', 'price': 30.00},
                            {'name': 'Laptop', 'price': 1000.00},  # Duplicate
                            {'name': 'Smartwatch', 'price': 250.00},
                            {'name': 'Gaming Chair', 'price': 500.00},
                            {'name': 'Earbuds', 'price': -50.00}  # Invalid price
                              ]

        orders_data = [
                            {'user_id': 1, 'product_id': 1, 'quantity': 2},
                            {'user_id': 2, 'product_id': 2, 'quantity': 1},
                            {'user_id': 3, 'product_id': 3, 'quantity': 5},
                            {'user_id': 4, 'product_id': 4, 'quantity': 1},
                            {'user_id': 5, 'product_id': 5, 'quantity': 3},
                            {'user_id': 6, 'product_id': 6, 'quantity': 4},
                            {'user_id': 7, 'product_id': 7, 'quantity': 2},
                            {'user_id': 8, 'product_id': 8, 'quantity': 0},  # Invalid quantity
                            {'user_id': 9, 'product_id': 1, 'quantity': -1},  # Invalid quantity
                            {'user_id': 10, 'product_id': 11, 'quantity': 2}  # Invalid product_id
                            ]

        def insert_user(data):
            try:
                if '@' not in data['email']:  # Application-level validation
                    logger.warning(f"Invalid email: {data['email']}")
                    return
                Users.objects.get_or_create(**data)
                logger.info(f"Inserted user: {data['name']}")
            except Exception as e:
                logger.error(f"Error inserting user: {e}")

        def insert_product(data):
            try:
                if data['price'] < 0:  # Application-level validation
                    logger.warning(f"Invalid price: {data['price']}")
                    return
                Products.objects.get_or_create(**data)
                logger.info(f"Inserted product: {data['name']}")
            except Exception as e:
                logger.error(f"Error inserting product: {e}")

        def insert_order(data):
            try:
                if data['quantity'] < 0:  # Application-level validation
                    logger.warning(f"Invalid quantity: {data['quantity']}")
                    return
                Orders.objects.create(**data)
                logger.info(f"Inserted order for user_id: {data['user_id']}")
            except Exception as e:
                logger.error(f"Error inserting order: {e}")

        # Concurrent insertion using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(insert_user, users_data)
            executor.map(insert_product, products_data)
            executor.map(insert_order, orders_data)

        self.stdout.write(self.style.SUCCESS('Data insertion completed'))