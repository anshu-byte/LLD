from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


class PublisherSubscriberDemo:

    @staticmethod
    def run():
        publisher1 = Publisher("Publisher 1")
        subscriber1 = Subscriber("Subscriber 1")
        topic1 = Topic("Topic 1")
        topic1.add_subscriber(subscriber1)
        publisher1.send_message(topic1, subscriber1, "Hello World!")
        publisher1.send_message(topic1, subscriber1, "No problem")
        subscriber1.get_message(topic1)
        subscriber1.get_message(topic1)
        subscriber1.get_message(topic1)

        subscriber2 = Subscriber("Subscriber 2")
        topic2 = Topic("Topic 2")
        topic2.add_subscriber(subscriber2)
        publisher1.send_message(topic2, subscriber2, "Hey there!")
        subscriber2.get_message(topic2)


if __name__ == "__main__":
    PublisherSubscriberDemo.run()
