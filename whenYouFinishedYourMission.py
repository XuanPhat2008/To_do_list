from subprocess import call
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def wyfym():
	win = Tk()

	# MAIN 4: When you finished your missions ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# cấu hình của giao diện chính
	win.geometry("500x350+455+175")

	# set màu cho background
	win.config(bg="#404040")

	# khong cho phóng to màn hình
	#win.resizable(False, False)

	# xóa thanh navigate
	#win.overrideredirect(True)



	# MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(win, text="When you finished your mission", font=('Calibri', 24), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=1)
	# SUB TITLE: title phụ  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(win, text="click on Done to get Checkpoint", font=('Calibri', 14), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=2)



	# ẢNH MINH HỌA CHÍNH: chiếc laptop với các objects xung quanh~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	photo = Image.open('Resource/Illustate.png')
	photo = photo.resize((300, 250), Image.ANTIALIAS)
	cup = ImageTk.PhotoImage(photo)
	Label(win, image = cup, highlightthickness = 0, bd = 0).grid(column=1, row=3, sticky=tk.N)



	# MAIN BUTTON: một button chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# [Done] --------------------------------------------------------------------------------------------------------------------------------------
	# dn viết tắt của: done

	# Hoạt động chính của button [Done]

	# hoạt động 1: khi chuột hover vào button
	def dnHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if dn_pic.get() == 'Resource/Buttons/Button_done1.png':
			# sẽ đổi button sang trạng thái: đã hover
			dn_pic.set('Resource/Buttons/Button_done2.png')
			dn = Image.open(dn_pic.get())
			dn = dn.resize((70, 30), Image.ANTIALIAS)
			done_pic = ImageTk.PhotoImage(dn)
			done.config(image = done_pic)
			done.image = done_pic

		# đã hover
		else:
			# set button về trạng thái ban đầu
			dn_pic.set('Resource/Buttons/Button_done1.png')
			dn = Image.open(dn_pic.get())
			dn = dn.resize((70, 30), Image.ANTIALIAS)
			done_pic = ImageTk.PhotoImage(dn)
			done.config(image = done_pic)
			done.image = done_pic


	# hoạt động 2: khi chuột ấn vào button [New process]
	def dnEvent():
		win.destroy()
		messagebox.showinfo(message="To do list của bạn đã được lưu lại, quay về màn hình chính")


	# tạo biến ảnh [done]
	dn_pic = StringVar()
	dn_pic.set('Resource/Buttons/Button_done1.png')

	# hiển thị biến ảnh [done] ra màn hình
	dn = Image.open(dn_pic.get())
	dn = dn.resize((70, 30), Image.ANTIALIAS)
	done_pic = ImageTk.PhotoImage(dn)
	done = Button(win, image = done_pic, highlightthickness = 0, bd = 0, command=dnEvent, activebackground="#404040")
	done.grid(column=1, row=3, sticky=tk.NW, padx=210, pady=120)

	# chuột còn ở trên button
	done.bind('<Enter>', dnHover)
	# chuột rời button
	done.bind('<Leave>', dnHover)


	win.mainloop()