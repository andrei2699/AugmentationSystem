from typing import List

import yaml
from munch import Munch

from src.augmentation.algorithm import Algorithm
from src.augmentation.algorithms.clip import ClipAlgorithm
from src.augmentation.algorithms.composite import CompositeAlgorithm
from src.augmentation.algorithms.geometrical_transformation.flip import FlipAlgorithm
from src.augmentation.algorithms.geometrical_transformation.resizing import ResizingAlgorithm
from src.augmentation.algorithms.geometrical_transformation.rotate import RotationAlgorithm
from src.augmentation.algorithms.geometrical_transformation.scaling import ScalingAlgorithm
from src.augmentation.algorithms.geometrical_transformation.shearing import ShearingAlgorithm
from src.augmentation.algorithms.geometrical_transformation.translation import TranslationAlgorithm
from src.augmentation.algorithms.greyscale import GreyscaleAlgorithm
from src.augmentation.algorithms.identity import IdentityAlgorithm
from src.augmentation.algorithms.pixel_transformation.brightness import BrightnessAlgorithm
from src.augmentation.algorithms.pixel_transformation.contrast import ContrastAlgorithm
from src.augmentation.algorithms.pixel_transformation.gamma_correction import GammaCorrectionAlgorithm
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


def load_algorithms(initial_algorithms: List[Algorithm]):
    algorithms = []
    for x in initial_algorithms:
        name = x.name
        parameters = x.parameters if 'parameters' in x else []

        if name == 'Composite':
            parameters[0].value = load_algorithms(parameters[0].value)

        algorithms.append(create_algorithm(name, parameters))

    return algorithms


# TODO: maybe rethink a little bit the creation of algorithms
def create_algorithm(name: str, parameters: List) -> Algorithm:
    if name == 'Composite':
        return CompositeAlgorithm(parameters)
    if name == 'Identity':
        return IdentityAlgorithm()
    if name == 'Clip':
        return ClipAlgorithm(parameters)
    if name == 'Greyscale':
        return GreyscaleAlgorithm()
    if name == 'TextOverlay':
        return TextOverlayAlgorithm(parameters)
    if name == 'Contrast':
        return ContrastAlgorithm(parameters)
    if name == 'Brightness':
        return BrightnessAlgorithm(parameters)
    if name == 'GammaCorrection':
        return GammaCorrectionAlgorithm(parameters)
    # TODO
    # if name == 'BoxFilter':
    #     return BoxFilterAlgorithm(parameters)
    if name == 'Translation':
        return TranslationAlgorithm(parameters)
    if name == 'Resizing':
        return ResizingAlgorithm(parameters)
    if name == 'Scaling':
        return ScalingAlgorithm(parameters)
    if name == 'Shearing':
        return ShearingAlgorithm(parameters)
    if name == 'Flip':
        return FlipAlgorithm(parameters)
    if name == 'Rotation':
        return RotationAlgorithm(parameters)

    else:
        raise Exception('Unknown algorithm: ' + name)
