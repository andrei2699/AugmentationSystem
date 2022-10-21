import unittest

import numpy as np

from src.augmentation.algorithms.pixel_transformation.contrast import ContrastAlgorithm
from src.augmentation.algorithms.pixel_transformation.low_level_contrast import LowLevelContrastAlgorithm
from src.augmentation.parameter import Parameter
from test.test_augmentation.algorithms.geometrical_transformation.utils import generate_random_image


class TestLowLevelContrast(unittest.TestCase):

    def test_low_level_rotation(self):
        image = generate_random_image((20, 20, 3))

        contrast_algorithm = ContrastAlgorithm([Parameter('gain', 0.5)])
        low_level_contrast_algorithm = LowLevelContrastAlgorithm([Parameter('gain', 0.5)])

        contrasted_image = contrast_algorithm.apply(image)
        low_level_contrasted_image = low_level_contrast_algorithm.apply(image)

        self.assertTrue(np.array_equal(contrasted_image, low_level_contrasted_image))
