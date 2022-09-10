from flask import Flask, render_template
from post import Post

app = Flask(__name__)

URL = "https://api.npoint.io/c790b4d5cab58020d391"

post = Post(blog_url=URL)


@app.route('/')
def home():
    all_posts = post.blogs
    return render_template(
        "index.html",
        blog_posts=all_posts,
    )


@app.route('/blog/<int:num>')
def get_blog(num):
    blog = post.get_blog_by_id(num)
    print(blog)
    return render_template(
        "post.html",
        blog=blog,
    )


if __name__ == "__main__":
    app.run(debug=True)


# about this project
# it is simpler than it sounds.
# Just render "index.html" with "all_posts"
# And render "post.html" with blog
# The html will do their jobs, then we will be fine
