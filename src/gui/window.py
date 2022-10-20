import tkinter as tk
from tkinter import filedialog
from typing import Callable


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Augmentation System")
        self.geometry("600x400")
        self.resizable(False, False)

        self.input_folder = ""
        self.input_config = ""

        self.draw_input_folder_dialog_button()
        self.input_folder_label = tk.Label(self, text="No folder selected")
        self.input_folder_label.pack()

        self.draw_input_config_button()
        self.input_config_label = tk.Label(self, text="No config selected")
        self.input_config_label.pack()

    def draw_input_folder_dialog_button(self):
        open_input_folder_button = tk.Button(self, text="Select Input Folder", command=self.open_input_folder_dialog)
        open_input_folder_button.pack()

    def draw_input_config_button(self):
        input_config_button = tk.Button(self, text="Input Config", command=self.open_input_config_dialog)
        input_config_button.pack()

    def open_input_folder_dialog(self):
        self.input_folder = tk.filedialog.askdirectory()
        self.input_folder_label.config(text=self.input_folder)

    def open_input_config_dialog(self):
        self.input_config = tk.filedialog.askopenfilename()
        self.input_config_label.config(text=self.input_config)

    def set_process_button_click(self, process_button_callback: Callable[[str, str], None]):
        process_button = tk.Button(self, text="Process", command=lambda: process_button_callback(
            self.input_folder, self.input_config) if self.input_folder else None)
        process_button.pack()
