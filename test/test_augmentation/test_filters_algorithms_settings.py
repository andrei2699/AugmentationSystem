# TODO: fix paths relative
import unittest

from src.augmentation.algorithms_settings import load_algorithm_settings


class TestFiltersAlgorithmsSettings(unittest.TestCase):
    def test_load_box_filter_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/filters/box_filter_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'BoxFilter')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'size')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 3)

    def test_load_gaussian_blur_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/filters/gaussian_blur_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'GaussianBlur')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'size')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 3)
