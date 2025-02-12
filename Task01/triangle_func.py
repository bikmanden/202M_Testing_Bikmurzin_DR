class IncorrectTriangleSides(Exception):
    """Исключение для некорректных длин сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам его сторон.

    Args:
        a: Длина первой стороны.
        b: Длина второй стороны.
        c: Длина третьей стороны.

    Returns:
        Строка, описывающая тип треугольника: "nonequilateral", "isosceles", "equilateral".

    Raises:
        IncorrectTriangleSides: Если длины сторон некорректны (не образуют треугольник).
    """

    """
    >>> get_triangle_type(2, 2, 2)
    'equilateral'
    >>> get_triangle_type(2, 3, 4)
    'nonequilateral'
    >>> get_triangle_type(2, 2, 3)
    'isosceles'
    >>> get_triangle_type(1, 2, 5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    >>> get_triangle_type(-1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    """

    # Проверка на корректность длин сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Длины сторон должны быть положительными числами.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Треугольник с такими сторонами не существует.")

    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"

"""
# Примеры использования
try:
    print(get_triangle_type(5, 5, 5))  # equilateral
    print(get_triangle_type(3, 4, 5))  # nonequilateral
    print(get_triangle_type(2, 2, 3))  # isosceles
    print(get_triangle_type(1, 1, 1)) # equilateral
    print(get_triangle_type(-1, 2, 3)) # IncorrectTriangleSides
    print(get_triangle_type(1, 2, 5)) # IncorrectTriangleSides
except IncorrectTriangleSides as e:
    print(f"Ошибка: {e}")
    """