"""task3"""


class Temperature:
    """Клас описуючий температуору"""
    def __init__(self, celsius=None, fahrenheit=None):
        self._celsius = celsius
        self._fahrenheit = fahrenheit

    @property
    def celsius(self):
        """функція запиту цельсію"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """функція змін цельсію"""
        self._celsius = value
        self._fahrenheit = value * 9/5 + 32

    @property
    def fahrenheit(self):
        """функція запиту фаренгейту"""
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        """функція змін фаренгейту"""
        self._fahrenheit = value
        self._celsius = (value - 32) * 5/9


    def __str__(self):
        """Функція виводу інформації"""
        return (f'Температура за Цельсієм = {self.celsius:}. '
                f'Температура за Фарегейтом = {self.fahrenheit:}')


temp = Temperature()
temp.celsius = 25
print("Температура в градусах Фаренгейта:", temp.fahrenheit)
print("Температура в градусах Цельсія:", temp.celsius)
print(temp)
