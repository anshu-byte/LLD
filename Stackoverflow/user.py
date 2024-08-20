from tag import Tag
from typing import List
from question import Question
from comment import Comment
from answer import Answer


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []

    def ask_question(self, title, content: str, tags: List[Tag]):
        question = Question(self, title, content, tags)
        self.questions.append(question)
        self.update_reputation(5)  # Gain 5 reputation for asking a question

    def answer_question(self, question: Question, content: str):
        answer = Answer(self, question, content)
        question.add_answer(answer)
        self.answers.append(answer)
        self.update_reputation(10)  # Gain 10 reputation to answer

    def add_comment(self, content: str):
        comment = Comment(self, content)
        self.comments.append(comment)

    def delete_comment(self, comment: Comment):
        self.comments.remove(comment)

    def update_reputation(self, value: int):
        self.reputation += value
