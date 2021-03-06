"""
    Даны два целочисленных списка A и B, упорядоченных по неубыванию.
    Объедините их в один упорядоченный список С (то есть он должен содержать
    len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B),
    возвращающей новый список.
    Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные
    списки запрещается. Использовать функцию sorted и метод sort запрещается.

    Формат ввода
    Программа получает на вход два неубывающих списка, каждый в отдельной
    строке.

    Формат вывода
    Программа должна вывести последовательность неубывающих чисел, полученных
    объединением двух данных списков.

    Примеры
    Тест 1
    Входные данные:
    1 5 7
    2 4 4 5

    Вывод программы:
    1 2 4 4 5 5 7



    Тест 2
    Входные данные:
    1 4 7
    1 5 6

    Вывод программы:
    1 1 4 5 6 7



    Тест 3
    Входные данные:
    1
    1

    Вывод программы:
    1 1

"""


def merge(A, B):
    ia, ib = 0, 0
    C = []
    while ia + ib < len(A) + len(B):
        if ia < len(A) and ib < len(B):
            if A[ia] < B[ib]:
                C.append(A[ia])
                ia += 1
            else:
                C.append(B[ib])
                ib += 1
        elif ia < len(A):
            C.append(A[ia])
            ia += 1
        else:
            C.append(B[ib])
            ib += 1
    return C


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = merge(lst1, lst2)

print(*lst3)
