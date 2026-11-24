
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


def get_quote():
    """Fetch a random Kanye West quote."""
    try:
        response = requests.get(
            "https://api.kanye.rest/",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        return data.get("quote", "No quote available.")

    except requests.RequestException:
        return "Unable to fetch a quote. Please try again."


@app.route("/")
def home():
    quote = get_quote()
    return render_template("index.html", quote=quote)


@app.route("/api/quote")
def new_quote():
    quote = get_quote()
    return jsonify({"quote": quote})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
