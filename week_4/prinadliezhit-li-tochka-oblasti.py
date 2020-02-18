"""
    Проверьте, принадлежит ли точка данной закрашенной области:

    https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/
    CRrK-gpYEeeYfApVbTauLA_0f17268b488eb5a67146fbb1207d0da0_3795.png?expiry=
    1581897600000&hmac=PUhReOfMRItCJUv_jQE52aDr58Nx0j9WXiyarcOmVro

    Если точка принадлежит области (область включает границы),
    выведите слово YES, иначе выведите слово NO.
    Решение должно содержать функцию IsPointInArea(x, y),
    возвращающую True, если точка принадлежит области и False,
    если не принадлежит. Основная программа должна считать координаты точки,
    вызвать функцию IsPointInArea и в зависимости от возвращенного значения
    вывести на экран необходимое сообщение. Функция IsPointInArea не должна
    содержать инструкцию if.

    Формат ввода
    Вводится два действительных числа.

    Формат вывода
    Выведите ответ на задачу.

    Замечание:
    В задаче подразумевается, что нижняя область продолжается вниз бесконечно
    (картинка может ввести в заблуждение, как будто область заканчивается на
    y = -3.5). Т.е. например для ввода

    0
    -5

    ответ должен быть YES.

"""


def is_point_in_are(x, y):
    v1 = ((x + 1) ** 2 + (y - 1) ** 2) <= 4
    v2 = y >= - x
    v3 = y >= 2 * x + 2
    v4 = ((x + 1) ** 2 + (y - 1) ** 2) >= 4
    v5 = y <= - x
    v6 = y <= 2 * x + 2
    return (v1 and v2 and v3) or (v4 and v5 and v6)


a = float(input())
b = float(input())

if is_point_in_are(a, b):
    print('YES')
else:
    print('NO')