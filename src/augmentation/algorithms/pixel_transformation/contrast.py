from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class ContrastAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Contrast', parameters)

    def apply(self, image):
        gain = self.get_parameter('gain')

        return image * gain
