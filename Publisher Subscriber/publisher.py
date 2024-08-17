from topic import Topic
from subscriber import Subscriber


class Publisher:
    def __init__(self, name):
        self.name = name

    def send_message(self, topic: Topic, subscriber: Subscriber, message: str):
        topic.add_message(message, subscriber)
