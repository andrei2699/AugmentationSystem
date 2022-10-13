from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class GammaCorrectionAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('GammaCorrection', parameters)

    def apply(self, image):
        gamma = self.get_parameter('gamma')
        gamma_inverse = (1 / gamma)

        return ((image / 255.0) ** gamma_inverse) * 255
