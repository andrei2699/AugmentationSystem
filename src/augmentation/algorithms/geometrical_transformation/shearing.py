from typing import List

import cv2
import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class ShearingAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Shearing', parameters)

    def apply(self, image):
        x = self.get_parameter_or_default('x', 0)
        y = self.get_parameter_or_default('y', 0)

        shearing = np.float32([[1, x, 0], [y, 1, 0]])

        return cv2.warpAffine(image, shearing, (image.shape[1], image.shape[0]))
