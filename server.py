from flask import Flask, flash, render_template, request, session, redirect, url_for
# from delta import Delta

app = Flask(__name__)

# app.config["SERVER_NAME"] = "colindaugherty.net:80"

# @app.route("/" subdomain="api")
# def api_dashboard():
# 	return "<h1 style='color:blue'>It worked yea boi</h1>"
#
# @app.route("/" subdomain="delta")
# def delta():
# 	return "<h1 style='color:blue'>Delta is gonna be here yea boi</h1>"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/social")
def social():
    return render_template('404.html')

@app.route("/projects/delta")
def projectsdelta():
	return redirect(url_for('delta'))

@app.route("/projects/spotify-music-app")
def spotifyMusicApp():
	return render_template('coming1_soon.html')

@app.route("/projects/security-camera")
def securityCam():
	return render_template('coming1_soon.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_overloaded(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
