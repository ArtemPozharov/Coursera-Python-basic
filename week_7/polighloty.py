"""
    Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие
    языки знают все школьники и языки, которые знает хотя бы один из
    школьников.

    Формат ввода
    Первая строка входных данных содержит количество школьников N.
    Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих
    названия языков, которые знает i-й школьник. Длина названий языков не
    превышает 1000 символов, количество различных языков не более 1000.
    1≤N≤1000, 1≤Mᵢ≤500.

    Формат вывода
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков. Затем - количество языков,
    которые знает хотя бы один школьник, на следующих строках -
    список таких языков.

Примеры
Тест 1
Входные данные:
3
3
Russian
English
Japanese
2
Russian
English
1
English

Вывод программы:
1
English
3
Russian
Japanese
English

"""

shared_languages = set()
all_languages = set()
schoolchildren = [set() for i in range((int(input())))]
for schoolchild in schoolchildren:
    for m in range((int(input()))):
        language = input().rstrip()
        schoolchild.add(language)
        all_languages.add(language)

shared_languages |= all_languages
for i in schoolchildren:
    shared_languages &= i

print(len(shared_languages))
for i in shared_languages:
    print(i)

print(len(all_languages))
for i in all_languages:
    print(i)
