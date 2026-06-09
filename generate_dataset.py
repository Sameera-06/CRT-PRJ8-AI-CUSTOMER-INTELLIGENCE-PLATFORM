from faker import Faker
import pandas as pd
import random

fake = Faker()

cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Pune"
]

products = [
    "Laptop",
    "Phone",
    "Watch",
    "Shoes",
    "Headphones",
    "Bag"
]

categories = [
    "Electronics",
    "Fashion",
    "Accessories"
]

data = []

for i in range(1,501):

    age = random.randint(18,70)

    income = random.randint(
        20000,
        150000
    )

    spending_score = random.randint(
        1,
        100
    )

    tenure = random.randint(
        1,
        10
    )

    visits = random.randint(
        1,
        50
    )

    purchase_frequency = random.randint(
        1,
        30
    )

    churn = random.choice(
        [0,1]
    )

    data.append({

        "customer_id":i,
        "name":fake.name(),
        "age":age,
        "gender":random.choice(
            ["Male","Female"]
        ),
        "city":random.choice(
            cities
        ),
        "income":income,
        "spending_score":spending_score,
        "tenure":tenure,
        "monthly_visits":visits,
        "favorite_product":random.choice(
            products
        ),
        "favorite_category":random.choice(
            categories
        ),
        "purchase_frequency":purchase_frequency,
        "churn":churn

    })

df = pd.DataFrame(data)

df.to_csv(
    "data/customers.csv",
    index=False
)

print(
    "Dataset Created Successfully"
)