import requests


class Post:
    def __init__(self, blog_url):
        self.blog_url = blog_url
        self.blogs = None
        self.get_data()

    def get_data(self):
        response = requests.get(self.blog_url)
        self.blogs = response.json()

    def get_blog_by_id(self, blog_id):
        for blog in self.blogs:
            if blog["id"] == blog_id:
                return blog


# What does this class do?
# so we want to get hold of the json data just by passing
#   blog_url to this class init function
#   what we have in this class is an attribute contain blog value
#   a function that take id and return blog_post that has that id

