

def open_file(filename:str)->str:
    """
       Чтение содержимого файла.
       :param filename: файл, из которого считываем данные
       :return: строка, составленная при объединении всех строк файла filename
    """
    with open(filename,'r',encoding='utf-8') as file:
        data = file.read()
    return  data