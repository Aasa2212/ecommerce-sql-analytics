import pandas as pd
import psycopg2

df = pd.read_csv("customers.csv")

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_portfolio",
    user="postgres",
    password="YOUR_PASSWORD"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO customers
        (first_name,last_name,email,city,country,signup_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        row["first_name"],
        row["last_name"],
        row["email"],
        row["city"],
        row["country"],
        row["signup_date"]
    ))

conn.commit()

cur.close()
conn.close()

print("100 customers loaded successfully!")