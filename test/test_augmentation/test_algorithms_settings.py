import unittest

from src.augmentation.algorithms_settings import load_algorithm_settings


class TestAlgorithmsSettings(unittest.TestCase):
    def test_load_identity_algorithm(self):
        algorithm_settings = load_algorithm_settings('test/test_augmentation/test_data/identity_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Identity')

    def test_load_text_overlay_algorithm_algorithm(self):
        algorithm_settings = load_algorithm_settings('test/test_augmentation/test_data/text_overlay_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'TextOverlay')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'text')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 'Some Text')
