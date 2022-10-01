import tkinter as tk
from tkinter import filedialog


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
