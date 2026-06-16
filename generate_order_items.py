import pandas as pd
import random

order_items = []

for i in range(1000):

    order_items.append({
        "order_id": random.randint(1, 500),
        "product_id": random.randint(1, 6),
        "quantity": random.randint(1, 5),
        "unit_price": random.choice(
            [25, 35, 40, 90, 800, 1200]
        )
    })

df = pd.DataFrame(order_items)

df.to_csv(
    "order_items.csv",
    index=False
)

print("1000 order items generated!")