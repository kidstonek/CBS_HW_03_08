"""
Завдання 2

Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
щоб він зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете
ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html),
який у даному випадку буде дуже зручним та спростить виконання завдання.
"""

my_lib = {}
while True:
    print("choose what to do - 1) add items, 2) search by name, 3) show all")
    option = input('choose options: ')
    if option == '1':
        while True:
            big_url = input('введіть полний URL: ')
            if big_url:
                name = input('введіть назву: ')
                my_lib[name] = big_url
            else:
                print('end of input!')
                break
    elif option == '2':
        print('what to search?')
        search_name = input("what name?")
        if my_lib[search_name]:
            print(my_lib[search_name])
        else:
            print('nothing found')
            break
    elif option == '3':
        print(my_lib)
    else:
        print('end!')
        break