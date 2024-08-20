from stackoverflow import Stackoverflow


class StackoverflowDemo:

    @staticmethod
    def run():
        system = Stackoverflow()

        # create users
        alice = system.create_user("Alice", "alice@gmail.com")
        bob = system.create_user("Bob", "bob@gmail.com")
        system.delete_user("ram")

        # Alice asks a question
        python_question = system.ask_question(
            alice, "What is polymorphism?", ["python", "oop"]
        )

        # Bob answers the question
        system.answer_question(bob, python_question, "Polymorphism is cool!")


if __name__ == "__main__":
    StackoverflowDemo.run()
