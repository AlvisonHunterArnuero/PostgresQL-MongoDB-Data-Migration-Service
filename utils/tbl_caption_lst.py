from typing import List
# -- Table Data Feeders

# print table title parameter
tbl_caption_titles: dict[str, str] = {
    "clients": "Clients Table",
    "products": "Products Table",
    "orders": "Orders Table",
    "order_items": "Order Items Table",
    "order_highest_item": "Product Info Joined from Product Table",
    "popular_brand": "Most Popular Brand Table",
}

# Define All Table Headers lists
tbl_headers: dict[str, List[str]] = {
    "clients_header": ["Id", "Name", "Address", "Promo Day"],
    "products_header": ["Id", "Name", "Barcode", "Brand", "Unit Price", "Tax Rate"],
    "orders_header": ["Id", "Order Date", "Client Id", "Latitude", "Longitude", "Status"],
    "order_items_header": ["Id", "Product Id", "Quantity"],
    "popular_brand_header": ["uId", "Order Date", "Client Id", "Latitude", "Longitude", "Status", "Popular Brand"],
    "order_highest_item_header": ["Id", "Order Date", "Client Id", "Latitude", "Longitude", "Status", "Id",
                                  "Product Id",
                                  "Quantity", "UId", "Name", "Barcode", "Brand", "Unit Price", "Tax Rate"]
}
