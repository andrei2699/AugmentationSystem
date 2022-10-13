from src.augmentation.algorithm import Algorithm
import cv2


class GreyscaleAlgorithm(Algorithm):
    def __init__(self):
        super().__init__('Greyscale', [])

    def apply(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
