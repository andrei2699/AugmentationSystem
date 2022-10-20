from typing import List

import cv2
import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class ScalingAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Scaling', parameters)

    def apply(self, image):
        x = self.get_parameter_or_default('x', 1)
        y = self.get_parameter_or_default('y', 1)

        scaling = np.float32([[x, 0, 0], [0, y, 0]])

        return cv2.warpAffine(image, scaling, (image.shape[1], image.shape[0]))
