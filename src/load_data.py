import json
import csv

from src.base_function import make_custom_users


def load_json(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        users = json.load(file)
    return users


def load_csv(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        books_csv_reader = csv.DictReader(file)
        books = [book for book in books_csv_reader]
    return books


def join_users_books(books, users):
    custom_users = make_custom_users(users)

    count_books = len(books)
    index_book = 0

    while index_book < count_books - 1:
        for user in custom_users:
            if index_book < count_books - 1:
                user['books'].append(
                    {
                        "title": books[index_book]['Title'],
                        "author": books[index_book]['Author'],
                        "pages": books[index_book]['Pages'],
                        "genre": books[index_book]['Genre']
                    }
                )
                index_book += 1
            else:
                break
    return custom_users
