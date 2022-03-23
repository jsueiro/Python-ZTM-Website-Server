from flask import Flask, render_template
app = Flask(__name__)


# any time it requests endpoint, run hello_world
# root route
# http://127.0.0.1:5000/bob/2123
@app.route("/<username>/<int:post_id>")  # decorator
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/blog")  # decorator
def blog():
    return "<p>This is a blog.</p>"


@app.route("/about")  # decorator
def blog2():
    return render_template('about.html')
