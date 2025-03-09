import cv2
import os
import numpy as np

from image_reader import read_image
from parsing import parse_args
from histogram import plot_histogram
from image_flip import flip_image


def show_image(title:str, img: np.ndarray)->None:
    cv2.imshow(title, img)
    cv2.waitKey(0) # ждет нажатия клавиши для выхода
    cv2.destroyAllWindows()


def save_image(img, save_path):
    cv2.imwrite(save_path, img)


def main():
    """
    1) парсинг аргументов командной строки
    2) упаковка изображения в np.ndarray
    3) вывод размеров картинки
    4) создание и демонстрация гистограммы
    5)отражаем изображение по горизонтали
    6)демонстрация старого и нового изображения
    7)сохраняем новое изображение flipped_image.jpg
    """
    arguments = parse_args()
    try:
        if not os.path.isfile(arguments.image_path):
            raise FileNotFoundError(f"Файл {arguments.image_path} не найден")

        img = read_image(arguments.image_path)
        print(img.shape)
        print(f"Размер изображения: {img.shape[1]}x{img.shape[0]} ")

        plot_histogram(img)

        flipped_img = flip_image(img, 'horizontal')

        show_image('Исходное изображение', img)
        show_image('Отраженное изображение', flipped_img)

        save_path = os.path.join(arguments.save_dir, 'flipped_image.jpg')
        save_image(flipped_img, save_path)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

