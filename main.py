from src.load_data import load_json, load_csv, join_users_books
from src.dump_data import dump_to_json
from root import get_files


def books_to_users():
    path_json_users = get_files()['users.json']
    users = load_json(path_json_users)

    path_csv_books = get_files()['books.csv']
    books = load_csv(path_csv_books)

    path_result = get_files()['result.json']
    custom_users = join_users_books(books, users)

    dump_to_json(path_result, custom_users)


if __name__ == '__main__':
    books_to_users()
