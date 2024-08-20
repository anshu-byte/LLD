from abc import ABC, abstractmethod


class Commentable(ABC):

    @abstractmethod
    def add_comment(self, content):
        pass

    @abstractmethod
    def get_comments(self):
        pass
