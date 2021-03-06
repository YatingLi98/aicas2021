from flask import Flask, render_template, redirect, send_from_directory
import os
app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/index")


@app.route("/index")
def index_dup():
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


@app.route('/registration')
def registration():
    return render_template("registration.html")


@app.route('/authorInfo')
def authorInfo():
    return render_template("authorInfo.html")


@app.route('/programSchedule')
def programSchedule():
    return render_template("program_schedule.html")


@app.route('/keynoteSpeakers')
def keynoteSpeakers():
    return render_template("keynote_speakers.html")


@app.route('/tutorials')
def tutorials():
    return render_template("tutorials.html")


@app.route("/pdf/<path:path>")
def send_pdf(path):
    if os.path.exists(os.path.join("static/pdf", path)):
        return send_from_directory("static/pdf", path)
    return redirect("/index")
