from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class ClipAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Clip', parameters)

    def apply(self, image):
        min_clip = self.get_parameter('min')
        max_clip = self.get_parameter('max')

        return image.clip(min_clip, max_clip)
