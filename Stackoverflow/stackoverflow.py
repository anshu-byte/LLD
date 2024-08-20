from user import User
from typing import Dict
from question import Question
from answer import Answer
from tag import Tag
from typing import List


class Stackoverflow:
    def __init__(self):
        self._users: Dict[str, User] = {}
        self._questions: Dict[str, User] = {}
        self._answers: Dict[str, User] = {}
        self._tags: Dict[str, Tag] = {}

    def create_user(self, username: str, email: str):
        user = User(username, email)
        self._users[username] = user
        return user

    def delete_user(self, username: str):
        try:
            self._users.pop(username)
        except KeyError:
            print(f"{username} doesn't exist")

    def ask_question(self, author: User, title: str, content: str, tags: List[Tag]):
        question = author.ask_question(title, content, tags)
        self._questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question

    def answer_question(self, author: User, question: Question, content: str):
        answer = Answer(author, question, content)
        return answer

    def accept_answer(self, answer: Answer):
        answer.accept_answer()

    def search_questions(self, query):
        pass

    def get_user(self, user_id):
        pass

    def get_question_by_user(self, user_id):
        pass

    def get_answer(self, question):
        return self.answers.get()

    def get_tag(self, name: str):
        return self.tags.get(name)
