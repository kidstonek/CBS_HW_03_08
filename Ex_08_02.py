"""
Завдання 2

Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
щоб він зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете
ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html),
який у даному випадку буде дуже зручним та спростить виконання завдання.
"""


import shelve


while True:
    print("choose what to do:\n1) add items:\n2) search by name\n3) show all")
    option = input('choose options: ')
    if option == '1':
        with shelve.open('my_shelve.db') as my_lib:
            while True:
                print('Return для закінчення вводу')
                big_url = input('введіть повний URL: ')
                if big_url:
                    name = input('введіть короткий URL: ')
                    my_lib[name] = big_url
                else:
                    print('end of input!')
                    break
    elif option == '2':
        print('what to search?')
        search_name = input("what name? ")
        with shelve.open('my_shelve.db') as my_lib:
            found_something = False
            for key in my_lib:
                if key.lower() == search_name.lower():
                    print(my_lib[key])
                    input()
                    found_something = True
                    break
                continue
            if not found_something:
                input('nothing found')
    elif option == '3':
        with shelve.open('my_shelve.db') as my_lib:
            for key in my_lib:
                print(f'short url: {key} normal url {my_lib[key]}')
    else:
        print('end!')
        break