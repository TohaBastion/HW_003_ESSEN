"""task1"""


class Car:
    """Клас що описує авто"""

    def __init__(self, brand, model, year):
        """Ініціалізація"""
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def engineer_param(cls, software, controller, alarm_system):
        """Передача додаткових параметрів"""
        cls.__software = software
        cls.__controller = controller
        cls.__alarm_system = alarm_system

    def get_software(self):
        """get for software"""
        return self.__software

    def set_software(self, value):
        """set for software"""
        self.__software = value

    def get_controller(self):
        """get for controller"""
        return self.__controller

    def set_controller(self, value):
        """set for controller"""
        self.__controller = value

    def get_alarm_system(self):
        """get for alarm"""
        return self.__alarm_system

    def set_alarm_system(self, value):
        """set for alarm"""
        self.__alarm_system = value


car1 = Car("Toyota", "Camry", 2020)
car1.engineer_param('TPS-23223', '50 2011-8966106K64', 'REX')
print(car1.get_software())
print(car1.get_alarm_system())
car1.set_alarm_system('TXR1')
print(car1.get_alarm_system())
