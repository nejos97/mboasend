from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import make_response
from UrlClass import URL
from werkzeug import generate_password_hash
import pickle

app = Flask(__name__)
app.secret_key = "Hello"

@app.route("/", methods=['GET','POST'])
def todo():
    if not request.cookies.get("auth"):
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

@app.route("/login",methods=['GET','POST'])
def login():
    error = None
    if request.cookies.get("auth"):
        flash("You are already logged in")
        return redirect(url_for("todo"))
    if request.method == 'POST':
        if request.form['username']=="m" and request.form['password']=="m" :
            resp = make_response(redirect(url_for("todo")))
            resp.set_cookie("auth","0")
            return resp
        else :
            error = "username or password is invalide"
    return render_template("login.html",title="Login", error=error)

@app.route("/logout/")
def logout():
    flash("You were successfully logged out")
    resp = make_response(redirect(url_for("login")))
    resp.set_cookie("auth","",expires=0)
    return resp

@app.errorhandler(404)
def error404(error):
    return render_template("404.html"),404

if __name__ == "__main__" :
    app.run(port=5000, debug=True)
