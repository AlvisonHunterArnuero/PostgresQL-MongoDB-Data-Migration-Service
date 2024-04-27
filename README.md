# Integration Enginer Test
Este repositorio contiene el proyecto de prueba para Ingenieros de Integración. El objetivo principal de este proyecto es simular una infraestructura y problem set similar al que vería un Ingeniero de Integración en Ubiqua.

El problema es el siguiente: dado un dataset en una base de datos de PostgreSQL, analizar el esquema, los tipos de campos y las particularidades de cada cliente en el dataset. Utilizando el proceso de [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load), leer la data de PostgreSQL, la tranformarla con Python y cargue la data en la base de datos de Mongo.

El problema también requiere un poco de conocimiento previo o investigación sobre configuración de MongoDB, sistemas POSIX (Linux/Unix/macOS), llaves de SSH, droplets de Digital Ocean, comandos SQL y manejo de bases de dato relaciones como PostgreSQL.

## Pre-requisitos
- Tener acceso a una instancia de Digital Ocean
  - Un Public/Private keyset para acceder a la instancia
  - Utilizar comando **ssh -i path_to_private_key root@ipaddress**
- Acceso a la base de datos read-only de PostgreSQL

## Objetivos de la prueba
- Installar MongoDB localmente
- Crear una solución que carge las órdenes de PostgreSQL a una colección de Mongo
- Todas las órdenes se insertan sin duplicados, incluso cuando la solución se corre mútliples veces.
- La información del producto
- Product info joined from product table
- Subtotal, Tax y Total se calculan para cada órden
- La marca (**brand**) más popular se calcula para cada órden insertada
- Considerar que **is_promotion_day** debe de ser true/false dependiendo en la fecha de la órden y el campo **client promotion_date**


## Read Schema
Requiere investigación utilizando un tool como [DBeaver](https://dbeaver.io/) para leer los esquemas de data.

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
