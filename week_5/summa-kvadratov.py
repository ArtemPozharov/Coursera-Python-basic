"""
    По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

    Формат ввода
    Вводится натуральное число.

"""

n = int(input())
x = 0

for i in range(n + 1):
    x += i ** 2

print(x)
