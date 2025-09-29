# вспомогательные функции, переменные и т.д.


import os
import random


from enum import Enum


class Category(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


# "настройки" скрипта
CATEGORIES = [*Category]
FLOAT_MIN = 1.0
FLOAT_MAX = 100.0
ROWS_AMOUNT = 30
DATA_FOLDER = "data" # убедитесь что папка существует
RESULTS_FOLDER = "results" # то же самое


def get_random_float() -> float:
    return random.uniform(FLOAT_MIN, FLOAT_MAX)

 
def delete_files_in_folder(folder_path: str) -> None:
    """Очистка содержимого папки находящейся на пути folder_path

    Args:
        folder_path (str): путь к папке которую надо почистить
    """
    if not os.path.isdir(folder_path):
        print(f'Папка {folder_path} не существует')
        return 
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')
