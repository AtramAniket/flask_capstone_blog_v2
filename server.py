from flask import Flask, render_template, request, redirect, url_for, flash
from post import Post
from contact import Contact
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

blog = Post()

# GET "/"
@app.route("/")
def home():
    date_today = dt.datetime.now().strftime("%b, %d %Y")
    posts = blog.posts
    return render_template("index.html", blog_posts = posts, author = "Aniket Atram", date = date_today)

# GET "/about"
@app.route("/about")
def about_me():
    return render_template("about.html")

# GET "/contact"
@app.route("/contact")
def contact_me():
    return render_template("contact.html")

# GET "/post/:id"
@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = blog.get_post_by_id(post_id)
    return render_template("post.html", blog_post = post[0])

# POST "/contact/send_contact_request"
@app.route("/conatct/send_contact_request", methods=['POST'])
def send_contact_request():
    sender_name = request.form["sender_name"]
    sender_address = request.form["sender_email"]
    message_content = request.form["sender_message"]

    contact_request = Contact(sender_name, sender_address, message_content)
    contact_request.send_message()
    flash("Your message has been sent successfully!")
    return redirect(url_for("contact_me"))

if __name__ == "__main__":
    app.run(debug = True)