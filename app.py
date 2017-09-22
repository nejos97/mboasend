import os,sys
from flask import Flask,render_template,request,redirect,url_for,flash,make_response,session,send_file
from werkzeug import secure_filename

app = Flask(__name__)
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
            nom = secure_filename(fichier.filename)
            fichier.save("./uploads/"+nom)
            flash("File uploaded with success")
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

@app.route("/about")
def about():
    pass

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

@app.errorhandler(404)
def error404(error):
    return render_template("404.html"),404

if __name__ == "__main__" :
    app.run(port=5000, debug=True)
