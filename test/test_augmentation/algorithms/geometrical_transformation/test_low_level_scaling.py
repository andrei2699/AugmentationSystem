import unittest

import numpy as np

from src.augmentation.algorithms.geometrical_transformation.low_level_shearing import LowLevelShearingAlgorithm
from src.augmentation.algorithms.geometrical_transformation.shearing import ShearingAlgorithm
from src.augmentation.parameter import Parameter
from test.test_augmentation.algorithms.geometrical_transformation.utils import generate_random_image


class Center:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class TestLowLevelShearing(unittest.TestCase):

    def test_low_level_shearing_with_only_x(self):
        image = generate_random_image((30, 30, 3))

        shearing_algorithm = ShearingAlgorithm([Parameter('x', 2), Parameter('y', 0)])
        low_level_shearing_algorithm = LowLevelShearingAlgorithm([Parameter('x', 2), Parameter('y', 0)])

        sheared_image = shearing_algorithm.apply(image)
        low_level_sheared_image = low_level_shearing_algorithm.apply(image)

        self.assertTrue(np.array_equal(sheared_image, low_level_sheared_image))

    def test_low_level_shearing_with_only_y(self):
        image = generate_random_image((30, 30, 3))

        shearing_algorithm = ShearingAlgorithm([Parameter('x', 0), Parameter('y', 2)])
        low_level_shearing_algorithm = LowLevelShearingAlgorithm([Parameter('x', 0), Parameter('y', 2)])

        sheared_image = shearing_algorithm.apply(image)
        low_level_sheared_image = low_level_shearing_algorithm.apply(image)

        self.assertTrue(np.array_equal(sheared_image, low_level_sheared_image))

    # def test_low_level_shearing_with_x_and_y(self):
    #     image = generate_random_image((30, 30, 3))
    #
    #     shearing_algorithm = ShearingAlgorithm([Parameter('x', 2), Parameter('y', 2)])
    #     low_level_shearing_algorithm = LowLevelShearingAlgorithm([Parameter('x', 2), Parameter('y', 2)])
    #
    #     sheared_image = shearing_algorithm.apply(image)
    #     low_level_sheared_image = low_level_shearing_algorithm.apply(image)
    #
    #     self.assertTrue(np.array_equal(sheared_image, low_level_sheared_image))
