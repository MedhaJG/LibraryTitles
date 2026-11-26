import tkinter as tk

from gui import LibraryGUI
from search_index import SearchIndex


catalog = [
    "catalog",
    "catch",
    "catdog",
    "batdog",
    "catalog",
    "catlog",
    "catdog"
]

index = SearchIndex()
index.build_index(catalog)

root = tk.Tk()

app = LibraryGUI(root, index)

root.mainloop()