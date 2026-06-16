from faker import Faker
import pandas as pd
import random
from datetime import timedelta

fake = Faker()

shipments = []

for order_id in range(1, 501):

    shipped = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    delivered = shipped + timedelta(
        days=random.randint(2, 10)
    )

    shipments.append({
        "order_id": order_id,
        "shipped_date": shipped,
        "delivered_date": delivered
    })

df = pd.DataFrame(shipments)

df.to_csv(
    "shipments.csv",
    index=False
)

print("500 shipments generated!")