"""
Завдання 1

Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

"""

import random
import os

def main(path: str):
    with open(path + 'answer.txt', 'w') as file:
        for i in range(1, 10001):
            file.writelines((str(random.randint(1, 10000))+'\n'))


if "__main__" == __name__:
    path = os.getcwd() + '/'
    main(path)