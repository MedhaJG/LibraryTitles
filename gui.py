import tkinter as tk
from tkinter import messagebox


class LibraryGUI:

    def __init__(self, root, index):

        self.index = index
        self.root = root

        root.title("Library Partial Title Retrieval")
        root.geometry("500x350")

        tk.Label(
            root,
            text="Prefix"
        ).pack(pady=5)

        self.prefix_entry = tk.Entry(root, width=30)
        self.prefix_entry.pack()

        tk.Label(
            root,
            text="Suffix"
        ).pack(pady=5)

        self.suffix_entry = tk.Entry(root, width=30)
        self.suffix_entry.pack()

        tk.Button(
            root,
            text="Search",
            command=self.search
        ).pack(pady=15)

        self.result_text = tk.Text(
            root,
            height=10,
            width=50
        )

        self.result_text.pack()

    def search(self):

        prefix = self.prefix_entry.get().strip()
        suffix = self.suffix_entry.get().strip()

        if not prefix or not suffix:

            messagebox.showerror(
                "Error",
                "Prefix and suffix cannot be empty."
            )
            return

        record = self.index.search(prefix, suffix)

        self.result_text.delete(1.0, tk.END)

        if record:

            output = (
                f"Prefix: {prefix}\n"
                f"Suffix: {suffix}\n\n"
                f"Matched Record: {record.title}\n"
                f"Record ID: {record.id}"
            )

        else:

            output = (
                f"Prefix: {prefix}\n"
                f"Suffix: {suffix}\n\n"
                f"No Match Found"
            )

        self.result_text.insert(tk.END, output)
