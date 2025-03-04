import argparse

def parsing_arguments()->argparse.Namespace:
    '''
    парсинг аргументов командной строки
    :parameter: None
    :return: данные аргументов заключенные в объект argparse.Namespace
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    parser.add_argument('name', type=str, help='name of human for search')
    return parser.parse_args()