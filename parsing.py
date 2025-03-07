import argparse


def parse_args()->argparse.Namespace:
    """
           парсинг аргументов командной строки
           :parameter: None
           :return: данные аргументов заключенные в объект argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='Путь к изображению для обработки')
    parser.add_argument('save_dir', type=str, help='Директория для сохранения результатов обработки')
    return parser.parse_args()