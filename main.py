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

# with open('numbers.txt', 'r', encoding='utf8') as f:
#     numbers = []
#     for line in f:
#         numbers.append(int(line))
#     sum_ = min(numbers) + max(numbers)
# with open('output.txt', 'a', encoding='utf8') as output_file:
#     output_file.write('Сумма наибольшего и наименьшего числа в файле = ' + str(sum_))
#     output_file.write('\n')
# print(min(numbers), '---', max(numbers))


# output = ""
# for line in open ("input.txt", 'r', encoding="UTF-8"):
#    points = int(line.split()[-1])
#    if points < 3:
#        output += line
# print(output)

# from datetime import datetime
# import time  # проверять действие измерителя будем с помощью библиотеки time
# # вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием и закрытием контекстного менеджера
# class Timer:
#     def __init__(self):
#         pass
#     def __enter__(self):  # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
#         self.start = datetime.utcnow()
#         return None
#     def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
#         print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")
#
# with Timer():
#     time.sleep(2)  # засыпаем на 2 секунды
#
# from datetime import datetime
# import time
#
# from contextlib import contextmanager  # импортируем нужный нам декоратор
# @contextmanager  # оборачиваем функцию в декоратор contextmanager
# def timer():
#     start = datetime.utcnow()
#     yield  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
#     print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")
#
# with timer():
#     time.sleep(2)

# class OpenFile:
#     def __init__(self, path, type):
#         self.file = open(path, type)
#     def __enter__(self):
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with OpenFile ('hello.txt', 'w') as f:
#     f.write('Мой контекстный менеджер!\nВроде работает')



# Стэк

# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем ее в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент - открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит возвращаем True, иначе - False
#     return len(stack) == 0

# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
#
# def top():  # выводим приоритетную задачу
#         print("Задача №%d в приоритете" % (queue[head]))
#
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "top":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             top()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")


#
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#         print(self.value) # процедура обработки
#
#         if self.left_child is not None: # если левый потомок существует
#             self.left_child.pre_order() # рекурсивно вызываем функцию
#
#         if self.right_child is not None: # если правый потомок существует
#             self.right_child.pre_order() # рекурсивно вызываем функцию
#
#     def post_order(self):
#         if self.left_child is not None: # если левый потомок существует
#             self.left_child.post_order() # рекурсивно вызываем функцию
#
#         if self.right_child is not None: # если правый потомок существует
#             self.right_child.post_order() # рекурсивно вызываем функцию
#
#         print(self.value) # процедура обработки
#
#     def in_order(self):
#         if self.left_child is not None: # если левый потомок существует
#             self.left_child.in_order() # рекурсивно вызываем функцию
#
#         print(self.value) # процедура обработки
#
#         if self.right_child is not None: # если правый потомок существует
#             self.right_child.in_order() # рекурсивно вызываем функцию
#
#
#
# # A_node = BinaryTree('A').insert_left('B').insert_right('C')
# # создаем корень и его потомки /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
# # node_root.pre_order()
# node_root.post_order()
# # node_root.in_order()


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None: # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last: # если список содержит только один элемент
#             node = self.first # сохраняем его
#             self.__init__() # очищаем
#             return node # и возвращаем сохраненный элемент
#         else:
#             node = self.first # сохраняем первый элемент
#             self.first = self.first.next # меняем указатель на первый элемент
#             return node # возвращаем сохраненный
#     def popright(self):
#         if self.first is None: # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last: # если список содержит только один элемент
#             node = self.first # сохраняем его
#             self.__init__() # очищаем
#             return node # и возвращаем сохраненный элемент
#         else:
#             node = self.last # сохраняем последний
#             pointer = self.first # создаем указатель
#             while pointer.next is not node: # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None # обнуляем указатели, чтобы
#             self.last = pointer # предпоследний стал последним
#             return node # возвращаем сохраненный
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохраненный
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)
# print(len(LL))


# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
#
# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#             count += 1
#     return count


# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))


# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счетчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698

# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)
# print(len(str(factorial)))


# count = 0
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):  #
#         count += 1
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
#
# print(array)
# print(count)

count = 0
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]

# print(array)

for i in range(1, len(array)):
    x = array[i]
    idx = i

    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1
    array[idx] = x



print(array)
print(count)

