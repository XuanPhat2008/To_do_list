from tkinter import *
import tkinter as tk
import name
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

# file lưu dữ liệu: my_mission.csv
mission_type = {'Type':[]}

def mt():
	win = Tk()

	# xóa đi dữ liệu cũ
	mission_type['Type'] = []
	
	# MAIN 2: Mission type ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# cấu hình của giao diện chính
	win.geometry("500x350+455+175")

	# set màu cho background
	win.config(bg="#404040")

	# khong cho phóng to màn hình
	win.resizable(False, False)

	# tiêu đề của cửa sổ
	win.title('Pick the type of mission')

	win.columnconfigure(1, weight=1)

	# xóa thanh navigate
	#win.overrideredirect(True)


	# MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(win, text="Mission type", font=('Calibri', 24), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=1, pady=30)



	# MAIN BUTTONS: 3 Checkbox chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# [process] --------------------------------------------------------------------------------------------------------------------------------------
	# p viết tắt của: process

	# Hoạt động chính của checkbox [process]

	# hoạt động 1: khi click chuột vào checkbox
	def pEvent():
		# hình ảnh sẽ phản ánh

		# chưa click
		if p_pic.get() == 'Resource/Buttons/Checkbox1.png':
			# sẽ đổi checkbox sang trạng thái: đã click
			p_pic.set('Resource/Buttons/Checkbox2.png')
			photo = PhotoImage(file=p_pic.get())
			process.config(image = photo)
			process.image = photo
			mission_type['Type'].append('process')
			print(mission_type)

		# đã click
		else:
			# set checkbox về trạng thái ban đầu
			p_pic.set('Resource/Buttons/Checkbox1.png')
			photo = PhotoImage(file=p_pic.get())
			process.config(image = photo)
			process.image = photo
			mission_type['Type'].remove('process')
			print(mission_type)


	# tạo biến ảnh [process]
	p_pic = StringVar()
	p_pic.set('Resource/Buttons/Checkbox1.png')

	# hiển thị biến ảnh [process] ra màn hình
	p = PhotoImage(file=p_pic.get())
	process = Button(win, image = p, highlightthickness = 0, bd = 0, command=pEvent, activebackground="#404040")
	process.grid(column=1, row=2, sticky=tk.W, padx=50, pady=10)

	# hiểu thị label: process
	Label(win, text="process", font=("Calibri", 20), bg="#404040", fg="#fff").grid(column=1, row=2, sticky=tk.W, padx=120, pady=10)


	# [skill] --------------------------------------------------------------------------------------------------------------------------------------
	# s viết tắt của: skill

	# Hoạt động chính của checkbox [skill]

	# hoạt động 1: khi click chuột vào checkbox
	def sEvent():
		# hình ảnh sẽ phản ánh

		# chưa click
		if s_pic.get() == 'Resource/Buttons/Checkbox1.png':
			# sẽ đổi checkbox sang trạng thái: đã click
			s_pic.set('Resource/Buttons/Checkbox2.png')
			photo = PhotoImage(file=s_pic.get())
			skill.config(image = photo)
			skill.image = photo
			mission_type['Type'].append('skill')
			print(mission_type)

		# đã click
		else:
			# set checkbox về trạng thái ban đầu
			s_pic.set('Resource/Buttons/Checkbox1.png')
			photo = PhotoImage(file=s_pic.get())
			skill.config(image = photo)
			skill.image = photo
			mission_type['Type'].remove('skill')
			print(mission_type)


	# tạo biến ảnh [skill]
	s_pic = StringVar()
	s_pic.set('Resource/Buttons/Checkbox1.png')

	# hiển thị biến ảnh [skill] ra màn hình
	s = PhotoImage(file=s_pic.get())
	skill = Button(win, image = s, highlightthickness = 0, bd = 0, command=sEvent, activebackground="#404040")
	skill.grid(column=1, row=3, sticky=tk.W, padx=50, pady=10)

	# hiểu thị label: process
	Label(win, text="skill", font=("Calibri", 20), bg="#404040", fg="#fff").grid(column=1, row=3, sticky=tk.W, padx=120, pady=10)


	# [daily] --------------------------------------------------------------------------------------------------------------------------------------
	# d viết tắt của: daily

	# Hoạt động chính của checkbox [daily]

	# hoạt động 1: khi click chuột vào checkbox
	def dEvent():
		# hình ảnh sẽ phản ánh

		# chưa click
		if d_pic.get() == 'Resource/Buttons/Checkbox1.png':
			# sẽ đổi checkbox sang trạng thái: đã click
			d_pic.set('Resource/Buttons/Checkbox2.png')
			photo = PhotoImage(file=d_pic.get())
			daily.config(image = photo)
			daily.image = photo
			mission_type['Type'].append('daily')
			print(mission_type)

		# đã click
		else:
			# set checkbox về trạng thái ban đầu
			d_pic.set('Resource/Buttons/Checkbox1.png')
			photo = PhotoImage(file=d_pic.get())
			daily.config(image = photo)
			daily.image = photo
			mission_type['Type'].remove('daily')
			print(mission_type)


	# tạo biến ảnh [daily]
	d_pic = StringVar()
	d_pic.set('Resource/Buttons/Checkbox1.png')

	# hiển thị biến ảnh [daily] ra màn hình
	d = PhotoImage(file=d_pic.get())
	daily = Button(win, image = d, highlightthickness = 0, bd = 0, command=dEvent, activebackground="#404040")
	daily.grid(column=1, row=4, sticky=tk.W, padx=50, pady=10)

	# hiểu thị label: daily
	Label(win, text="daily", font=("Calibri", 20), bg="#404040", fg="#fff").grid(column=1, row=4, sticky=tk.W, padx=120, pady=10)

	def next_page():
		#chuyển giao diện tiếp theo
		win.destroy()
		name.name(mission_type['Type'])

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
	next_page.grid(column=1, row=5, sticky =tk.E, padx=20)

	# chuột còn ở trên button
	next_page.bind('<Enter>', npHover)
	# chuột rời button
	next_page.bind('<Leave>', npHover)


	win.mainloop()
