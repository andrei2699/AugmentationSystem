from typing import List

import cv2
import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class GammaCorrectionOpenCVAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('GammaCorrectionOpenCV', parameters)

    def apply(self, image):
        gamma = self.get_parameter('gamma')

        return adjust_gamma(image, gamma)


def adjust_gamma(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)])

    return cv2.LUT(image, table)
