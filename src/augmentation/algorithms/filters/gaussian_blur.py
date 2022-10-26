from typing import List

import cv2

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class GaussianBlurAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('GaussianBlur', parameters)

    def apply(self, image):
        size = self.get_parameter('size')

        kernel = cv2.getGaussianKernel(size, 0)

        return cv2.filter2D(image, -1, kernel)
