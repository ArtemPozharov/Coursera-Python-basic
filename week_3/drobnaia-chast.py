"""
    Дано положительное действительное число X. Выведите его дробную часть.

    Формат ввода
    Вводится положительное действительное число.

"""

n = float(input())

answer = round(n - int(n), 10)

print(answer)
