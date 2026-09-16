import math


class Point3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __repr__(self):
        return f"Point3d(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"


class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    # Красивый вывод
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    # Представление объекта
    def __repr__(self):
        return (
            f"Vector3d(x={self.x:.2f}, "
            f"y={self.y:.2f}, "
            f"z={self.z:.2f})"
        )

    # Фабричный метод.
    # Создает вектор из двух точек: конец - начало
    @classmethod
    def from_points(cls, start: Point3d, end: Point3d):
        return cls(
            end.x - start.x,
            end.y - start.y,
            end.z - start.z
        )

    # Проверка, что справа находится вектор или число
    def _get_values(self, other):
        if isinstance(other, Vector3d):
            return other.x, other.y, other.z

        if isinstance(other, (int, float)):
            return other, other, other

        return NotImplemented

    # =========================
    # СРАВНЕНИЯ
    # =========================

    def __eq__(self, other):
        if isinstance(other, Vector3d):
            return (
                self.x == other.x
                and self.y == other.y
                and self.z == other.z
            )

        return False

    def __lt__(self, other):
        if isinstance(other, Vector3d):
            return len(self) < len(other)

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector3d):
            return len(self) > len(other)

        return NotImplemented

    # =========================
    # СЛОЖЕНИЕ
    # =========================

    def __add__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            self.x + x,
            self.y + y,
            self.z + z
        )

    def __radd__(self, other):
        return self + other

    # =========================
    # ВЫЧИТАНИЕ
    # =========================

    def __sub__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            self.x - x,
            self.y - y,
            self.z - z
        )

    def __rsub__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            x - self.x,
            y - self.y,
            z - self.z
        )

    # =========================
    # УМНОЖЕНИЕ
    # =========================

    def __mul__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            self.x * x,
            self.y * y,
            self.z * z
        )

    def __rmul__(self, other):
        return self * other

    # =========================
    # ДЕЛЕНИЕ
    # =========================

    def __truediv__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            self.x / x,
            self.y / y,
            self.z / z
        )

    def __rtruediv__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        return Vector3d(
            x / self.x,
            y / self.y,
            z / self.z
        )

    # =========================
    # ИНКРЕМЕНТАЛЬНЫЕ ОПЕРАЦИИ
    # =========================

    def __iadd__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        self.x += x
        self.y += y
        self.z += z

        return self

    def __isub__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        self.x -= x
        self.y -= y
        self.z -= z

        return self

    def __imul__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        self.x *= x
        self.y *= y
        self.z *= z

        return self

    def __itruediv__(self, other):
        values = self._get_values(other)

        if values is NotImplemented:
            return NotImplemented

        x, y, z = values

        self.x /= x
        self.y /= y
        self.z /= z

        return self

    # =========================
    # ВЕКТОРНОЕ ПРОИЗВЕДЕНИЕ
    # =========================

    def __matmul__(self, other):
        if not isinstance(other, Vector3d):
            return NotImplemented

        return Vector3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # =========================
    # ДЛИНА ВЕКТОРА
    # =========================

    def __len__(self):
        return int(
            math.sqrt(
                self.x ** 2 +
                self.y ** 2 +
                self.z ** 2
            )
        )

    # =========================
    # ДОСТУП ПО ИНДЕКСУ И ИМЕНИ
    # =========================

    def __getitem__(self, key):
        if key == 0 or key == "x":
            return self.x

        if key == 1 or key == "y":
            return self.y

        if key == 2 or key == "z":
            return self.z

        raise KeyError("Допустимые значения: 0, 1, 2, 'x', 'y', 'z'")

    # =========================
    # ПЕРЕБОР FOR
    # =========================

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    # =========================
    # СТАТИЧЕСКИЕ МЕТОДЫ
    # =========================

    @staticmethod
    def is_collinear(a, b):
        if not isinstance(a, Vector3d) or not isinstance(b, Vector3d):
            return False

        result = a @ b

        return (
            result.x == 0
            and result.y == 0
            and result.z == 0
        )

    @staticmethod
    def is_complanar(a, b, c):
        if (
            not isinstance(a, Vector3d)
            or not isinstance(b, Vector3d)
            or not isinstance(c, Vector3d)
        ):
            return False

        # Смешанное произведение:
        # (a x b) . c

        cross = a @ b

        result = (
            cross.x * c.x
            + cross.y * c.y
            + cross.z * c.z
        )

        return result == 0


# ============================================================
# ДЕМОНСТРАЦИЯ РАБОТЫ
# ============================================================

print("========== POINT3D ==========")

p1 = Point3d(1, 2, 3)
p2 = Point3d(4, 6, 8)

print(p1)
print(repr(p1))


print("\n========== VECTOR3D ==========")

a = Vector3d(3, 4, 5)
b = Vector3d(1, 2, 3)

print("a =", a)
print("repr(a) =", repr(a))


print("\n========== FROM_POINTS ==========")

v = Vector3d.from_points(p1, p2)

print("Вектор из p1 в p2:", v)


print("\n========== СРАВНЕНИЯ ==========")

print("a == b:", a == b)
print("a < b:", a < b)
print("a > b:", a > b)


print("\n========== АРИФМЕТИКА ==========")

print("a + b =", a + b)
print("a + 3 =", a + 3)
print("3 + a =", 3 + a)

print("a - b =", a - b)
print("a - 3 =", a - 3)
print("3 - a =", 3 - a)

print("a * b =", a * b)
print("a * 3 =", a * 3)
print("3 * a =", 3 * a)

print("a / b =", a / b)
print("a / 2 =", a / 2)
print("2 / a =", 2 / a)


print("\n========== ИНКРЕМЕНТАЛЬНЫЕ ==========")

c = Vector3d(1, 2, 3)

print("c =", c)

c += 2
print("c += 2 ->", c)

c -= 1
print("c -= 1 ->", c)

c *= 2
print("c *= 2 ->", c)

c /= 2
print("c /= 2 ->", c)


print("\n========== ВЕКТОРНОЕ ПРОИЗВЕДЕНИЕ ==========")

print("a @ b =", a @ b)


print("\n========== ДЛИНА ==========")

print("len(a) =", len(a))


print("\n========== ИНДЕКСЫ ==========")

print("a[0] =", a[0])
print("a[1] =", a[1])
print("a[2] =", a[2])

print("a['x'] =", a["x"])
print("a['y'] =", a["y"])
print("a['z'] =", a["z"])


print("\n========== FOR ==========")

for component in a:
    print(component)


print("\n========== КОЛЛИНЕАРНОСТЬ ==========")

v1 = Vector3d(1, 2, 3)
v2 = Vector3d(2, 4, 6)
v3 = Vector3d(1, 0, 0)

print("v1 и v2:", Vector3d.is_collinear(v1, v2))
print("v1 и v3:", Vector3d.is_collinear(v1, v3))


print("\n========== КОМПЛАНАРНОСТЬ ==========")

v4 = Vector3d(1, 0, 0)
v5 = Vector3d(0, 1, 0)
v6 = Vector3d(1, 1, 0)

print(
    "v4, v5, v6:",
    Vector3d.is_complanar(v4, v5, v6)
)
