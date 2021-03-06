"""
    В олимпиаде по информатике принимало участие N человек. Определите школы,
    из которых в олимпиаде принимало участие больше всего участников. В этой
    задаче необходимо считывать данные построчно, не сохраняя в памяти данные
    обо всех участниках, а только подсчитывая число участников для каждой
    школы.

    Формат ввода

    Информация о результатах олимпиады записана в файле, каждая из строк
    которого имеет вид: фамилия имя школа балл
    Фамилия и имя — текстовые строки, не содержащие пробелов.
    Школа — целое число от 1 до 99.
    Балл — целое число от 0 до 100.

    Формат вывода
    Выведите номера этих школ в порядке возрастания.

    Примеры
Тест 1
Входные данные:
Иванов Сергей 14 56
Сергеев Петр 23 74
Петров Василий 3 99
Васильев Андрей 3 56
Андреев Роман 14 75
Романов Иван 27 68

Вывод программы:
3 14

"""

infile = open('input.txt', 'r', encoding='utf8')
tmp = [[0, i] for i in range(101)]
res = []

for line in infile:
    tmp[int(line.split()[-2])][0] += 1
max_ = max(tmp)[0]

for i in range(101):
    if tmp[i][0] == max_:
        res.append(tmp[i][1])
infile.close()

print(*res)
