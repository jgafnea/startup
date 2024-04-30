import requests
from faker import Faker
from flask import Flask, render_template

app = Flask(__name__)
fake = Faker()


def get_bs() -> tuple:
    first, second = [fake.bs() for _ in range(2)]
    return first, second


def get_tt() -> tuple:
    resp = requests.get("https://itsthisforthat.com/api.php?json").json()
    this, that = resp.values()
    return this, that


@app.route("/")
def get_index() -> str:
    first, second = get_bs()
    this, that = get_tt()

    statement = f"{first.title()} and {second.title()}"
    basically = f"Basically it's {this} for {that}"

    return render_template("index.html", statement=statement, basically=basically)


if __name__ == "__main__":
    app.run()
