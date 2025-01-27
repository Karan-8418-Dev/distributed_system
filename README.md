# Distributed System Simulation with Django

This project simulates a distributed system where different types of data (Users, Products, Orders) are stored in separate SQLite databases. Multiple threads perform simultaneous insert operations into these databases. The project is built using Django and Python.

## Project Overview

Task Description:
The task involves:
- Creating three models:
  - Users (stored in users.db)
  - Products (stored in products.db)
  - Orders (stored in orders.db)
- Simulating at least 10 simultaneous insertions for each model using multiple threads.
- Handling all validations in the application logic (no database-level validation).
- Running a single command to perform the insertions and display the results.

## Requirements

To run this project, you need:
- Python 3.8 or higher
- Django 4.0 or higher

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

## Setup Instructions

1. Clone the Repository:
Clone the project repository to your local machine:

git clone <repository-url>
cd distributed_system

2. Create a Virtual Environment:
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
Install the required dependencies:

pip install django

4. Configure Databases:
In distributed_system/settings.py, configure the databases to use separate SQLite files for Users, Products, and Orders.

5. Run Migrations:
Create the database tables by running migrations for each database:

python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db

## Running the Task

1. Insert Data Concurrently:
Run the management command to perform concurrent insertions:

python manage.py insert_data

2. Expected Output:
The command will:
- Insert 10 records into each of the Users, Products, and Orders tables.
- Log the results of each insertion to the console.

Example output:
Inserted user: Alice
Inserted product: Laptop
Inserted order for user_id: 1
...
Data insertion completed

## Validation

All validations are handled in the application logic:
- Users: Check for valid email format.
- Products: Ensure price is non-negative.
- Orders: Ensure quantity is non-negative.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.
