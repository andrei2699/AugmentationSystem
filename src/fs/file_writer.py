import os


def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


class FileWriter:
    def __init__(self, output_folder_path):
        self.output_folder_path = output_folder_path
        self.current_index = 1

    def write(self, file_name, data):
        file_path = os.path.join(self.output_folder_path, file_name + "_" + str(self.current_index) + ".jpg")

        ensure_path_exists(file_path)

        with open(file_path, 'w') as f:
            f.write(data)

        self.current_index += 1
