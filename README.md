# Distributed System Simulation with Django

This project simulates a distributed system where different types of data (Users, Products, Orders) are stored in separate SQLite databases. Multiple threads perform simultaneous insert operations into these databases. The project is built using Django and Python.

---

## Project Overview

### Task Description:
The task involves:
- Creating three models:
  - Users (stored in `users.db`)
  - Products (stored in `products.db`)
  - Orders (stored in `orders.db`)
- Simulating at least 10 simultaneous insertions for each model using multiple threads.
- Handling all validations in the application logic (no database-level validation).
- Running a single command to perform the insertions and display the results.

---

## Requirements

To run this project, you need:
- Python 3.8 or higher
- Django 4.0 or higher

---

## Project Structure

distributed_system/
  data_insertion/
    migrations/
    models.py
    management/
      commands/
        insert_data.py
  distributed_system/
    settings.py
    urls.py
  manage.py
  README.md

---

## Setup Instructions

1. Clone the Repository:  
Clone the project repository to your local machine:


2. Create a Virtual Environment:  
Create and activate a virtual environment


3. Install Dependencies
  Python
  Django
  sqlite3

5. Configure Databases:  
In `distributed_system/settings.py`, configure the databases to use separate SQLite files for Users, Products, and Orders.
DATABASES = {

  'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'users_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users.db',
    },
    'products_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'products.db',
    },
    'orders_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'orders.db',
    }
}
6. Run Migrations:  
Create the database tables by running migrations for each database:
python manage.py makemigrations
python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db


---

## Running the Task

1. Insert Data Concurrently:  
Run the management command to perform concurrent insertions:


2. Expected Output:  
The command will:
- Insert 10 records into each of the Users, Products, and Orders tables.
- Log the results of each insertion to the console.

Example output:
Inserted user: Alice Inserted product: Laptop Inserted order for user_id: 1 ... Data insertion completed

---

## Validation

All validations are handled in the application logic:
- Users: Check for valid email format and duplicate emails.
- Products: Ensure no duplicate products and price is non-negative.
- Orders: Ensure quantity is non-negative and product_id exists.

---


