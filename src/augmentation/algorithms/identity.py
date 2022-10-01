from src.augmentation.algorithm import Algorithm


class IdentityAlgorithm(Algorithm):
    def __init__(self):
        super().__init__('Identity', [])

    def apply(self, image):
        return image
