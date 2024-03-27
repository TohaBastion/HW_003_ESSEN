"""task2"""


class English:
    """Class English"""
    def greeting(self):
        """Greetings in English"""
        return "Hello, friend!"

class Spanish:
    """Class Spanish"""
    def greeting(self):
        """Greetings in Spanish"""
        return "Hola, amigo!"


def hello_friend(english_say, spanish_say):
    """Функція виводу"""
    print("English:", english_say.greeting())
    print("Spanish:", spanish_say.greeting())


english = English()
spanish = Spanish()

hello_friend(english, spanish)
