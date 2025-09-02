from dotenv import load_dotenv
import os
import psycopg2 # PostgreSQL adapter for Python
import pyodbc # ODBC adapter for Python

load_dotenv()  # load variables from .env

# MS SQL Server connection example (uncommented) to Azure SQL Database

server=os.environ['DB_SEVER']
port=os.environ['DB_PORT']
database=os.environ['DB_NAME']
username=user=os.environ['DB_USER']
password=os.environ['DB_PASSWORD']
driver = '{ODBC Driver 18 for SQL Server}'  # Make sure this driver is installed

# Create connection string
conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()

    # Create table if it doesn't exist (Commented out to avoid errors if run multiple times)
    # cur.execute("""
    #     IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='test_table' AND xtype='U')
    #     CREATE TABLE test_table (
    #         id INT IDENTITY(1,1) PRIMARY KEY,
    #         name NVARCHAR(50),
    #         age INT
    #     )
    # """)
    # conn.commit()
    # print("Test table created successfully!")

    # Insert a row (Commented out to avoid duplicate entries on multiple runs)
    # cur.execute("INSERT INTO test_table (name, age) VALUES (?, ?)", ("Alice", 25))
    # conn.commit()
    # print("Inserted a row successfully!")

    # Query the table
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()
    print("Current rows in table:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)


# PostgreSQL connection example (commented out) to Neon

# Values need for PostgreSQL connection to Neon
# HOST=os.environ['DB_HOST']
# port=os.environ['DB_PORT']
# database=os.environ['DB_NAME']
# username=user=os.environ['DB_USER']
# password=os.environ['DB_PASSWORD']

# try:
#     # Connect to the database
#     conn = psycopg2.connect(
#         host=host,
#         port=port,
#         dbname=dbname,
#         user=user,
#         password=password
#     )

#     cur = conn.cursor()

#     # Query the table
#     cur.execute("SELECT * FROM test_table")
#     rows = cur.fetchall()
#     print("Current rows in table:")
#     for row in rows:
#         print(row)

#     cur.close()
#     conn.close()

# except Exception as e:
#     print("An error occurred:", e)
