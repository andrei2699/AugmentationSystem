import unittest

from src.augmentation.algorithms_settings import load_algorithm_settings


# TODO: fix paths relative
class TestAlgorithmsSettings(unittest.TestCase):
    def test_load_identity_algorithm(self):
        algorithm_settings = load_algorithm_settings('test/test_augmentation/test_data/identity_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Identity')
        self.assertEqual(len(algorithm_settings.algorithms[0].parameters), 0)

    def test_load_text_overlay_algorithm(self):
        algorithm_settings = load_algorithm_settings('test/test_augmentation/test_data/text_overlay_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'TextOverlay')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'text')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 'Some Text')

    def test_load_composite_algorithm(self):
        algorithm_settings = load_algorithm_settings('test/test_augmentation/test_data/composite_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Composite')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'algorithms')

        composite_algorithms = algorithm_settings.algorithms[0].parameters[0].value
        self.assertEqual(len(composite_algorithms), 3)
        self.assertEqual(composite_algorithms[0].name, 'TextOverlay')
        self.assertEqual(composite_algorithms[0].parameters[0].name, 'text')
        self.assertEqual(composite_algorithms[0].parameters[0].value, 'Some Text')
        self.assertEqual(composite_algorithms[1].name, 'Identity')
        self.assertEqual(len(composite_algorithms[1].parameters), 0)
        self.assertEqual(composite_algorithms[2].name, 'Composite')
        self.assertEqual(composite_algorithms[2].parameters[0].name, 'algorithms')

        nested_composite_algorithms = composite_algorithms[2].parameters[0].value
        self.assertEqual(len(nested_composite_algorithms), 1)
        self.assertEqual(nested_composite_algorithms[0].name, 'TextOverlay')
        self.assertEqual(nested_composite_algorithms[0].parameters[0].name, 'text')
        self.assertEqual(nested_composite_algorithms[0].parameters[0].value, 'Other Text')
