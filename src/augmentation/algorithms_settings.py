from typing import List

import yaml

from src.augmentation.algorithm import Algorithm
from src.augmentation.algorithms.identity import IdentityAlgorithm


class AlgorithmsSettings:
    def __init__(self, algorithms: List[Algorithm]):
        self.algorithms = algorithms


def load_algorithm_settings(file_path: str) -> AlgorithmsSettings:
    with open(file_path) as f:
        algorithm_settings_dict = yaml.safe_load(f)

        algorithms_dict = algorithm_settings_dict['algorithms']

        algorithms = []

        for x in algorithms_dict:
            name = x['name']
            parameters = x['parameters'] if 'parameters' in x else []

            algorithms.append(load_algorithm(name, parameters))

        return AlgorithmsSettings(algorithms)


def load_algorithm(name: str, parameters: List) -> Algorithm:
    if name == 'Identity':
        return IdentityAlgorithm()
    else:
        raise Exception('Unknown algorithm: ' + name)
