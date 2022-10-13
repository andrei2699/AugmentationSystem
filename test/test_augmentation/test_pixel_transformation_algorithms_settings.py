import unittest

from src.augmentation.algorithms_settings import load_algorithm_settings


# TODO: fix paths relative
class TestPixelTransformationAlgorithmsSettings(unittest.TestCase):
    def test_load_contrast_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/pixel_transformation/contrast_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Contrast')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'gain')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 0.8)

    def test_load_brightness_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/pixel_transformation/brightness_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Brightness')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'bias')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 0.5)
