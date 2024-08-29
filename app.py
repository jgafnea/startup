import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_index() -> str:
    # Use Faker/Mocker API for header. Call twice and combine responses with "and".
    response = requests.get("https://api.mockster.dev/api/v1/companies").json()
    first, second = [response[i].get("buzzPhrase") for i in range(2)]
    header = f"{first.title()} and {second.title()}"

    # Use ITFT API for paragraph.
    response = requests.get("https://itsthisforthat.com/api.php?json").json()
    this, that = response.values()
    paragraph = f"Basically it's {this} for {that}"

    return render_template("index.html.j2", header=header, paragraph=paragraph)


if __name__ == "__main__":
    app.run()
