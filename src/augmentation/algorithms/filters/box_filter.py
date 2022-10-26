from typing import List

import cv2
import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class BoxFilterAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('BoxFilter', parameters)

    def apply(self, image):
        size = self.get_parameter('size')

        kernel = np.ones((size, size)) / (size * size)

        return cv2.filter2D(image, -1, kernel)
