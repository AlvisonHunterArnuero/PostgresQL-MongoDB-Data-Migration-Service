#### Steps to Run this solution on your local machine

1. Install the required Python modules:
   ```
   pip install psycopg2 pymongo tabulate decouple
   ```
2. You can alternatively use the following command to install all the requirements directly:
   ```
   pip install -r requirements.txt
   ```
### PostgresQL Setup Steps
To securely manage your PostgresQL database credentials, create an .env file in the project directory.
This file will contain sensitive information, so ensure it is not included in version control by 
adding it to your .gitignore file.

**Creating the .env File**
1. Create a new file named .env in the root of your project directory.
2. Add the following keys to the .env file, replacing your_db_name, your_db_user, your_db_password, your_db_host, 
and your_db_port with your actual PostgresQL database credentials:
   ```python
   PG_DBNAME='your_db_name'
   PG_USER='your_db_user'
   PG_PASSWORD='your_db_password'
   PG_HOST='your_db_host'
   PG_PORT='your_db_port'
   ```
3. Update PostgresQL config details in the `solution.py` file to match your PostgresQL database configuration.
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
---
### Digital Ocean Droplet
Create and Access Your Droplet
As part of the requirements in the given tasks, this project should be setup and run on a DigitalOcean Droplet. 
You'll need a [DigitalOcean](https://www.digitalocean.com) account to create one. A DigitalOcean Droplet is 
essentially a cloud-based virtual private server (VPS) that runs on Linux. Think of it as a computer running 
in the cloud that you can control and use for your projects. It provides scalable and affordable computing resources,
offering more control and flexibility than shared hosting.

### Accessing Your DigitalOcean Droplet Using SSH**

**Create a Droplet:** To set up a Virtual Private Server (VPS) known as a Droplet, begin by registering for 
a DigitalOcean account. Select a plan that suits your needs and configure your Droplet through your 
dashboard. This includes generating SSH key pairs, which are essential for secure access to your Droplet.
Download these keys locally for future use.

**Access via SSH:** Once created, use the IP address and login credentials provided by DigitalOcean to connect to your
Droplet via SSH client (e.g., terminal for macOS/Linux). I personally use Warp as my main terminal on macOS Sonoma.
To access this Droplet via SSH, please use the command below:
   ```
   ssh -i path_to_your_private_key root@ip_address
   ```
Once you press Enter, you will be prompted for your passphrase (if you set one when creating the SSH keys), 
granting you access to your Digital Ocean droplet. 

**Private Key Permissions too open Error:**
Occasionally, macOS may raise concerns about unknown hosts or excessively permissive permissions on your private key.
When encountering this issue, you might see an error message similar to the following after entering a command:
   ```
   Permissions 0644 for 'your_private_key' are too open.
   It is required that your private key files are NOT accessible by others.
   This private key will be ignored.
   Load key "your_private_key": bad permissions
   root@ip_address: Permission denied (publickey).
   ```
You can resolve this issue by adjusting the permissions on your private key file to be more restrictive
and better protected. Use the following command to change the permissions:
   ```
   chmod 600 your_private_key
   ```
This command will set the permissions on `your_private_key` file to 600, ensuring that only the owner (you) 
has read and write permissions, while restricting access for anyone else. After running this command, you should 
be able to use your private key without encountering permission errors. To reconnect with your SSH client, 
use the following command:
   ```
   ssh -i path_to_your_private_key root@ip_address
   ```


