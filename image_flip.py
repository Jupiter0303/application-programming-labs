from argparse import ArgumentTypeError

import cv2
import numpy as np


def flip_image(img: np.ndarray, direction: str) -> np.ndarray:
    """
    отражение изображения по заданной оси
    :param img:  np.ndarray массив пикселей изображения
    :param direction: ось, относительно которой будем отражать изображение
    :return: новый массив np.ndarray
    """
    if direction == 'horizontal':
        return cv2.flip(img, 1)
    elif direction == 'vertical':
        return cv2.flip(img, 0)
    else:
        raise  ArgumentTypeError('Некорректный direction в flip_image')