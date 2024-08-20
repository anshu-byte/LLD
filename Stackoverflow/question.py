from datetime import datetime
from typing import List
from tag import Tag
from comment import Comment
from answer import Answer


class Question:
    def __init__(self, author, title: str, content: str, tags: List[Tag]):
        self.id = id(self)
        self.title = title
        self.content = content
        self.author = author
        self.tags = [Tag(name) for name in tags]
        self.answers = []
        self.comments = []
        self.votes = 0
        self.creation_date = datetime.now()

    def add_answer(self, answer: Answer):
        self.answers.append(answer)

    def vote(self, user, value: int):
        if value not in [1, -1]:
            raise ValueError("Vote value must be either 1 or -1")
        elif user == self.author:
            raise ValueError("User can't upvote/downvote itself")
        self.votes += value
        self.author.update_reputation(value * 5)  # +5 for upvote -5 for downvote

    def get_vote_count(self):
        return self.votes

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self) -> List[Comment]:
        return self.comments.copy()
