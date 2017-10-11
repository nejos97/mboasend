#pyUpload
---

it's a web applicationl with flask.
you can discover Upload, Weather and Todo module.
**What's the flask ?**

> **Flask** is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed.Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

**Setup**

For use this application lacally, yous should firstly have python installed to your cumputer. it's installed if using linux distributuion; for windows, you can find how to install it online.

After installing pyhton create a virtual environment.

```bash
cd /
mkdir pyUpload
python3 -m venv pyUpload --without-pip
```

for activate your venv

```bash
cd pyUpload
. bin/activate
```

All this step is already in repo. now you just clone it.

```bash
git clone https://github.com/nejos97/pyUpload.git
```

in our venv you should have installed all dependencies.

actviate your venv and install all dependencies with pip3

```
click==6.7
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
olefile==0.44
Werkzeug==0.12.2

```

now your locally repo is ready to launch but let's set some config.

open `app.py` with your text editor

```py
path = "/path/to/the/pyUpload/uploads"
```

set password to connect to default account

```py
if request.form['username']=="root" and request.form['password']=="toor" :
```

now all is set you can run application

```
cd pyUpload
pyhon3 app.py

#output exemple

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 758-570-599
```

open your browser and write `http://localhost:5000/`
