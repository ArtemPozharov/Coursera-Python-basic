"""
    Дано натуральное число n>1. Выведите его наименьший делитель,
    отличный от 1. Решение оформите в виде функции MinDivisor(n).
    Алгоритм должен иметь сложность порядка корня квадратного из n.

    Указание. Если у числа n нет делителя не превосходящего корня из n,
    то число n — простое и ответом будет само число n.
    А у всех составных чисел обязательно есть делители,
    отличные от единицы и не превосходящие корня из n.

"""


def min_divisor(n):
    import math
    divisor = 2
    while n % divisor:
        if divisor >= math.sqrt(n):
            return n
        divisor += 1
    return divisor


result = min_divisor(int(input()))
print(result)