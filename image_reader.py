import cv2
import numpy as np


def read_image(image_path: str) -> np.ndarray:
    """
    упаковываем изображение в массив np.ndarray
    :param image_path: путь к изображению
    :return: массив np.ndarray, который хранит пиксели изображения с соответствующими цветовыми каналами BGR
    """
    img = cv2.imread(image_path)
    if img is None: # одна из возможных проблем - неправильный формат файла
        raise FileNotFoundError(f"Не удалось загрузить изображение: {image_path}")
    return img

