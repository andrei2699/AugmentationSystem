from pathlib import Path
import os
import cv2


def ensure_path_exists(path):
    parent_path = Path(path).parent
    if not os.path.exists(parent_path):
        os.makedirs(parent_path)


class FileWriter:
    def __init__(self, output_folder_path):
        self.output_folder_path = output_folder_path
        self.current_index = 1

    def write(self, file_name, data):
        file_path = os.path.join(self.output_folder_path, file_name + "_" + str(self.current_index) + ".jpg")

        ensure_path_exists(file_path)

        cv2.imwrite(file_path, data)

        self.current_index += 1
