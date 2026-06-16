from faker import Faker
import pandas as pd

fake = Faker()

customers = []

for i in range(100):

    customers.append({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "city": fake.city(),
        "country": fake.country(),
        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    })

df = pd.DataFrame(customers)

df.to_csv("customers.csv", index=False)

print("100 customers generated!")