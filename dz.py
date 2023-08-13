# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# o doctest,
# o unittest,
# o pytest.

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

text = input("1. Здравствуйте. Введите желаемый текст\n: ")
res = newstr(text)
print(f"\nРезультат:" )
print(*res, sep="\n")

if __name__ == '__main__':
    from doctest import testmod
    from doctest import testfile
    testmod(verbose=True)
    # testfile('testtxt.md', verbose=True)