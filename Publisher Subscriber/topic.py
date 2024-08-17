from collections import deque


class Topic:
    def __init__(self, name):
        self._name = name
        self._map = {}

    def add_subscriber(self, subscriber):
        self._map[subscriber] = deque([])

    def remove_subscriber(self, subscriber):
        self._map.pop(subscriber)

    def add_message(self, message, subscriber):
        self._map[subscriber].append(message)

    def get_message(self, subscriber):
        return self._map[subscriber].popleft()
