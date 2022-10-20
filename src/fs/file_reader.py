import os
from pathlib import Path

import cv2


def get_files_with_extension(input_path):
    for f in os.listdir(input_path):
        if os.path.isfile(os.path.join(input_path, f)):
            path = Path(f)
            name = path.stem
            extension = path.suffix

            yield name, extension


def combine_paths(path1, path2):
    return os.path.join(path1, path2)


def read_image(path):
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)
