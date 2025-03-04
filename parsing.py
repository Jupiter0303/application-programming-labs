import argparse


def parsing_arguments() -> argparse.Namespace:
    '''
       парсинг аргументов командной строки
       :parameter: None
       :return: данные аргументов заключенные в объект argparse.Namespace
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help="keyword for search")
    parser.add_argument('save_path', type=str, help="the path to the folder to save")
    parser.add_argument("annotation", type=str, help="the path to the annotation file")
    return parser.parse_args()
