"""
Завдання 3

Створіть список товарів в інтернет-магазині.
Серіалізуйте його за допомогою pickle та збережіть у JSON.

"""

import pickle
import json
import os



def main(path: str):
    internet_shop = [
    {
        "category": "toys",
        "item": 'soldier',
        'price': 45
    },
    {
        "category": "flowers",
        "item": 'lylies',
        'price': 10
    },
    {
        "category": "electronics",
        "item": 'iron',
        "price": 400
    },
    {
        "category": "electronics",
        "item": "tv",
        "price": 10000
    },
    {
        "category": "books",
        "item": 'sons III',
        'price': 4
    },
]

    with open(path + 'data.pickle', 'wb') as file:
        pickle.dump('internet_shop', file)

    with open(path + 'data_json.json', 'w') as file:
        json.dump(internet_shop, file, indent = 2, ensure_ascii = False)


if "__main__" == __name__:
    path = os.getcwd() + '/'
    main(path)