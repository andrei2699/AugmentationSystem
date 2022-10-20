from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.algorithms.geometrical_transformation.low_level_utils import convert_image_to_points, \
    convert_points_to_image
from src.augmentation.parameter import Parameter


class LowLevelTranslationAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('LowLevelRotation', parameters)

    def apply(self, image):
        x = self.get_parameter_or_default('x', 0)
        y = self.get_parameter_or_default('y', 0)

        points = convert_image_to_points(image)

        for point in points:
            point.x += x
            point.y += y

        return convert_points_to_image(points, image.shape)
