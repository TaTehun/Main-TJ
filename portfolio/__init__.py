from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)

projects = [
    {
        "name": "App Tester",
        "thumb": "img/automation.png",
        "hero": "img/automation.png",
        "categories": ["Python", "PyQt5", "Automation"],
        "slug": "app-tester",
        "gh": "https://github.com/TaTehun/3rd_apps/tree/main"
    },
    {
        "name": "Korean-Speaking Taxi Service",
        "thumb": "img/taxi.png",
        "hero": "img/taxi.png",
        "categories": ["Javascript", "React", "Node.js"],
        "slug": "korean-taxi",
        "prod": "https://familytaxidallas.com/",
        "gh": "https://github.com/TaTehun/Korean-Taxi-Web",
    },
    {
        "name": "User-Email-Feedback application",
        "thumb": "img/email.png",
        "hero": "img/email.png",
        "categories": ["Javascript", "React", "Node.js"],
        "slug": "email-feedback",
        "gh": "https://github.com/TaTehun/User-Email-Feedback"
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

# ✅ Serve demo videos from static/videos/
@app.route("/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename)
