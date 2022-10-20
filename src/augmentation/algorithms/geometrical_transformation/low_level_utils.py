import numpy as np


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def apply_translation(self, new_x, new_y):
        self.x += new_x
        self.y += new_y


def convert_image_to_points(image):
    points = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            points.append(Point(x, y, image[x, y]))
    return points


def convert_points_to_image(points, image_shape):
    image = np.zeros(image_shape)

    for point in points:
        if 0 <= point.x < image_shape[0] and 0 <= point.y < image_shape[1]:
            image[point.x, point.y] = point.color

    return image
