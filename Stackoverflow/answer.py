from votable import Votable
from commentable import Commentable
from typing import List
from comment import Comment


class Answer(Votable, Commentable):
    def __init__(self, author, question, content: str):
        self.id = id(self)
        self.author = author
        self.question = question
        self.content = content
        self._votes = 0
        self._comments = []
        self._is_accepted = False

    def vote(self, user, value: int):
        if value not in [1, -1]:
            raise ValueError("Vote value must be either 1 or -1")
        elif user == self.author:
            raise ValueError("User can't upvote/downvote itself")
        self.votes += value
        self.author.update_reputation(value * 5)  # +5 for upvote -5 for downvote

    def get_vote_count(self):
        return self.votes

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self) -> List[Comment]:
        return self._comments

    def accept_answer(self):
        if self._is_accepted:
            raise ValueError("This answer is already accepted")
        self._is_accepted = True
        self.author.update_reputation(15)  # +15 for accepted answer

    def accepted(self) -> bool:
        return self._is_accepted
