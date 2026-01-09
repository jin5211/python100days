class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticate_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticate_decorator
def create_post(user):
    print(f"This is a post created by {user.name}.")


user = User("Jin")
user.is_logged_in = True
create_post(user)
