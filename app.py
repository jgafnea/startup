import requests
from faker import Faker
from flask import Flask, render_template

app = Flask(__name__)
fake = Faker()


@app.route("/")
def get_index() -> str:
    # Use Faker for header
    first, second = [fake.bs() for _ in range(2)]
    header = f"{first.title()} and {second.title()}"

    # Use API for paragraph
    response = requests.get("https://itsthisforthat.com/api.php?json").json()
    this, that = response.values()
    paragraph = f"Basically it's {this} for {that}"

    return render_template("index.html.j2", header=header, paragraph=paragraph)


if __name__ == "__main__":
    app.run()
