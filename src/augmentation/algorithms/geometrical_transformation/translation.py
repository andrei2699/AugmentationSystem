from typing import List

import cv2
import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class TranslationAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Translation', parameters)

    def apply(self, image):
        x = self.get_parameter_or_default('x', 0)
        y = self.get_parameter_or_default('y', 0)

        translation = np.float32([[1, 0, x], [0, 1, y]])

        return cv2.warpAffine(image, translation, (image.shape[1], image.shape[0]))
