import csv
from concurrent.futures import ProcessPoolExecutor
from util import DATA_FOLDER, RESULTS_FOLDER, delete_files_in_folder
from processing import generate_csv_files, process_file, secondary_processing


def main() -> None:
    # предварительно очищаем папки с данными
    delete_files_in_folder(DATA_FOLDER)
    delete_files_in_folder(RESULTS_FOLDER)
    
    # генерируем файлы 
    files_name = input("Type name for your files without extension (all your files will have that name, plus its index and .csv extension): ")
    files_amount = int(input("Type amount of files you want to generate: "))
    generate_csv_files(amount=files_amount, name=files_name)
    files = [f"{files_name}_{i + 1}.csv" for i in range(files_amount)]
    
    # параллельная обработка файлов 
    with ProcessPoolExecutor() as executor:
        data_from_files = list(executor.map(process_file, files))
    
    # сохраняем данные в файлы
    for i in range(files_amount):
        with open(f"./{RESULTS_FOLDER}/result_{i + 1}.csv", mode="w", newline="") as result:
            writer = csv.writer(result)
            for category, values in data_from_files[i].items():
                median = values[0]
                stdev = values[1]
                writer.writerow([category, median, stdev])
    
    # вторичная обработка данных (ну то есть вторая часть лабораторной)
    secondary_processing(amount=files_amount)


if __name__ == "__main__":
    main()