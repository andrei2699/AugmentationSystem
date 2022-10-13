from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class CompositeAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Composite', parameters)

    def apply(self, image):
        algorithms = self.get_parameter('algorithms')

        for algorithm in algorithms:
            image = algorithm.apply(image)

        return image

    def get_name(self):
        return '_'.join([x.get_name() for x in self.get_parameter('algorithms')])
