import unittest

import numpy as np

from src.augmentation.algorithms.pixel_transformation.gamma_correction import GammaCorrectionAlgorithm
from src.augmentation.algorithms.pixel_transformation.gamma_correction_opencv import GammaCorrectionOpenCVAlgorithm
from src.augmentation.parameter import Parameter
from test.test_augmentation.algorithms.geometrical_transformation.utils import generate_random_image


class TestLowLevelContrast(unittest.TestCase):

    def test_low_level_rotation(self):
        image = generate_random_image((20, 20, 3))

        gamma_correction_algorithm = GammaCorrectionAlgorithm([Parameter('gamma', 0.2)])
        low_level_gamma_correction_algorithm = GammaCorrectionOpenCVAlgorithm([Parameter('gamma', 0.2)])

        corrected_image = gamma_correction_algorithm.apply(image)
        low_level_corrected_image = low_level_gamma_correction_algorithm.apply(image)

        self.assertTrue(np.array_equal(corrected_image, low_level_corrected_image))
