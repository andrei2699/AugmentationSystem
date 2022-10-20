from typing import List

import cv2

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class ResizingAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Resizing', parameters)

    def apply(self, image):
        x = self.get_parameter_or_default('x', 1)
        y = self.get_parameter_or_default('y', 1)

        return cv2.resize(image, None, fx=x, fy=y, interpolation=cv2.INTER_CUBIC)
