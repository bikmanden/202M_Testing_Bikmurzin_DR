import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_triangle_creation_positive():
    triangle = Triangle(2, 2, 2)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 6

    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

    triangle = Triangle(5, 5, 6)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 16

def test_triangle_creation_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, -1, -1)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, -1, 1)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-2, 2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 2, -4)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 1, -1)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-2, -2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, -2, -4)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-4, -4, -7)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 2)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(5, 10, 16)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)

print(test_triangle_creation_positive())
print(test_triangle_creation_negative())