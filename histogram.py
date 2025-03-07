import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(img: np.ndarray )->None :
    """
    Создание и демонстрация гистограммы по 3 цветовым каналам
    :param img: np.ndarray массив пикселей изображения
    :return: None - просто демонстрация
    """
    colors = ('blue', 'green', 'red')
    shape = img.shape
    plt.figure(figsize=(10, 8))
    for i, color in enumerate(colors):
        lst = []
        for x in range(shape[0]):     # перебираем все пиксели и по ключевому каналу выбираем нужные
            for y in range(shape[1]): # для составления списка lst, по которому сможем разобрать конкретный канал
                lst.append(img[x, y, i])
        plt.subplot(3, 1, i + 1) # составляем столбец графиков (3 строки 1 столбец и индекс текущего графика(старт с 1))
        plt.hist(lst, bins=128, color=color)
        plt.title(f'Гистограмма {color} канала')
        plt.xlabel('Интенсивность')
        plt.ylabel('Кол-во пикселей')
    plt.subplots_adjust(hspace=0.5) # прослойка между графиками
    plt.show()