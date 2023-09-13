from flask import Flask, render_template, abort

app = Flask(__name__)
projects = [
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
        "name": "User-Email-Feedback application",
        "thumb": "img/email.png",
        "hero": "img/email.png",
        "categories": ["Javascript", "react", "nodejs"],
        "slug": "email-feedback",
        "gh": "https://github.com/TaTehun/User-Email-Feedback"
    },
    {
        "name": "Social-Media-platform",
        "thumb": "img/social.png",
        "hero": "img/social.png",
        "categories": ["Typescript", "React", "NodeJS"],
        "slug": "social-media",
        "gh": "https://github.com/TaTehun/SocialMedia"
    }
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