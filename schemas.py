# Define MongoDB OrderSchema
order_schema = {
    'uid': int,
    'date_of_order': str,
    'client_uid': int,
    'client_name': str,
    'client_address': str,
    'latitude': float,
    'longitude': float,
    'status': str,
    'subtotal': float,
    'taxes': float,
    'total': float,
    'is_promotion_day': bool,
    'most_popular_brand': str
}

# Define MongoDB OrderItemsSchema
order_items_schema = {
    'uid': int,
    'quantity': int,
    'price': float,
    'name': str,
    'brand': str
}
