from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/cpapers')
def cpapers():
    return render_template("cpapers.html")


@app.route('/cdemos')
def cdemos():
    return render_template("cdemos.html")


@app.route('/ctutorials')
def ctutorials():
    return render_template("ctutorials.html")


@app.route('/csessions')
def csessions():
    return render_template("csessions.html")


@app.route('/organization')
def organization():
    return render_template("organization.html")
