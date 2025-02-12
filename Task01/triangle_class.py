class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


class Triangle:
    def __init__(self, a, b, c):
        """
        Конструктор класса Triangle.

        Args:
            a: Длина первой стороны.
            b: Длина второй стороны.
            c: Длина третьей стороны.

        Raises:
            IncorrectTriangleSides: Если стороны не образуют треугольник.
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            raise IncorrectTriangleSides("Стороны треугольника должны быть числами.")
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Стороны треугольника должны быть положительными числами.")
        if not (a + b > c and a + c > b and b + c > a):
            raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника.")

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        """
        Определяет и возвращает тип треугольника.

        Returns:
            str: Тип треугольника ("nonequilateral", "isosceles", "equilateral").
        """
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        """
        Вычисляет и возвращает периметр треугольника.

        Returns:
            float: Периметр треугольника.
        """
        return self.a + self.b + self.c


"""
# Примеры использования
try:
    triangle1 = Triangle(3, 4, 5)
    print(f"Тип треугольника: {triangle1.triangle_type()}")  # nonequilateral
    print(f"Периметр треугольника: {triangle1.perimeter()}")  # 12

    triangle2 = Triangle(5, 5, 5)
    print(f"Тип треугольника: {triangle2.triangle_type()}")  # equilateral
    print(f"Периметр треугольника: {triangle2.perimeter()}")  # 15

    triangle3 = Triangle(2, 2, 3)
    print(f"Тип треугольника: {triangle3.triangle_type()}")  # isosceles
    print(f"Периметр треугольника: {triangle3.perimeter()}")  # 7

    triangle4 = Triangle(1, 1, 3) #  Вызовет исключение
    print(f"Тип треугольника: {triangle4.triangle_type()}")
except IncorrectTriangleSides as e:
    print(f"Ошибка: {e}")

except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
    """