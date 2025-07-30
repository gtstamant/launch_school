import os
from flask import (Flask,
                   flash,
                   redirect,
                   render_template,
                   request,
                   send_from_directory,
                   session,
                   url_for,
)
from markdown import markdown
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret1"

def require_signed_in_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)

        flash("You must be signed in to do that.")
        return redirect(url_for("sign_in_page"))

    return wrapper

def get_data_path():
    dir_path = os.path.dirname(__file__)

    if app.config['TESTING']:
        return os.path.join(dir_path, "tests", "data")

    return os.path.join(dir_path, "cms", "data")

@app.route("/")
def index():
    data_dir = get_data_path()
    files = [os.path.basename(path) for path in os.listdir(data_dir)]

    return render_template("index.html", files=files)

@app.route("/<filename>")
def file_content(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    if not os.path.isfile(file_path):
        flash(f"{filename} does not exist")
        return redirect(url_for("index"))

    if filename.endswith(".md"):
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template("markdown.html", content=markdown(content))

    return send_from_directory(data_dir, filename)

@app.route("/<filename>/edit")
@require_signed_in_user
def edit_document(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template("edit.html",
                               filename=filename,
                               content=content)

    flash(f"{filename} does not exist")
    return redirect(url_for("index"))

@app.route("/<filename>", methods=["POST"])
@require_signed_in_user
def save_document(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    content = request.form['content']
    with open(file_path, 'w') as file:
        file.write(content)

    flash(f"{filename} has been updated")
    return redirect(url_for('index'))

@app.route("/new_document")
@require_signed_in_user
def new_document():
    return render_template("new_document.html")

@app.route("/create_document", methods=["POST"])
@require_signed_in_user
def create_document():
    filename = request.form.get('filename', '').strip()
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    if len(filename) == 0:
        flash("A name is required")
        return render_template("new_document.html"), 422

    if os.path.exists(file_path):
        flash(f"{filename} already exists")
        return render_template("new_document.html"), 422

    with open(file_path, "w") as file:
        file.write("")

    flash(f"{filename} has been created")
    return redirect(url_for("index"))

@app.route("/<filename>/delete", methods=["POST"])
@require_signed_in_user
def delete_document(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    os.remove(file_path)
    flash(f"{filename} has been deleted")
    return redirect(url_for("index"))

@app.route("/users/signin")
def sign_in_page():
    return render_template("sign_in.html")

@app.route("/users/signin", methods=["POST"])
def sign_in():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if username == 'admin' and password == 'secret':
        session['username'] = username
        flash("Welcome!")
        return redirect(url_for("index"))

    flash("Invalid credentials")
    return render_template("sign_in.html"), 422

@app.route("/users/signout", methods=["POST"])
def sign_out():
    session.pop('username', None)
    flash("You have been signed out.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5003)