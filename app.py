from flask import Flask, render_template
from flask_flatpages import FlatPages


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


@app.route("/blog/")
def blog():
    return render_template("blog.html", pages=pages)


@app.errorhandler(404)
def page_not_found(path):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
