# Integrations Engineer - Python Technical Test
This repository contains the test project for Integration Engineers. The main objective of this project is to simulate an infrastructure and problem set similar to what an Integration Engineer would encounter at the company you will be working for.

**Problem Scope:** The problem is as follows: Given a dataset in a PostgresQL database, analyze the schema, field types, and specificities of each client in the dataset. Using the [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) process, read the data from PostgresQL, transform it with Python, and load the data into the Mongo database.

The problem also requires some prior knowledge or research on MongoDB configuration, POSIX systems (Linux/Unix/macOS), SSH keys, Digital Ocean droplets, SQL commands, and handling relational databases like PostgreSQL.
## Prerequisites
- To have prior access to a Digital Ocean instance.
  - A Public/Private SSH Key-sets to access the instance
  - Use the command **ssh -i path_to_private_key root@ipaddress** to access the droplet
- Get full access to read-only PostgresQL database to get the data

## Test Objectives
- Install MongoDB locally
Create a solution that loads orders from PostgresQL into a Mongo collection
- - All orders are inserted without duplicates, even when the solution is run multiple times.
- Product information
- Product info joined from product table
- Subtotal, Tax, and Total are calculated for each order
- The most popular brand is calculated for each inserted order
- Consider that is_promotion_day should be true/false depending on the order date and the client promotion_date field

## Read Schema
Requires doing database analysis and research using a tool like DBeaver [DBeaver](https://dbeaver.io/) to read the data schemas.

### Tables
  - Clients
  - Products
  - Orders
  - Order Items

## Write schema

### Order
  - uid
  - date_of_order
  - client_uid
  - client_name
  - client_address
  - latitude
  - longitude
  - status
  - subtotal
  - taxes
  - total
  - is_promotion_day
  - most_popular_brand
  - OrderItems:
    - uid
    - quantity
    - price
    - name
    - brand
