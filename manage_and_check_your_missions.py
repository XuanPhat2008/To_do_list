from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from mission_type import mt
import pandas as pd
#from create_to_do_list import Create_to_do_list
def main_1():
	win = Toplevel()

	# MAIN 1: Manage and check your missions ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# cấu hình của giao diện chính
	win.geometry("500x350+100+100")

	# set màu cho background
	win.config(bg="#404040")

	# khong cho phóng to màn hình
	win.resizable(False, False)

	win.columnconfigure(1, weight=1)



	# MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(win, text="Manage and check your missions", font=('Calibri', 24), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=1)
	# SUB TITLE: title phụ  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(win, text="there are so much things you have done", font=('Calibri', 14), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=2)



	# ẢNH MINH HỌA CHÍNH: chiếc Cúp ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	photo = Image.open('Resource/Cup.png')
	photo = photo.resize((160, 160), Image.ANTIALIAS)
	cup = ImageTk.PhotoImage(photo)
	Label(win, image = cup, highlightthickness = 0, bd = 0).grid(column=1, row=3, pady=20)



	# MAIN BUTTONS: hai button chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# [New process] --------------------------------------------------------------------------------------------------------------------------------------
	# np viết tắt của: new process

	# Hoạt động chính của button [New process]

	# hoạt động 1: khi chuột hover vào button
	def npHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if np_pic.get() == 'Resource/Buttons/Button_newprocess1.png':
			# sẽ đổi button sang trạng thái: đã hover
			np_pic.set('Resource/Buttons/Button_newprocess2.png')
			photo = PhotoImage(file=np_pic.get())
			new_process.config(image = photo)
			new_process.image = photo

		# đã hover
		else:
			# set button về trạng thái ban đầu
			np_pic.set('Resource/Buttons/Button_newprocess1.png')
			photo = PhotoImage(file=np_pic.get())
			new_process.config(image = photo)
			new_process.image = photo


	# hoạt động 2: khi chuột ấn vào button [New process]
	def npEvent():
		mt()

	# tạo biến ảnh [New process]
	np_pic = StringVar()
	np_pic.set('Resource/Buttons/Button_newprocess1.png')

	# hiển thị biến ảnh [New process] ra màn hình
	np = PhotoImage(file=np_pic.get())
	new_process = Button(win, image = np, highlightthickness = 0, bd = 0, command=npEvent, activebackground="#404040")
	new_process.grid(column=1, row=4, sticky =tk.W, padx=100)

	# chuột còn ở trên button
	new_process.bind('<Enter>', npHover)
	# chuột rời button
	new_process.bind('<Leave>', npHover)


	# [Check what you have done] --------------------------------------------------------------------------------------------------------------------------------------
	# cwyhd viết tắt của: check what you have done

	# Hoạt động chính của button [Check what you have done]

	# hoạt động 1: khi chuột hover vào button
	def cwyhdHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if cwyhd_pic.get() == 'Resource/Buttons/Button_cwyhd1.png':
			# sẽ đổi button sang trạng thái: đã hover
			cwyhd_pic.set('Resource/Buttons/Button_cwyhd2.png')
			photo = PhotoImage(file=cwyhd_pic.get())
			check_what_you_have_done.config(image = photo)
			check_what_you_have_done.image = photo

		# đã hover
		else:
			# set button về trạng thái ban đầu
			cwyhd_pic.set('Resource/Buttons/Button_cwyhd1.png')
			photo = PhotoImage(file=cwyhd_pic.get())
			check_what_you_have_done.config(image = photo)
			check_what_you_have_done.image = photo


	# hoạt động 2: khi chuột ấn vào button [Check what you have done]
	def cwyhdEvent():
		messagebox.showinfo(message="Tính năng này sẽ được cải thiện sau")


	# tạo biến ảnh [Check what you have done]
	cwyhd_pic = StringVar()
	cwyhd_pic.set('Resource/Buttons/Button_cwyhd1.png')

	# hiển thị biến ảnh [Check what you have done] ra màn hình
	cwyhd = PhotoImage(file=cwyhd_pic.get())
	check_what_you_have_done = Button(win, image = cwyhd, highlightthickness = 0, bd = 0, command=cwyhdEvent, activebackground="#404040")
	check_what_you_have_done.grid(column=1, row=4, sticky=tk.E, padx=100)

	# chuột còn ở trên button
	check_what_you_have_done.bind('<Enter>', cwyhdHover)
	# chuột rời button
	check_what_you_have_done.bind('<Leave>', cwyhdHover)



	win.mainloop()