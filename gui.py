from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from hashes import Hashes
import hashlib

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
        self.upper_frame = None
        self.lower_frame = None
        self.configure_window()
        self.configure_upper_frame()
        self.configure_lower_frame()
        self.mainloop()

    def configure_window(self):
        self.title("Hash Value Comparison GUI")
        self.geometry("700x300")
        self.resizable(False, False)

    def configure_upper_frame(self):
        self.upper_frame = Frame(self, height=250)
        self.upper_frame.pack(fill=X, expand=True)
        self.upper_frame.grid_rowconfigure(0, weight=0, minsize=50)
        self.upper_frame.grid_rowconfigure(1, weight=0, minsize=50)
        self.upper_frame.grid_rowconfigure(2, weight=0, minsize=50)
        self.upper_frame.grid_rowconfigure(3, weight=0, minsize=50)
        self.upper_frame.grid_rowconfigure(4, weight=0, minsize=50)
        self.upper_frame_row0()
        self.upper_frame_row1()
        self.upper_frame_row2()
        self.upper_frame_row3()
        self.upper_frame_row4()

    def configure_lower_frame(self):
        self.lower_frame = Frame(self, height=50)
        self.lower_frame.pack(fill=X, expand=True)
        self.lower_frame.grid_rowconfigure(0, weight=1, minsize=50)
        self.lower_frame_row0()

    def upper_frame_row0(self):
        ref_hash_label = Label(self.upper_frame, text="Reference Hash:")
        ref_hash_label.grid(row=0, column=0, sticky="w", padx=10)
        self.ref_hash_entry = Entry(self.upper_frame, width=50)
        self.ref_hash_entry.grid(row=0, column=1)

    def upper_frame_row1(self):
        hash_alg_label = Label(self.upper_frame, text="Hash Algorithm:")
        hash_alg_label.grid(row=1, column=0, sticky="w", padx=10)
        self.hash_alg_list = ttk.Combobox(self.upper_frame, values=self.options, width=25)
        self.hash_alg_list.config(justify="center")
        self.hash_alg_list.grid(row=1, column=1, sticky="w")

    def upper_frame_row2(self):
        file_label = Label(self.upper_frame, text="File:")
        file_label.grid(row=2, column=0, sticky="w", padx=10)
        file_btn = Button(self.upper_frame, text="Select File", command=self.open_file)
        file_btn.grid(row=2, column=1, sticky="w")

    def upper_frame_row3(self):
        select_file_label = Label(self.upper_frame, text="Selected File:")
        select_file_label.grid(row=3, column=0, sticky="w", padx=10)
        self.file_info_label = Label(self.upper_frame, text="No File Selected Yet")
        self.file_info_label.grid(row=3, column=1, sticky="w")

    def upper_frame_row4(self):
        cmp_hash_btn = Button(self.upper_frame, text="Compare Hash Values", command=self.calculate_hash)
        cmp_hash_btn.grid(row=4, column=0, sticky="w", padx=10)

    def lower_frame_row0(self):
        self.result_label = Label(self.lower_frame, text="", foreground="red")
        self.result_label.grid(row=0, column=0, sticky="w", padx=10)

    def open_file(self):
        self.filepath = filedialog.askopenfilename()
        self.file_info_label.config(text=self.filepath)

    def calculate_hash(self):
        if not self.ref_hash_entry.get():
            self.result_label.config(text="Need A Reference Hash")
            return
        selected_algorithm = self.hash_alg_list.get()
        print(selected_algorithm)
        try:
            calculated_hash = self.hashes.get_file_hash(self.filepath, selected_algorithm)
        except ValueError:
            self.result_label.config(text="Hash or File Missing")
            return
        if self.ref_hash_entry.get() == calculated_hash:
            self.result_label.config(text=f"Hashes are equal\nCalculated Hash: {calculated_hash}")
        else:
            self.result_label.config(text=f"Hashes are NOT equal\nCalculated Hash: {calculated_hash}")
        print(calculated_hash)
