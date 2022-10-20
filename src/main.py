from src.augmentation.algorithms_settings import load_algorithm_settings
from src.fs.file_reader import get_files_with_extension, combine_paths, read_image
from src.fs.file_writer import FileWriter
from src.gui.window import Window


def process_button_click(input_folder: str, settings_path: str):
    algorithm_settings = load_algorithm_settings(settings_path)

    output_folder = input_folder + "_aug"

    file_writer = FileWriter(output_folder)

    # TODO Check order of created files
    for name, extension in get_files_with_extension(input_folder):
        for algorithm in algorithm_settings.algorithms:
            file_name = name + "_" + algorithm.get_name()
            image = read_image(combine_paths(input_folder, name + extension))
            image = image.astype(float)

            apply_image = algorithm.apply(image)

            apply_image = apply_image.astype('uint8')
            file_writer.write(file_name, apply_image)


def main():
    # process_button_click(input_folder, algorithm_settings_path)
    window = Window()
    window.set_process_button_click(
        lambda input_folder, input_config: process_button_click(input_folder, input_config))
    window.mainloop()


if __name__ == '__main__':
    main()
