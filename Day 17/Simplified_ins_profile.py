# use class to create objects that has
# Attribute: id, name, follower, following
# Method: follow
# This method will get input: an user name. increase "user2" follower one
#                                           and increase "user1" following one


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1, user_2 = User("001", "BRO"), User("002", "NOTBRO")
user_1.follow(user_2)
print(user_1.followers)