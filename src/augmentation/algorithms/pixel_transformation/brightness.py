from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class BrightnessAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Brightness', parameters)

    def apply(self, image):
        bias = self.get_parameter('bias')

        return bias + image
