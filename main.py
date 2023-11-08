# try:
#     raise ZeroDivisionError # возбуждаем исключение ZeroDivisionError
# except ArithmeticError: # ловим его родителя
#     print("Hello from arithmetic error")

# class ParentException(Exception):
#     def __init__(self, message,
#                  error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
#         super().__init__(message)  # помним про вызов конструктора родительского класса
#         print(f"Errors: {error}")  # печатаем ошибку
#
#
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     def __init__(self, message, error):
#         super().__init__(message, error)
#
#
# try:
#     raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
# except ParentException as e:
#     print(e)  # выводим информацию об исключении

# import os
# import sys
#
# print(os.getcwd())
# print(os.listdir())

# import math
# print(math.pi)

# import math as m # Даем новое имя Модулю
# print(m.pi)

# from math import pi as PI # Даем новое имя функции или переменной
# print(PI)

# import time
#
# print(time.strftime('%X')) # Вывод времени
# print(time.strftime('%M')) # Вывод минут
# print(time.strftime('%x')) # Вывод даты
# print(time.strftime('%m')) # Вывод месяца

# import time
#
# i = 10
#
# while i != -1:
#     print(i)
#     time.sleep(1)
#     i -= 1
# print('Время вышло')


# from scrypt import area_circle
# from scrypt import square_area
# from scrypt import triangle_area
#
# print(area_circle(2))
# print(square_area(4))
# print(triangle_area(2, 6))

# import os
#
# start_path = os.getcwd() # Получить текущий путь
# print(start_path)
# print(os.listdir())
# if 'main.py' not in os.listdir():
#     print('Файла main.py, нет в директории!')
# else:
#     print('Все хорошо, файл main.py на месте')

# f = open('text.txt', 'w', encoding='utf8') # Создали файл
# f.write('Какой-то текст!\n') # Записали что-то в файл
# f.write('Еще текст!\n')
# f.close() # Обязательно закрыли файл
#
# f = open('text.txt', 'r', encoding='utf8') # Открыли файл
# print(f.read())
# f.close()
#
# f = open('text.txt', 'a', encoding='utf8') # Открыли файл на дозапись
# sequense = ['Other string?\n', '12345\n', 'И еще одна строка!\n']
# f.writelines(sequense) # Берет строки из sequnse и записывает в файл
# f.close()
#
# f = open('text.txt', 'r', encoding='utf8')
# print(f.readline()) # Метод f.readline() возвращает строку (символы от текущей позиции до символа переноса строки):
# print(f.read(4))
# print(f.readline())
# f.close()
#
# with open('text.txt', 'a', encoding='utf8') as f: # Убирает необходимость открытия и ЗАКРЫТИЯ файла
#     f.writelines('Еще чуть-чуть текста?\n')
#
# f = open('text.txt', 'r', encoding='utf8')
# for line in f:
#     print(line, ('|' * 10))
# f.close()

# with open('input.txt', 'r') as input_file: # Открыте файла input.txt на чтение
#    with open('output.txt', 'w') as output_file: # Открытие файла output.txt на запись
#        for line in input_file:
#            output_file.write(line) # Построчная перезапись данных из файла input.txt в файл output.txt

with open('numbers.txt', 'r', encoding='utf8') as f:
    numbers = []
    for line in f:
        numbers.append(float(line))
    sum_ = min(numbers) + max(numbers)
with open('output.txt', 'a', encoding='utf8') as output_file:
    output_file.write('Сумма наибольшего и наименьшего числа в файле = ' + str(sum_))
    output_file.write('\n')
print(min(numbers), '---', max(numbers))









