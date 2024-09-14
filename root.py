import os

FILES_DIR = os.path.dirname(os.path.abspath(__file__))


def get_files():
    path_files = {
        'books.csv': os.path.join(FILES_DIR, 'files', 'books.csv'),
        'users.json': os.path.join(FILES_DIR, 'files', 'users.json'),
        'result.json': os.path.join(FILES_DIR, 'files', 'result.json'),
    }
    return path_files
