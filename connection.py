from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # load variables from .env

host=os.environ['DB_HOST']
port=os.environ['DB_PORT']
dbname=os.environ['DB_NAME']
user=user=os.environ['DB_USER']
password=os.environ['DB_PASSWORD']


try:
    # Connect to the database
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    cur = conn.cursor()

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
