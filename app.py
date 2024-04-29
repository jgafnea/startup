from faker import Faker
from flask import Flask

app = Flask(__name__)
fake = Faker()


def get_bs() -> tuple:
    first, second = [fake.bs() for _ in range(2)]
    return first, second


@app.route("/")
def get_index() -> str:
    first, second = get_bs()
    statement = f"{first.capitalize()} and {second}"
    return statement


if __name__ == "__main__":
    app.run()
