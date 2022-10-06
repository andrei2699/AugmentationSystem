import tkinter as tk
from tkinter import filedialog
from typing import Callable


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Augmentation System")
        self.geometry("600x400")
        self.resizable(False, False)

        self.draw_input_folder_dialog_button()

        self.input_folder = ""

        self.input_folder_label = tk.Label(self, text="No folder selected")
        self.input_folder_label.pack()

    def draw_input_folder_dialog_button(self):
        open_input_folder_button = tk.Button(self, text="Select Input Folder", command=self.open_input_folder_dialog)
        open_input_folder_button.pack()

    def open_input_folder_dialog(self):
        self.input_folder = tk.filedialog.askdirectory()
        self.input_folder_label.config(text=self.input_folder)

    def set_process_button_click(self, process_button_callback: Callable[[str], None]):
        process_button = tk.Button(self, text="Process", command=lambda: process_button_callback(
            self.input_folder) if self.input_folder else None)
        process_button.pack()
