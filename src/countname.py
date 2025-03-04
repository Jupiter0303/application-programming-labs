import re


def count_copy_name(text: str, name: str) -> int:
    """
     Подсчет повторений имени name в строке text
     :param text: строка, в которой ищем совпадения
     :param name: строка для создания шаблона поиска
     :return: кол-во повторений
    """
    pattern = fr'Имя: {name}\n'
    re.findall(pattern, text)
    return len(re.findall(pattern, text))

