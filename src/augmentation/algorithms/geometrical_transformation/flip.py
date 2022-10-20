from typing import List

import cv2

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class FlipAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Flip', parameters)

    def apply(self, image):
        vertical = self.get_parameter_or_default('vertical', False)
        horizontal = self.get_parameter_or_default('horizontal', False)

        if vertical and horizontal:
            return cv2.flip(image, -1)
        elif vertical:
            return cv2.flip(image, 0)
        elif horizontal:
            return cv2.flip(image, 1)

        return image
