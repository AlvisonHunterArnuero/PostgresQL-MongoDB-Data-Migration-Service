#### Steps to Run this solution on your local machine

1. Install the required Python modules:
   ```
   pip install psycopg2 pymongo tabulate decouple
   ```
2. You can alternatively use the following command to install the requirements directly:
   ```
   pip install -r requirements.txt
   ```
### PostgresQL Setup Steps
1. Create an `.env` file in the project directory to handle PostgresSQL DB credentials. Add the following content to the `.env` file:
   ```
   PG_DBNAME=your_db_name
   PG_USER=your_db_user
   PG_PASSWORD=your_db_password
   PG_HOST=your_db_host
   PG_PORT=your_db_port

   ```
2. Update PostgresQL config details in the `solution.py` file to match your PostgresQL database configuration.
```python
from decouple import config # type: ignore
import psycopg2 # type: ignore
import pymongo # type: ignore
from tabulate import tabulate # type: ignore
from utils import is_promo_day, unique_id, print_table

# Import schemas
from schemas import order_schema, order_items_schema

# Load environment variable values
PG_DBNAME = config('PG_DBNAME')
PG_USER = config('PG_USER')
PG_PASSWORD = config('PG_PASSWORD')
PG_HOST = config('PG_HOST')
PG_PORT = config('PG_PORT')

# ----------- PostgresQL Connection Setup  -----------

# Connect to PostgresQL using the above environment variable values
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
    pg_cur = pg_conn.cursor()

except psycopg2.OperationalError as e:
    # Handle connection errors
    print(f"Error connecting to PostgresQL: {e}")

```

### MongoDB setup steps

1. Install MongoDB locally. You can download MongoDB Community Server from the official MongoDB website: [MongoDB Download](https://www.mongodb.com/try/download/community).

2. Run MongoDB either via the `mongo` command or using `brew` services (for macOS):
   - Use `brew services start mongodb-community` to start MongoDB.
   - Use `brew services stop mongodb-community` to stop MongoDB.

3. Finally, to run the solution, type the following command in your terminal and hit enter:
   ```
   python3 solution.py
   ```
### Virtual Environment Setup and activation
Finally, as an optional step, it is recommended to run this application within a virtual environment. 
Running Python apps in virtual environments (venv) is quite important and a good practice because it 
allows you to isolate your project's dependencies from other projects and the system Python installation.

This means you can have different versions of packages for different projects without conflicts. 
It also helps in keeping your system Python installation clean and avoids potential dependency issues.

To create a virtual environment, activate it, and deactivate it, you can use the following shell commands:

#### Create a virtual environment:
   ```
   python3 -m venv myenv
   ```
This command creates a new virtual environment named myenv in the current directory.

#### Activate the virtual environment (Linux/Mac):
   ```
   source myenv/bin/activate
   ```
For Windows OS, use the below command:
   ```
   myenv\Scripts\activate
   ```
Activating the virtual environment modifies the shell's PATH to use the Python interpreter and packages
from the virtual environment.

#### Deactivate the virtual environment:
   ```
   deactivate
   ```
This command deactivates the current virtual environment, restoring the shell's PATH to its original state.
Remember to replace myenv with the name you want to give to your virtual environment.