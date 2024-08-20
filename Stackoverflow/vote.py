from user import User


class Vote:
    def __init__(self, author: User, value: int):
        self.id = id(self)
        self.author = author
        self.value = value
