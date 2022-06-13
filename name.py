from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import describeYourGoal
from PIL import Image, ImageTk
import pandas as pd

# file lưu dữ liệu: my_mission.csv
mission_name = {'Type':[], 'Name':[], 'Deadline':[], 'Checkpoint':[]}

def name(type_of_the_mission):
    win = Tk()

    # MAIN 3: Name ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    # cấu hình của giao diện chính
    win.geometry("500x350+455+175")

    # set màu cho background
    win.config(bg="#404040")

    # khong cho phóng to màn hình
    #win.resizable(False, False)

    # xóa thanh navigate
    #win.overrideredirect(True)


    # MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    Label(win, text="Name", font=('Calibri', 24), width=30, bg="#404040", fg="#fff", anchor=CENTER).grid(column=1, row=1, columnspan = 3, pady=15)

    # MAIN ENTRY: trường nhập chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    # trường 1: [Name process] ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # nm: viết tắt của name

    Label(win, text="Name process: ",  font=("Calibri", 16), bg="#404040", fg="#fff",).grid(column=1, row=2, sticky=tk.W, padx=22)

    #tạo trường nhập
    nm = Image.open('Resource/Textbox/Textbox_name.png')
    nm = nm.resize((300, 45), Image.ANTIALIAS)
    name = ImageTk.PhotoImage(nm)
    name_label = Label(win, image = name, highlightthickness = 0, bd = 0)
    name_label.grid(column=2, row=2, columnspan=2) 

    # trường nhập của [name]
    name_of_mission = Entry(win, font=("Calibri", 16), bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0,)
    name_of_mission.grid(column=2, row=2, columnspan=2)

    # trường 2: [Deadline]

    Label(win, text="Deadline: ",  font=("Calibri", 16), bg="#404040", fg="#fff",).grid(column=1, row=3, sticky=tk.W, padx=22, pady=10)

    # DAY ----------------------------------------------------------------------------------------------------------------
    Label(win, text ="day", font=("Calibri", 12), bg="#404040", fg="#fff").grid(column=1, row=4, sticky=tk.W, padx=80, pady=10)

    #tạo trường nhập DAY
    d = Image.open('Resource/Textbox/Textbox_date.png')
    d = d.resize((50, 40), Image.ANTIALIAS)
    day = ImageTk.PhotoImage(d)
    Label(win, image = day, highlightthickness = 0, bd = 0).grid(column=1, row=4, sticky=tk.E, padx=10)

    # trường nhập của [day]
    day_deadline_of_mission = Entry(win, font=("Calibri", 16), width=2, bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0,)
    day_deadline_of_mission.grid(column=1, row=4, sticky=tk.E, padx=22)


    # MONTH ------------------------------------------------------------------------------------------------------------------
    Label(win, text ="month", font=("Calibri", 12), bg="#404040", fg="#fff").grid(column=2, row=4, sticky=tk.W)

    #tạo trường nhập MONTH
    m = Image.open('Resource/Textbox/Textbox_date.png')
    m = m.resize((50, 40), Image.ANTIALIAS)
    month = ImageTk.PhotoImage(m)
    Label(win, image = month, highlightthickness = 0, bd = 0).grid(column=2, row=4, sticky=tk.E, padx=30)

    # trường nhập của [month]
    month_deadline_of_mission = Entry(win, font=("Calibri", 16), width=2, bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0,)
    month_deadline_of_mission.grid(column=2, row=4, sticky=tk.E, padx=44)


    # YEAR ---------------------------------------------------------------------------------------------------------------------
    Label(win, text ="year", font=("Calibri", 12), bg="#404040", fg="#fff").grid(column=3, row=4, sticky=tk.W)

    #tạo trường nhập YEAR
    y = Image.open('Resource/Textbox/Textbox_date.png')
    y = y.resize((70, 40), Image.ANTIALIAS)
    year = ImageTk.PhotoImage(y)
    Label(win, image = year, highlightthickness = 0, bd = 0).grid(column=3, row=4, sticky=tk.E, padx=20)

    # trường nhập của [year]
    year_deadline_of_mission = Entry(win, font=("Calibri", 14), width=4, bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0,)
    year_deadline_of_mission.grid(column=3, row=4, sticky=tk.E, padx=33)


    # trường 3: [Checkpoint value] ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # cv: viết tắt của name

    Label(win, text="Checkpoint value: ",  font=("Calibri", 16), bg="#404040", fg="#fff",).grid(column=1, row=5, sticky=tk.E, pady=10)

    #tạo trường nhập
    cv = Image.open('Resource/Textbox/Textbox_name.png')
    cv = cv.resize((50, 45), Image.ANTIALIAS)
    checkpoint_value = ImageTk.PhotoImage(cv)
    Label(win, image = checkpoint_value, highlightthickness = 0, bd = 0).grid(column=2, row=5, columnspan=2, sticky=tk.W, pady=20) 

    # trường nhập của [checkpoint value]
    checkpoint_value_of_mission = Entry(win, font=("Calibri", 16), width=2, bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0,)
    checkpoint_value_of_mission.grid(column=2, row=5, columnspan=2, sticky=tk.W, padx=14, pady=20)

    Label(win, text="%",  font=("Calibri", 16), bg="#404040", fg="#fff",).grid(column=2, row=5, sticky=tk.W, padx=50, pady=20)

    def next_page():
        # xóa đi dữ liệu cũ
        mission_name['Type'] = []
        mission_name['Name'] = []
        mission_name['Deadline'] = []
        mission_name['Checkpoint'] = []

        # lấy dữ liệu từ trường nhập [Name]
        mission_name['Name'].append(name_of_mission.get())

        # lấy dữ liệu từ trường nhập [day] [month] [year]
        deadline = day_deadline_of_mission.get() + '/' + month_deadline_of_mission.get() + '/' + year_deadline_of_mission.get()
        mission_name['Deadline'].append(deadline)

        # lấy dữ liệu từ trường nhập [Checkpoint value]
        mission_name['Checkpoint'].append(checkpoint_value_of_mission.get())

        mission_name['Type'] = type_of_the_mission

        #chuyển giao diện tiếp theo
        win.destroy()
        describeYourGoal.ds(mission_name['Type'], mission_name['Name'], mission_name['Deadline'], mission_name['Checkpoint'])

    def npHover(event):
    # hình ảnh sẽ phản ánh

        # chưa hover
        if np_pic.get() == 'Resource/Buttons/Button_nextpage1.png':
            # sẽ đổi button sang trạng thái: đã hover
            np_pic.set('Resource/Buttons/Button_nextpage2.png')
            photo = PhotoImage(file=np_pic.get())
            next_page.config(image = photo)
            next_page.image = photo

        # đã hover
        else:
            # set button về trạng thái ban đầu
            np_pic.set('Resource/Buttons/Button_nextpage1.png')
            photo = PhotoImage(file=np_pic.get())
            next_page.config(image = photo)
            next_page.image = photo

    # tạo biến ảnh [Next page]
    np_pic = StringVar()
    np_pic.set('Resource/Buttons/Button_nextpage1.png')

    # hiển thị biến ảnh [Next page] ra màn hình
    np = PhotoImage(file=np_pic.get())
    next_page = Button(win, image = np, highlightthickness = 0, bd = 0, command=next_page, activebackground="#404040")
    next_page.grid(column=3, row=6, sticky =tk.E, padx=10)

    # chuột còn ở trên button
    next_page.bind('<Enter>', npHover)
    # chuột rời button
    next_page.bind('<Leave>', npHover)

    win.mainloop()
