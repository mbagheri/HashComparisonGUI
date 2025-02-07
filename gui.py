from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from hashes import Hashes
import hashlib

# Adjust window and divide into 2 frames, so long error messages don't affect the rendering
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.hashes = Hashes()
        self.file_info_label = None
        self.hash_alg_list = None
        self.filepath = None
        self.ref_hash_entry = None
        self.result_label = None
        self.options = []
        for algo in hashlib.algorithms_available:
            self.options.append(algo)
        self.configure_window()
        self.configure_rows()
        self.configure_row0()
        self.configure_row1()
        self.configure_row2()
        self.configure_row3()
        self.configure_row4()
        self.configure_row5()
        self.mainloop()

    def configure_window(self):
        self.title("Hash Value Comparison GUI")
        self.geometry("700x300")
        self.resizable(False, False)

    def configure_rows(self):
        self.grid_rowconfigure(0, weight=0, minsize=50)
        self.grid_rowconfigure(1, weight=0, minsize=50)
        self.grid_rowconfigure(2, weight=0, minsize=50)
        self.grid_rowconfigure(3, weight=0, minsize=50)
        self.grid_rowconfigure(4, weight=0, minsize=50)
        self.grid_rowconfigure(5, weight=0, minsize=50)

    def configure_row0(self):
        ref_hash_label = Label(self, text="Reference Hash:")
        ref_hash_label.grid(row=0, column=0, sticky="w", padx=10)
        self.ref_hash_entry = Entry(self, width=50)
        self.ref_hash_entry.grid(row=0, column=1)

    def configure_row1(self):
        hash_alg_label = Label(self, text="Hash Algorithm:")
        hash_alg_label.grid(row=1, column=0, sticky="w", padx=10)
        self.hash_alg_list = ttk.Combobox(self, values=self.options, width=25)
        self.hash_alg_list.config(justify="center")
        self.hash_alg_list.grid(row=1, column=1, sticky="w")

    def configure_row2(self):
        file_label = Label(self, text="File:")
        file_label.grid(row=2, column=0, sticky="w", padx=10)
        file_btn = Button(self, text="Select File", command=self.open_file)
        file_btn.grid(row=2, column=1, sticky="w")

    def configure_row3(self):
        select_file_label = Label(self, text="Selected File:")
        select_file_label.grid(row=3, column=0, sticky="w", padx=10)
        self.file_info_label = Label(self, text="No File Selected Yet")
        self.file_info_label.grid(row=3, column=1, sticky="w")

    def configure_row4(self):
        cmp_hash_btn = Button(self, text="Compare Hash Values", command=self.calculate_hash)
        cmp_hash_btn.grid(row=4, column=0, sticky="w", padx=10)

    def configure_row5(self):
        self.result_label = Label(self, text="Test", foreground="red")
        self.result_label.grid(row=5, column=0, sticky="w", padx=10)

    def open_file(self):
        self.filepath = filedialog.askopenfilename()
        self.file_info_label.config(text=self.filepath)

    def calculate_hash(self):
        if not self.ref_hash_entry.get():
            self.result_label.config(text="Need Reference Hash")
            return
        selected_algorithm = self.hash_alg_list.get()
        print(selected_algorithm)
        try:
            calculated_hash = self.hashes.get_file_hash(self.filepath, selected_algorithm)
        except ValueError:
            self.result_label.config(text="Hash or File Missing")
            return
        if self.ref_hash_entry.get() == calculated_hash:
            #self.result_label.config(text=f"Calculated Hash: {calculated_hash}\nHashes are equal")
            self.result_label.config(text="Hashes are equal")
        else:
            self.result_label.config(text="Hashes NOT equal")
        print(calculated_hash)
