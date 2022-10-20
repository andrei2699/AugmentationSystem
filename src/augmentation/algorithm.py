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

    def get_parameter(self, name: str):
        for x in self.parameters:
            if x.name == name:
                return x.value

        raise Exception('Parameter not found: ' + name)

    def get_parameter_or_default(self, name: str, default):
        for x in self.parameters:
            if x.name == name:
                return x.value

        return default
