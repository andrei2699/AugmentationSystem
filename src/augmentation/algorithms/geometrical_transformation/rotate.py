from typing import List

import cv2

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter


class RotationAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Rotation', parameters)

    def apply(self, image):
        angle = self.get_parameter_or_default('angle', 0)
        center = self.get_parameter_or_default('center', None)

        center_x = center.x if center is not None else image.shape[1] / 2
        center_y = center.y if center is not None else image.shape[0] / 2

        rotation = cv2.getRotationMatrix2D((center_x, center_y), angle, 1)

        return cv2.warpAffine(image, rotation, (image.shape[1], image.shape[0]))
