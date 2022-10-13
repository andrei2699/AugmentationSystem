from typing import List

import yaml
from munch import Munch

from src.augmentation.algorithm import Algorithm
from src.augmentation.algorithms.composite import CompositeAlgorithm
from src.augmentation.algorithms.identity import IdentityAlgorithm
from src.augmentation.algorithms.text_overlay import TextOverlayAlgorithm


class AlgorithmsSettings:
    def __init__(self, algorithms: List[Algorithm]):
        self.algorithms = algorithms


def load_algorithm_settings(file_path: str) -> AlgorithmsSettings:
    with open(file_path) as f:
        algorithm_settings_dict = yaml.unsafe_load(f)
        algorithm_settings: AlgorithmsSettings = Munch.fromDict(algorithm_settings_dict)

        algorithms = load_algorithms(algorithm_settings.algorithms)

        return AlgorithmsSettings(algorithms)


def load_algorithms(initialAlgorithms: List[Algorithm]):
    algorithms = []
    for x in initialAlgorithms:
        name = x.name
        parameters = x.parameters if 'parameters' in x else []

        if name == 'Composite':
            parameters[0].value = load_algorithms(parameters[0].value)

        algorithms.append(create_algorithm(name, parameters))

    return algorithms


def create_algorithm(name: str, parameters: List) -> Algorithm:
    if name == 'Identity':
        return IdentityAlgorithm()
    if name == 'TextOverlay':
        return TextOverlayAlgorithm(parameters)
    if name == 'Composite':
        return CompositeAlgorithm(parameters)
    else:
        raise Exception('Unknown algorithm: ' + name)
