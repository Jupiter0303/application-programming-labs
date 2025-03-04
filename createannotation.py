import csv
import os


def create_annotation(annotation: str, path:str) -> None:
    """
    заполнение файла аннотации
    :param annotation: файл аннотации, в который внесем пары абсолютного
                       и относительного путей к картинкам
    :param path: путь к папке с картинками
    :return: ничего не возвращает
    """
    image_paths = []
    for filename in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, filename))
        rel_path = os.path.relpath(abs_path, path)
        image_paths.append((abs_path, rel_path))

    with open(annotation, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute Path", "Relative Path"])
        writer.writerows(image_paths)