from flask import Flask, render_template, abort

app = Flask(__name__)
projects = [
    {
        "name": "Korean-Speaking Taxi Service Website",
        "thumb": "img/tj.png",
        "hero": "img/tj.png",
        "categories": ["python", "web"],
        "slug": "korean-taxi",
        "prod": "https://familytaxidallas.com/",
    },
    {
        "name": "Project2",
        "thumb": "img/tj.png",
        "hero": "img/tj.png",
        "categories": ["react", "javascript"],
        "slug": "2",
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