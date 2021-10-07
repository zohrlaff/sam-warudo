from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def main():
    year = datetime.datetime.today().year
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=True)
