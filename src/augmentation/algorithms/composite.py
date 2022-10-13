from typing import List

from src.augmentation.algorithm import Algorithm
from src.augmentation.parameter import Parameter
import cv2


class CompositeAlgorithm(Algorithm):
    def __init__(self, parameters: List[Parameter]):
        super().__init__('Composite', parameters)

    def apply(self, image):
        text = self.get_parameter('text')

        cv2.putText(image, text, (int(image.shape[1] / 2), int(image.shape[0] / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 0), 2)

        return image
