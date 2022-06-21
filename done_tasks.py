from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

def taskHaveDone():
	main = Toplevel()

	# cấu hình của giao diện
	main.geometry("750x500+300+70")

	# set màu cho background
	main.config(bg="#fff")

	# khong cho phóng to màn hình
	main.resizable(False, False)

	# tiêu đề của cửa sổ
	main.title('What you have done...')

	# làm mờ cửa sổ
	main.attributes('-alpha', 0.95)

	# khai báo file csv mang dữ liệu chính
	my_to_do_list = pd.read_csv('my_todolist.csv')


	#Defining Background
	list_frame = Frame(main, bg = "#404040", width = 300, height = 500)
	list_frame.grid(column = 1, row = 1, sticky = tk.W)

	background = Canvas(list_frame, width=750, height=500, bg="#404040")
	background.grid(row=1, column=1)

	# tạo cuộn quay cho màn hình nếu dòng [mục đích] dài vượt qua [cấu hình] ban đầu của giao diện
	scroll_bar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=background.yview)
	scroll_bar.grid(row=1, column=1, sticky=tk.E, padx=10)

	background.configure(yscrollcommand=scroll_bar.set)

	second_frame = Frame(background, bg="#404040")
	background.create_window(0,0, window=second_frame)

	# ADDED
	second_frame.bind('<Configure>', lambda e: background.configure(scrollregion=background.bbox('all')))


	blanks = []
	circles = []
	types = []	
	names = []
	colors = []
	olives = []
	deadlines = []
	describes = []
	medals = []
	gems = []

	for done, name, mission_type, deadline, describe, gem in zip(my_to_do_list['Done'], my_to_do_list['Name'], my_to_do_list['Type'], my_to_do_list['Deadline'], my_to_do_list['Describe'], my_to_do_list['Checkpoint']):
	
		if done == False:
			continue

		if mission_type == 'process':
			photo_blank = Image.open('Resource/Blank/Red_blank.png')
			photo_blank = photo_blank.resize((680, 400), Image.ANTIALIAS)
			blank = ImageTk.PhotoImage(photo_blank)
			

			photo_circle = Image.open('Resource/Blank/red_circle.png')
			photo_circle = photo_circle.resize((80, 80), Image.ANTIALIAS)
			circle = ImageTk.PhotoImage(photo_circle)
			
			
			photo_type = Image.open('Resource/Blank/process_blank.png')
			photo_type = photo_type.resize((100, 35), Image.ANTIALIAS)
			type_of_mission = ImageTk.PhotoImage(photo_type)

			photo_medal = Image.open('Resource/Medals/process_medal.png')
			photo_medal = photo_medal.resize((45, 60), Image.ANTIALIAS)
			medal = ImageTk.PhotoImage(photo_medal)

			color = "#F36447"

		elif mission_type == 'skill':
			photo_blank = Image.open('Resource/Blank/Blue_blank.png')
			photo_blank = photo_blank.resize((680, 400), Image.ANTIALIAS)
			blank = ImageTk.PhotoImage(photo_blank)
			

			photo_circle = Image.open('Resource/Blank/blue_circle.png')
			photo_circle = photo_circle.resize((80, 80), Image.ANTIALIAS)
			circle = ImageTk.PhotoImage(photo_circle)
			
			
			photo_type = Image.open('Resource/Blank/skill_blank.png')
			photo_type = photo_type.resize((100, 35), Image.ANTIALIAS)
			type_of_mission = ImageTk.PhotoImage(photo_type)

			photo_medal = Image.open('Resource/Medals/skill_medal.png')
			photo_medal = photo_medal.resize((45, 60), Image.ANTIALIAS)
			medal = ImageTk.PhotoImage(photo_medal)

			color = "#558ED5"


		elif mission_type == 'daily':
			photo_blank = Image.open('Resource/Blank/Yellow_blank.png')
			photo_blank = photo_blank.resize((680, 400), Image.ANTIALIAS)
			blank = ImageTk.PhotoImage(photo_blank)
			

			photo_circle = Image.open('Resource/Blank/yellow_circle.png')
			photo_circle = photo_circle.resize((80, 80), Image.ANTIALIAS)
			circle = ImageTk.PhotoImage(photo_circle)
			
			
			photo_type = Image.open('Resource/Blank/daily_blank.png')
			photo_type = photo_type.resize((100, 35), Image.ANTIALIAS)
			type_of_mission = ImageTk.PhotoImage(photo_type)

			photo_medal = Image.open('Resource/Medals/daily_medal.png')
			photo_medal = photo_medal.resize((45, 60), Image.ANTIALIAS)
			medal = ImageTk.PhotoImage(photo_medal)
			
			color = "#EEC44C"

		photo_olive = Image.open('Resource/Blank/White_blank.png')
		photo_olive = photo_olive.resize((120, 35), Image.ANTIALIAS)
		olive = ImageTk.PhotoImage(photo_olive)

		blanks.append(blank)
		circles.append(circle)
		types.append(type_of_mission)
		names.append(name)
		colors.append(color)
		olives.append(olive)
		deadlines.append(deadline)
		describes.append(describe)
		medals.append(medal)
		gems.append(gem)

	photo_gem = Image.open('Resource/gem.png')
	photo_gem = photo_gem.resize((40, 40), Image.ANTIALIAS)
	gem = ImageTk.PhotoImage(photo_gem)

	coordinate_y = 50
	coordinate_x_STT = 88 # tùy vào độ dài của dãy số mới có thể quy được tọa độ
	coordinate_x_deadline = 539 # nếu dãy kí tự có tổng 8 kí tự thì tọa tại tọa độ này

	for i in range(len(blanks)):
		Label(second_frame, image = blanks[i], highlightthickness = 0, bd = 0, bg="#fff").grid(column=1,row=i+1, padx = 20, pady = 20)

		Label(second_frame, image = circles[i], highlightthickness = 0, bd = 0).place(x=60, y=coordinate_y)
		
		# số thứ tự của task
		if i >= 9:
			coordinate_x_STT = 78
		elif i >= 99:
			coordinate_x_STT = 68
		Label(second_frame, text = i+1, font=('Calibiri', 27, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040").place(x=coordinate_x_STT, y=coordinate_y+20)

		# tên của task
		Label(second_frame, text = names[i], font=('Calibiri', 18, 'bold'), highlightthickness = 0, bd = 0, bg=colors[i], fg="#fff").place(x=150, y=coordinate_y+10)

		# loại nhiệm vụ
		Label(second_frame, image = types[i], highlightthickness = 0, bd = 0).place(x=160, y=coordinate_y+60)

		# medal của nhiệm vụ
		Label(second_frame, image = medals[i], highlightthickness = 0, bd = 0, bg=colors[i]).place(x=270, y=coordinate_y+50)

		# gem của nhiệm vụ
		Label(second_frame, image = gem, highlightthickness = 0, bd = 0, bg=colors[i]).place(x=440, y=coordinate_y+60)
		# số gem
		Label(second_frame, text = gems[i], font=('Calibiri', 16, 'bold'), highlightthickness = 0, bd = 0, bg=colors[i], fg="#fff").place(x=480, y=coordinate_y+65)

		# deadline Label
		Label(second_frame, text = 'deadline', font=('Calibiri', 11), highlightthickness = 0, bd = 0, bg=colors[i], fg="#fff").place(x=551, y=coordinate_y+40)
		Label(second_frame, image = olives[i], highlightthickness = 0, bd = 0, bg=colors[i]).place(x=520, y=coordinate_y+60)

		# deadline
		if len(deadlines[i]) == 9:
			coordinate_x_deadline = 532
		elif len(deadlines[i]) == 10:
			coordinate_x_deadline = 530

		Label(second_frame, text = deadlines[i], font=('Calibiri', 15, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040").place(x=coordinate_x_deadline, y=coordinate_y+65)

		
		# miêu tả nhiệm vụ [describe]
		text = []
		s = ""
		for char in describes[i]:
			if char != '\n':
				s=s+char
			else:
				text.append(s)
				s = ""
		
		add  = 125
		for t in text:
			s = ""
			if len(t) > 65: # nếu như độ dài xâu có nhiều hơn 65 kí tự sẽ tạo xuống dòng
					dem = 65
					for char in range(0, 65):
						s+=t[char]
					for char in range(65, len(t)):
						if t[char] == " " and dem >= 65: # nếu một dòng dài hon 45 ki tu thi cho xuong dong
							s+='\n'
							dem=0
						else:
							s+=t[char]
							dem+=1
			else:
				s = t

			Label(second_frame, text = s, font=('Calibiri', 14), highlightthickness = 0, bd = 0, bg=colors[i], fg="#fff").place(x=60, y=coordinate_y+add)
			add += 50


		coordinate_y += 400 + 40



	main.mainloop()