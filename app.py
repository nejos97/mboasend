import os,sys
from flask import Flask,render_template,request,redirect,url_for,flash,make_response,session,send_file
from werkzeug import secure_filename
import hashlib
from weather_location import *
import json

app = Flask(__name__)
app.jinja_env.globals.update(get_icon=get_icon)
app.jinja_env.globals.update(get_date=get_date) 
app.secret_key = "Hello"
app.config['PERMANENT_SESSION_LIFETIME'] = 3600*24*30
path = "/home/nejos97/PycharmProjects/pyUpload/uploads"

@app.route("/")
def index():
    return render_template("index.html",title="Home")


@app.route("/todo/", methods=['GET','POST'])
def todo():
    if not "auth" in session :
        flash("Please login firstly")
        return redirect(url_for("login"))
    t=[]
    with open("donnee.dat","r") as f :
        t = f.readlines()
    if request.method == "POST" and len(request.form['item'])>0 :
        data = request.form['item']
        with open("donnee.dat","a") as f:
            t.append(data)
            f.write("{}\n".format(data))
    t.reverse()
    return render_template("todo.html", title="Todo list", todo = t)

@app.route("/upload", methods=["GET","POST"])
def upload():
    if not "auth" in session:
        flash("Please login firstly")
        return make_response(redirect(url_for("login")))

    if request.method == "POST" :
        fichier = request.files["fichier"]
        if fichier and not fichier.filename == '':
            ext = fichier.filename.split('.')[-1]
            if ext.lower() in ["png","jpg","jpeg","gif",""]:
                nom = secure_filename(fichier.filename)
                fichier.save("./uploads/"+nom)
                flash("File uploaded with success")
            else :
                flash("Extension is not allowed. Please choose another file")
                redirect(request.url)
        else:
            flash("File input is empty or is deleted")
            redirect(request.url)

    liste = os.listdir("uploads")
    tmp = {}
    for e in liste :
        if os.path.isfile("uploads/"+e):
            tmp[e] = path+"/"+e
    return render_template("uploads.html",title="Uploads", fichiers = tmp)

@app.route("/download/<p>")
def download(p):
    chemin = path+"/"+p
    return send_file(chemin)

@app.route("/hashing", methods=["GET","POST"])
def hashing():
    r = {}
    if request.method == "POST":
        text = request.form["texte"].encode()
        r["text"] = text.decode()
        r["md5"] = hashlib.md5(text).hexdigest()
        r["sha1"] = hashlib.sha1(text).hexdigest()
        r["sha512"] = hashlib.sha512(text).hexdigest()
        flash("hashing result")
    return render_template("hashing.html",title="Test de hashage", result=r)

@app.route("/about")
def about():
    return "nejos97"

@app.route("/login/",methods=['GET','POST'])
def login():
    error = None
    if "auth" in session :
        flash("You are already logged in")
        return redirect(url_for("index"))
    if request.method == 'POST':
        if request.form['username']=="m" and request.form['password']=="m" :
            session["auth"] = True
            return redirect(url_for("index"))
        else :
            error = "username or password is invalide"
    return render_template("login.html",title="Login", error=error)

@app.route("/logout/")
def logout():
    if "auth" in session :
        flash("You were successfully logout")
        session.pop("auth",None)
    return redirect(url_for("login"))

@app.route("/weather/")
def weather():
    if not "auth" in session :
        flash("Please login firstly")
        return make_response(redirect(url_for("login")))
    d = get_coordonates()
    data = json.loads(d)
    meteo = json.loads(get_weather(data["lon"],data["lat"]))
    return render_template("weather.html",title="Weather of your location", ip=json.loads(d), meteo=meteo)

@app.errorhandler(404)
def error404(error):
    return render_template("404.html"),404

if __name__ == "__main__" :
    app.run(port=5000, debug=True)
