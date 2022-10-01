from typing import List

from src.augmentation.parameter import Parameter


class Algorithm:
    def __init__(self, name: str, parameters: List[Parameter]):
        self.name = name
        self.parameters = parameters

    def apply(self, image):
        pass

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_parameters(self):
        return self.parameters
