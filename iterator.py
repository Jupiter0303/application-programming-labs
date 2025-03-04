import csv


class Iterator:

    """
    Итератор по все
    """

    def __init__(self, annotation: str)->None:
        """
        конструктор
        :param annotation: путь к файлу с аннотацией
        """
        self.annotation = annotation
        self.images = tuple()
        self.current = 0

        with open(self.annotation, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # пропуск заголовка
            self.images = tuple(reader)

    def __iter__(self)->'Iterator': # объект класса будет являться итерируемым
        return self

    def __next__(self)->tuple:
        """
         метод для реализации итерации
        :return: кортеж из абсолютного и относительного пути
        """
        if self.current < len(self.images):
            image = tuple(self.images[self.current])
            self.current += 1
            return image
        else:
            raise StopIteration
