# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# o doctest,
# o unittest,
# o pytest.

import unittest
import math

# Семинар 2 Задание 4
# Напишите программу, которая вычисляет площадь 
# круга и длину окружности по введённому диаметру. 
# ✔ Диаметр не превышает 1000 у.е. 
# ✔ Точность вычислений должна составлять 
# не менее 42 знаков после запятой.

print("\n1.")
def diamcom(d):
    """
    >>> diamcom(66)
    (18.04707580845021, 207.34511513692635)
    """
    r = d / 2
    s = math.pi * math.sqrt(r)
    l = 2 * math.pi * r
    print("Площадь данного круга\n: ", f'{s:.50g}')
    print("Длина данного круга\n: ", f'{l:.50g}')
    return s, l

class ComTest(unittest.TestCase):
    def test_diamcom(self):
        res = diamcom(66)
        self.assertEqual(res, (18.04707580845021, 207.34511513692635), msg='Что-то пошло не так...')

def test_diamcom():
    res = diamcom(66)
    assert len(res) == 2

compute = True
while (compute):
    diameter = float(input("Введите желаемое значение диаметра (до 1000)\n: "))
    if diameter < 1000:
        diamcom(diameter)
        compute = False

# Семинар 3 Задание 2
# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

def industry(mylist):
    """
    >>> industry('5614245456486')
    ['5', '6', '4']
    """
    warehouse = list(mylist)
    market = list()
    check = ''
    list(set(warehouse))
    for i in range(0, len(warehouse)):
        got = 0
        for j in range(0, len(warehouse)):
            if warehouse[i] == warehouse[j] and warehouse[j] != check:
                got += 1
                if got > 1 and warehouse[i] != ' ':
                    market.insert(j, warehouse[i])
                    check = warehouse[i]

    if len(market) == 0:
        market.insert(0, 'empty')
    return market

class IndusTest(unittest.TestCase):
    def test_industry(self):
        res = industry('5614245456486')
        self.assertEquals(res, ['5', '6', '4'], msg='Что-то пошло не так :(')

def test_industry():
    assert len(res) == 3
    assert res == ['5', '6', '4']

mylist = input("2. Здравствуйте. Введите желаемый текст/число\n: ")

print("Лист повторяющихся элементов\n: ", list(set(industry(mylist))))

# Семинар 4 Задание 1
# ✔ Напишите функцию, которая принимает строку текста. 
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого 
# длинного слова был один пробел между ним и номером строки.

def newstr(text, nid = 0):
    """
    Выводит каждое введённое пользователем значение с новой строки, с нумерацией, отсортированно согласно Unicode
    >>> newstr('Hello World!')
    ['1. Hello', '2. World!']
    """
    text = sorted(text.split())
    stext = list()

    for line in text:
        nid += 1
        stext.append(str(nid) + '. ' + line)
        # print(f'{nid}. {line}')
    return stext

class NewTest(unittest.TestCase):
    def test_newstr(self):
        res = newstr(text)
        self.assertEqual(res, ['1. Hello', '2. World!'], msg='Что-то пошло не так...')

def test_newstr():
    assert len(res) == 2
    assert res == ['1. Hello', '2. World!']

text = input("2. Здравствуйте. Введите желаемый текст\n: ")
res = newstr(text)
print(f"\nРезультат:" )
print(*res, sep="\n")

# Тесты

if __name__ == '__main__':
    from doctest import testmod
    from doctest import testfile
    testmod(verbose=True)
    # testfile('testtxt.md', verbose=True)

if __name__ == '__main__':
    unittest.main()