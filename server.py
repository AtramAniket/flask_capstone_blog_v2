from flask import Flask, render_template
from post import Post
import datetime as dt


app = Flask(__name__)

blog = Post()

# "/"
@app.route("/")
def home():
    date_today = dt.datetime.now().strftime("%b, %d %Y")
    posts = blog.get_all_blog_posts()
    return render_template("index.html", blog_posts = posts, author = "Aniket Atram", date = date_today)

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