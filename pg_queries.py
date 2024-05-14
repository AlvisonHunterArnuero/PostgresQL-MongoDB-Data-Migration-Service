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