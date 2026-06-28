from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

history = []
clicks = {}

url_mapping = {}

@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None

    if request.method == "POST":

        original_url = request.form["url"]

        short_code = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )

        url_mapping[short_code] = original_url

        clicks[short_code] = 0

        short_url = f"http://127.0.0.1:5000/{short_code}"

        history.append({
            "original": original_url,
            "short": short_url,
             "clicks": clicks[short_code]
     })

    return render_template(
        "index.html",
        short_url=short_url,
        history=history
    )


@app.route("/<short_code>")
def redirect_url(short_code):

    if short_code in url_mapping:

        clicks[short_code] += 1

        return redirect(
            url_mapping[short_code]
        )

    return "URL not found!"


if __name__ == "__main__":
    app.run(debug=True)