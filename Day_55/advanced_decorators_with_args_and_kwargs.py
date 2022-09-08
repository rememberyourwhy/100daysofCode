class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# def is_authenticated_decorator(function):
#     def wrapper(user: User):
#         if user.is_logged_in:
#             function()
#     return wrapper

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        return wrapper


def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("pt")
new_user.is_logged_in = True
create_blog_post(new_user)
