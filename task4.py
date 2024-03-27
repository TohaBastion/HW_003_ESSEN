"""task4"""


class Base:
    """Базовий клас"""
    @classmethod
    def method(cls):
        """Метод виводу"""
        print("Hello from Base")

class Child(Base):
    """Похідний клас"""
    @classmethod
    def method(cls):
        """Метод виводу"""
        print("Hello from Child")


Base.method()
Child.method()
