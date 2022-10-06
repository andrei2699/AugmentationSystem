from src.augmentation.algorithms_settings import load_algorithm_settings
from src.fs.file_reader import get_files_with_extension, combine_paths, read_image
from src.fs.file_writer import FileWriter
from src.gui.window import Window

# Todo add a button to the window to open a dialog to select the input algorithm_settings_path
algorithm_settings_path = "test/test_augmentation/test_data/identity_algorithm.yaml"


def process_button_click(input_folder: str, settings_path: str):
    algorithm_settings = load_algorithm_settings(settings_path)

    output_folder = input_folder + "_aug"

    file_writer = FileWriter(output_folder)

    for name, extension in get_files_with_extension(input_folder):
        for algorithm in algorithm_settings.algorithms:
            file_name = name + "_" + algorithm.get_name()
            image = read_image(combine_paths(input_folder, name + extension))

            file_writer.write(file_name, algorithm.apply(image))


if __name__ == '__main__':
    # process_button_click(input_folder, algorithm_settings_path)
    window = Window()
    window.set_process_button_click(lambda input_folder: process_button_click(input_folder, algorithm_settings_path))
    window.mainloop()
