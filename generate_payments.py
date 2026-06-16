from faker import Faker
import pandas as pd
import random

fake = Faker()

payments = []

for order_id in range(1, 501):

    payments.append({
        "order_id": order_id,
        "payment_method": random.choice(
            [
                "Credit Card",
                "Debit Card",
                "PayPal"
            ]
        ),
        "payment_amount": random.randint(
            50,
            5000
        ),
        "payment_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        )
    })

df = pd.DataFrame(payments)

df.to_csv(
    "payments.csv",
    index=False
)

print("500 payments generated!")