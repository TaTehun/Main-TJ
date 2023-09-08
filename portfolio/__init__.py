from flask import Flask, render_template, abort

app = Flask(__name__)
projects = [
    {
        "name": "Project1",
        "thumb": "img/tj.png",
        "hero": "img/tj.png",
        "categories": ["Python", "Flask"],
        "slug": "movie-watchlist",
    },
    {
        "name": "Korean-Speaking Taxi Service",
        "thumb": "img/taxi.png",
        "hero": "img/taxi.png",
        "categories": ["Javascript", "react", "nodejs"],
        "slug": "korean-taxi",
        "prod": "https://familytaxidallas.com/",
        "gh": "https://github.com/TaTehun/Korean-Taxi-Web",
    },
    {
        "name": "Project3",
        "thumb": "img/tj.png",
        "hero": "img/tj.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404