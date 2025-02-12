import cmath

def quadratic_equation(a, b, c):
    """Решает квадратное уравнение ax^2 + bx + c = 0 и возвращает корни в порядке возрастания.
       Обрабатывает случаи линейного уравнения, отсутствия решений.
    """
    if a == 0:
        if b == 0:
            return [] # Нет решений
        else:
            return [-c / b] # Линейное уравнение
    else:
        delta = (b**2) - 4*(a*c)
        if delta >= 0:
            x1 = (-b - delta**0.5) / (2 * a)
            x2 = (-b + delta**0.5) / (2 * a)
            # Округляем до нуля очень маленькую мнимую часть, если она есть
            x1 = x1.real if abs(x1.imag) < 1e-10 else x1
            x2 = x2.real if abs(x2.imag) < 1e-10 else x2
            return sorted([x1, x2])
        else:
            x1 = (-b - cmath.sqrt(delta)) / (2 * a)
            x2 = (-b + cmath.sqrt(delta)) / (2 * a)
            x1 = x1.real if abs(x1.imag) < 1e-10 else x1
            x2 = x2.real if abs(x2.imag) < 1e-10 else x2
            return sorted([x1, x2], key=abs)

print(quadratic_equation(1, 5, 6))