import numpy as np


def generate_random_image(shape):
    return np.random.randint(255, size=shape, dtype=np.uint8)
