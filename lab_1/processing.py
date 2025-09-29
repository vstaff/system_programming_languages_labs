# функции связанные с обработкой, генерацией данных


from collections import defaultdict
import statistics as stats
import csv 
import random
from util import DATA_FOLDER, ROWS_AMOUNT, CATEGORIES, get_random_float, Category, RESULTS_FOLDER


def generate_csv_files(amount: int, name: str) -> None:
    """Генерирует заданное число csv-файлов с заданным общим именем (файлы отличаются индексом). Каждый файл состоит из ROWS_AMOUNT строк, двух столбцов - первый столбец - случайная буква из набора A, B, C, D, второй столбец - случайное число от FLOAT_MIN до FLOAT_MAX

    Args:
        amount (int): количество файлов которые надо сгенерировать
        name (str): общее имя для файлов (без индекса и .csv)
    """
    for i in range(amount):
        filename = f"./{DATA_FOLDER}/{name}_{i + 1}.csv"
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            for j in range(ROWS_AMOUNT):
                category = random.choice(CATEGORIES).value
                value = get_random_float()
                writer.writerow([category, value])


def process_file(filename: str) -> dict[Category, list[float, float]]:
    """Обработка файла - получение медианы и стандартного отклонения для каждой буквы в рамках этого файла

    Args:
        filename (str): название файла который нужно обработать

    Returns:
        dict[Category, tp.List[float, 2]]: категория: [медиана, стандартное отклонение]
    """
    data: dict[Category, list[float]] = defaultdict(list)
    
    with open(f"./{DATA_FOLDER}/{filename}", encoding="utf-8", mode="r") as file: 
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            letter = row[0].strip()
            value = float(row[1].strip())
            data[letter].append(value)
    
    result = { letter: [stats.median(values), stats.stdev(values)] for letter, values in data.items() }
    
    return result


def secondary_processing(amount: int) -> None:
    """Вторичная обработка файлов (вторая часть задания)

    Args:
        amount (int): количество файлов, появившихся после первичной обработки, которые надо обработать
    """
    files_medians: dict[Category, list[float]] = defaultdict(list)
    
    for i in range(amount):
        with open(f"./{RESULTS_FOLDER}/result_{i + 1}.csv", encoding="utf-8", mode="r") as result_file:
            reader = csv.reader(result_file)
            for row in reader:
                category: Category = row[0]
                median = float(row[1])
                files_medians[category].append(median)
                
    with open(f"{RESULTS_FOLDER}/RESULT.csv", mode="x+", newline="") as result:
        writer = csv.writer(result)
        for category, values in files_medians.items():
            median = stats.median(values)
            stdev = stats.stdev(values)
            writer.writerow([category, median, stdev])