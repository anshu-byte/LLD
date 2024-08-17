from topic import Topic


class Subscriber:
    def __init__(self, name):
        self.name = name

    def get_message(self, topic: Topic):
        try:
            message = topic.get_message(self)
            print(f"{self.name} received message: {message}")
        except IndexError:
            print(f"{self.name} has no messages")
