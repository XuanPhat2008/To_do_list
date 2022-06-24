from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkmagicgrid import *
import io
import csv

def show_detail_csv():
    # Create a root window
    root = Toplevel()

    # khong cho phóng to màn hình
    root.resizable(False, False)

    # tiêu đề của cửa sổ
    root.title('Details')

    #Defining Background
    list_frame = Frame(root, bg = "#fff", width = 300, height = 500)
    list_frame.grid(column = 1, row = 1, sticky = tk.W)

    background = Canvas(list_frame, width=980, height=500, bg="#fff")
    background.grid(row=1, column=1)

    # tạo cuộn quay cho màn hình nếu dòng [mục đích] dài vượt qua [cấu hình] ban đầu của giao diện
    scroll_bar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=background.yview)
    scroll_bar.grid(row=1, column=2, sticky=N+S+W, padx=5)

    background.configure(yscrollcommand=scroll_bar.set)

    second_frame = Frame(background, bg="#fff")
    background.create_window(0,0, window=second_frame)

    # ADDED
    second_frame.bind('<Configure>', lambda e: background.configure(scrollregion=background.bbox('all')))


    # Create a MagicGrid widget
    grid = MagicGrid(second_frame)
    grid.pack()

    # Display the contents of some CSV file
    # (note this is not a particularly efficient viewer)
    with io.open("my_todolist.csv", "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        parsed_rows = 0
        for row in reader:
            if parsed_rows == 0:
                # Display the first row as a header
                grid.add_header(*row)
            else:
                grid.add_row(*row)
            parsed_rows += 1

    # Start Tk's event loop
    root.mainloop()
