import unittest

import numpy as np

from src.augmentation.algorithms.geometrical_transformation.low_level_translation import LowLevelTranslationAlgorithm
from src.augmentation.algorithms.geometrical_transformation.translation import TranslationAlgorithm
from src.augmentation.parameter import Parameter
from test.test_augmentation.algorithms.geometrical_transformation.test_low_level_scaling import generate_random_image


class TestLowLevelTranslation(unittest.TestCase):

    def test_low_level_rotation(self):
        image = generate_random_image((20, 20, 3))

        translation_algorithm = TranslationAlgorithm([Parameter('x', 5), Parameter('y', 5)])
        low_level_translation_algorithm = LowLevelTranslationAlgorithm([Parameter('x', 5), Parameter('y', 5)])

        translated_image = translation_algorithm.apply(image)
        low_level_translated_image = low_level_translation_algorithm.apply(image)

        self.assertTrue(np.array_equal(translated_image, low_level_translated_image))
