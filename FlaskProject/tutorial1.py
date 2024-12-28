from flask import Flask, render_template
app = Flask(__name__)

# End Point No. 1
@app.route("/")
def hello():
    return render_template("index.html")

# End Point No. 2
@app.route("/about")

def atif():
    name = "Atif Salam"
    return render_template("about.html", name_about = name)

# End Point No. 3
@app.route("/bootstrap")
def bootstrap():

    return render_template("bootstrap.html")

# app.run()
app.run(debug=True)