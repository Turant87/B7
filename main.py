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


from scrypt import area_circle
from scrypt import square_area
from scrypt import triangle_area

print(area_circle(2))
print(square_area(4))
print(triangle_area(2, 6))




