from typing import Any, KeysView

from decouple import config  # type: ignore
import psycopg2  # type: ignore
import pymongo  # type: ignore
from tabulate import tabulate  # type: ignore
from utils import is_promo_day, unique_id, print_table

# Import schemas
from schemas import order_schema, order_items_schema

# Load environment variable values
PG_DBNAME: Any = config('PG_DBNAME')
PG_USER: Any = config('PG_USER')
PG_PASSWORD: Any = config('PG_PASSWORD')
PG_HOST: Any = config('PG_HOST')
PG_PORT: Any = config('PG_PORT')

# ----------- PostgresSQL Connection Setup  -----------

# Connect to PostgresSQL using the above environment variable values
try:
    # Attempt to establish a connection to PostgresQL
    pg_conn = psycopg2.connect(
        dbname=PG_DBNAME,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )
    # Create the connection cursor instance
    print("PostgresQL connection established.")
    pg_cur: Any = pg_conn.cursor()

except psycopg2.OperationalError as e:
    # Handle connection errors
    print(f"Error connecting to PostgresQL: {e}")

# ----- PostgresQL SQL procedures  -----------

# Define All Table Headers lists
clients_header = ["Id", "Name", "Address", "Promo Day"]
products_header = ["Id", "Name", "Barcode", "Brand", "Unit Price", "Tax Rate"]
orders_header = ["Id", "Order Date", "Client Id", "Latitude", "Longitude", "Status"]
order_items_header = ["Id", "Product Id", "Quantity"]
popular_brand_header = ["uId", "Order Date", "Client Id", "Latitude", "Longitude", "Status", "Popular Brand"]
order_highest_item_header = ["Id", "Order Date", "Client Id", "Latitude", "Longitude", "Status", "Id", "Product Id",
                             "Quantity", "UId", "Name", "Barcode", "Brand", "Unit Price", "Tax Rate"]

# Define a dictionary to store SQL queries for better readability and easier editing.
# Each key represents a specific query, with the value being the corresponding SQL string.

pg_queries = {
    "clients": "SELECT * FROM clients",
    "products": "SELECT * FROM products",
    "orders": "SELECT * FROM orders",
    "order_items": "SELECT * FROM order_items",
    "order_highest_item": """
        SELECT * FROM orders 
        JOIN order_items ON orders.uid = order_items.order_uid 
        JOIN products ON products.uid = order_items.product_uid
    """,
    "popular_brand": """
        SELECT *, (
            SELECT brand FROM order_items 
            JOIN products ON order_items.product_uid = products.uid 
            AND order_items.order_uid = orders.uid 
            ORDER BY order_items.quantity DESC LIMIT 1
        ) AS popular_brand FROM orders
    """,
}

# SQL queries to extract data from PostgresQL DB
try:
    pg_cur.execute(pg_queries["clients"])
    clients: Any = pg_cur.fetchall()
    print_table("Clients Table", clients, clients_header)

    pg_cur.execute(pg_queries["products"])
    products: Any = pg_cur.fetchall()
    print_table("Products Table", products, products_header)

    pg_cur.execute(pg_queries["orders"])
    orders: Any = pg_cur.fetchall()
    print_table("Orders Table", orders, orders_header)

    pg_cur.execute(pg_queries["order_items"])
    order_items: Any = pg_cur.fetchall()
    print_table("Order Items Table", order_items, order_items_header)

    pg_cur.execute(pg_queries["order_highest_item"])
    order_highest_item: Any = pg_cur.fetchall()
    print_table("Product Info Joined from Product Table", order_highest_item, order_highest_item_header)

    pg_cur.execute(pg_queries["popular_brand"])
    popular_brand: Any = pg_cur.fetchall()
    print_table("Most Popular Brand Table", popular_brand, popular_brand_header)

except psycopg2.Error as e:
    print("Error While processing this Query: ", e.pgerror)

# Close PostgresQL Connection
pg_cur.close()
pg_conn.close()

# ----------- MongoDB Connection Setup  -----------

# Connect to MongoDB and create its instance
mongo_client = pymongo.MongoClient('localhost', 27017)

# Check if the database exists, just for dev purposes
if 'integrationsDB' in mongo_client.list_database_names():
    # Drop this DB temporary until we are good to go with the collected data
    mongo_client.drop_database('integrationsDB')
    print("Database 'integrationsDB' dropped.")

# Create the database
mongo_db = mongo_client['integrationsDB']

# Create all MongoDB collections
orders_collection = mongo_db['orders']

# Create indexes for MongoDB collections
orders_collection.create_index('uid', unique=True)

# ----- MongoDB Database Data Transformation procedures  -----------

# Orders Iteration to insert data in integrationsDB MongoDB db
for order in orders:
    # Determine if it's a promotion day
    order_promo_day: tuple[Any] = next(client[3] for client in clients if client[0] == order[2]),
    is_promotion_day: bool = is_promo_day(str(order[1]), order_promo_day[0])

    # Get order items information to add it to MongoDB orders
    order_items_details: tuple[Any] = next(item for item in order_items if item[0] == order[0]),

    # Let's get current product details as well
    current_product: Any = next(product for product in products if product[0] == order_items_details[0][1])

    # Calculate subtotal, taxes, totals
    subtotal: float = float(current_product[4])
    taxes: float = float(current_product[5])
    total: float = round(float(current_product[4]) * (1 + float(current_product[5])), 2)

    # Calculate most popular brand as per integration request
    most_popular_brand: tuple[Any] = next(brand[6] for brand in popular_brand if brand[0] == order[0]),

    # Let's build the dictionary containing the summary of all this info for MONGODB
    order_items_dict: dict[str, Any] = {
        "uid": order_items_details[0][0],
        "quantity": order_items_details[0][2],
        "price": total,
        "name": current_product[1],
        "brand": current_product[3],
    }

    # Generate a unique uid for the order
    order_uid: str = unique_id()

    # Insert order data collected from PostgresQL into our MongoDB database
    try:
        orders_collection.insert_one({
            'uid': order[0],
            'date_of_order': order[1],
            'client_uid': order[2],
            'client_name': next(client[1] for client in clients if client[0] == order[2]),
            'client_address': next(client[2] for client in clients if client[0] == order[2]),
            'latitude': order[3],
            'longitude': order[4],
            'status': order[5],
            'subtotal': subtotal,
            'taxes': taxes,
            'total': total,
            'is_promotion_day': is_promotion_day,
            'most_popular_brand': most_popular_brand[0],
            'order_items': order_items_dict,
        })
    except pymongo.errors.DuplicateKeyError as e:
        print("Error: Duplicated key", e)
    except Exception as e:
        print("Error inserting data:", e)
    else:
        print(f"Data inserted successfully for order# {order[0]}")

# Fetch orders from MongoDB
orders = list(orders_collection.find())

# Display orders using tabulate
if orders:
    mongo_tbl_headers: KeysView[str] = orders[0].keys()
    rows = [[order[field] for field in mongo_tbl_headers] for order in orders]
    # noinspection PyTypeChecker
    print(tabulate(rows, headers=mongo_tbl_headers, tablefmt="fancy_grid"))
else:
    print("No orders found.")

# Close Mongo Connection
mongo_client.close()

# Wrap up this solution letting the user know that all is now ready
print("All Integration Engineer Test requests have been completed!")
