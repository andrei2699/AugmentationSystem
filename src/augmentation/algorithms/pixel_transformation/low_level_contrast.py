from typing import List

import numpy as np

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class LowLevelContrastAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('LowLevelContrast', parameters)

    def apply(self, image):
        gain = self.get_parameter('gain')

        new_image = np.zeros(image.shape)

        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                for c in range(image.shape[2]):
                    new_image[x, y, c] = image[x, y, c] * gain

        return new_image
