from faker import Faker
import pandas as pd
import random

fake = Faker()

orders = []

for i in range(500):

    orders.append({
        "customer_id": random.randint(1, 100),
        "order_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        ),
        "order_status": random.choice(
            [
                "Delivered",
                "Shipped",
                "Pending"
            ]
        )
    })

df = pd.DataFrame(orders)

df.to_csv("orders.csv", index=False)

print("500 orders generated!")