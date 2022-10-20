import unittest

from src.augmentation.algorithms_settings import load_algorithm_settings


# TODO: fix paths relative
class TestGeometricalTransformationAlgorithmsSettings(unittest.TestCase):
    def test_load_translation_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/translation_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Translation')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'x')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 50)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'y')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value, 50)

    def test_load_scaling_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/scaling_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Scaling')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'x')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 1.25)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'y')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value, 1.6)

    def test_load_resizing_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/resizing_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Resizing')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'x')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 0.8)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'y')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value, 1)

    def test_load_shearing_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/shearing_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Shearing')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'x')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 0.2)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'y')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value, 0.1)

    def test_load_flip_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/flip_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Flip')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'vertical')
        self.assertTrue(algorithm_settings.algorithms[0].parameters[0].value)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'horizontal')
        self.assertFalse(algorithm_settings.algorithms[0].parameters[1].value)

    def test_load_rotation_algorithm(self):
        algorithm_settings = load_algorithm_settings(
            'test/test_augmentation/test_data/geometrical_transformation/rotation_algorithm.yaml')

        self.assertEqual(len(algorithm_settings.algorithms), 1)
        self.assertEqual(algorithm_settings.algorithms[0].name, 'Rotation')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].name, 'angle')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[0].value, 45)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].name, 'center')
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value.x, 0.5)
        self.assertEqual(algorithm_settings.algorithms[0].parameters[1].value.y, 0.5)
