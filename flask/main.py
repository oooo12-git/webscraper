from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/search")
def hello():
    return render_template("search.html")


app.run(debug=True)
