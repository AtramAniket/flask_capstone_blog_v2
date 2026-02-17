from flask import Flask, render_template


app = Flask(__name__)

# "/"
@app.route("/")
def home():
    return render_template("index.html")

# "/about"
@app.route("/about")
def about_me():
    return render_template("about.html")

# "/contact"
@app.route("/contact")
def contact_me():
    return render_template("contact.html")

# "/post"
@app.route("/post")
def sample_post():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug = True)