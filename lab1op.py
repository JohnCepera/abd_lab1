import math


class Angle:
    def __init__(self, radians):
        self._radians = radians

    # Создание угла в радианах
    @classmethod
    def from_radians(cls, radians):
        return cls(radians)

    # Создание угла в градусах
    @classmethod
    def from_degrees(cls, degrees):
        return cls(math.radians(degrees))

    # Получить угол в радианах
    def get_radians(self):
        return self._radians

    # Получить угол в градусах
    def get_degrees(self):
        return math.degrees(self._radians)

    # Установить угол в радианах
    def set_radians(self, radians):
        self._radians = radians

    # Установить угол в градусах
    def set_degrees(self, degrees):
        self._radians = math.radians(degrees)

    # Привести угол к одному периоду [0, 2π)
    def normalized(self):
        return self._radians % (2 * math.pi)

    # Строковое представление
    def __str__(self):
        return f"{self.get_degrees()}°"

    def __repr__(self):
        return f"Angle({self._radians})"

    # Сравнение
    def __eq__(self, other):
        if not isinstance(other, Angle):
            return False

        return math.isclose(
            self.normalized(),
            other.normalized()
        )

    def __lt__(self, other):
        return self.normalized() < other.normalized()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    # Преобразование в float
    def __float__(self):
        return float(self._radians)

    # Преобразование в int
    def __int__(self):
        return int(self._radians)

    # Сложение
    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self._radians + other._radians)

        if isinstance(other, (int, float)):
            return Angle(self._radians + other)

        return NotImplemented

    # Вычитание
    def __sub__(self, other):
        if isinstance(other, Angle):
            return Angle(self._radians - other._radians)

        if isinstance(other, (int, float)):
            return Angle(self._radians - other)

        return NotImplemented

    # Умножение на число
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Angle(self._radians * other)

        return NotImplemented

    # Деление на число
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Angle(self._radians / other)

        return NotImplemented


# Демонстрация работы

a = Angle.from_degrees(90)
b = Angle.from_radians(math.pi)

print("a =", a)
print("b =", b)

print("a в радианах:", a.get_radians())
print("a в градусах:", a.get_degrees())

a.set_degrees(180)
print("После изменения:", a)

x = Angle.from_degrees(0)
y = Angle.from_degrees(360)

print("0° == 360°:", x == y)

c = Angle.from_degrees(30)
d = Angle.from_degrees(60)

print("30° + 60° =", c + d)
print("60° - 30° =", d - c)
print("30° * 2 =", c * 2)
print("60° / 2 =", d / 2)

print("float(a) =", float(a))
print("int(a) =", int(a))