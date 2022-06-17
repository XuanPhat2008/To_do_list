from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mission_type
import timer
import pandas as pd
import random

def App():
	main = Tk()

	# cấu hình của giao diện chính
	main.geometry("1100x600+150+50")

	# set màu cho background
	main.config(bg="#404040")

	# khong cho phóng to màn hình
	main.resizable(False, False)

	# khai báo file csv mang dữ liệu chính
	my_to_do_list = pd.read_csv('my_todolist.csv')

	# khai báo file csv mang dữ liệu người dùng về [Level] và [Gem]
	your_experiments = pd.read_csv('your_experiments.csv')
	level_file = pd.read_csv('level.csv')


	# DÒNG 1

	# tạo frame 1: title
	title_frame = Frame(main, bg="#404040", width= 1100, height=100)
	title_frame.grid(column = 1, row = 1, columnspan = 3)


	# DÒNG 2
	# tạo FRAME THỨ 1: Tạo report ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

	report_frame = Frame(main, bg="white", width = 300, height = 350)
	report_frame.grid(column = 1, row = 2, sticky = tk.W)

		# các biến lưu lại thông tin

	# biến lưu lại [Level] ------------------
	number_of_level = StringVar()
	number_of_level.set('0')
	
	# biến lưu lại [Gem] --------------------
	number_of_gem = StringVar()
	number_of_gem.set('0')

	# biến lưu lại [Experiments]
	number_of_experiments = StringVar()
	number_of_experiments.set('0')

	# biến lưu lại số lượng task về [Process]
	number_of_process = StringVar()
	number_of_process.set('0')
	
	# biến lưu lại số lượng task về [Skill]
	number_of_skill = StringVar()
	number_of_skill.set('0')
	
	# biến lưu lại số lượng task về [Daily]
	number_of_daily = StringVar()
	number_of_daily.set('0')

	# biến lưu lại tổng số tasks đã hoàn thành
	number_of_tasks = StringVar()
	number_of_tasks.set('0')

	# lấy số liệu về các tasks
	for missionType, missionProcess in zip(my_to_do_list['Type'], my_to_do_list['Done']):
		# nếu nhiệm vụ nào chưa hoàn thành sẽ khong tính
		if missionProcess == False:
			continue

		if missionType == 'process':
			so = str(int(number_of_process.get()) + 1)
			number_of_process.set(so)

			so = str(int(number_of_tasks.get()) + 1)
			number_of_tasks.set(so)

		elif missionType == 'skill':
			so = str(int(number_of_skill.get()) + 1)
			number_of_skill.set(so)

			so = str(int(number_of_tasks.get()) + 1)
			number_of_tasks.set(so)

		elif missionType == 'daily':
			so = str(int(number_of_daily.get()) + 1)
			number_of_daily.set(so)

			so = str(int(number_of_tasks.get()) + 1)
			number_of_tasks.set(so)

	# lấy số liệu về Level và Gem trong file csv [your_experiments.csv]

	# [Level]
	number_of_level.set(str(your_experiments['Level'].iloc[0]))
	
	# [Gem]
	number_of_gem.set(str(your_experiments['Gem'].iloc[0]))



	# hiển thị Level --------------------------------------------------------------------------------------------------------
	Label(report_frame, text="Level", font=('Courier New', 20, "bold"), bg="#fff", fg="#404040").place(x=15, y=10)

	level = Label(report_frame, text= number_of_level.get(), font=('Courier New', 20, "bold"), bg="#fff", fg="#404040")
	level.place(x=110, y=10)


	# hiển thị kinh nghiệm --------------------------------------------------------------------------------------------------------
	#Label(report_frame, text="300/1000", font=('Courier New', 10), bg="#fff").place(x=45, y=40)


	# line ngăn cách --------------------------------------------------------------------------------------------------------
	photo_line_white = Image.open('Resource/line_white.png')
	photo_line_white = photo_line_white.resize((15, 40), Image.ANTIALIAS)
	line_white = ImageTk.PhotoImage(photo_line_white)
	Label(report_frame, image = line_white, highlightthickness = 0, bd = 0, bg="#fff", fg="#404040").place(x=146, y=8)


	# hiển thị biểu tượng Gem -----------------------------------------------------------------------------------------------
	photo_gem = Image.open('Resource/Gem.png')
	photo_gem = photo_gem.resize((40, 40), Image.ANTIALIAS)
	gem = ImageTk.PhotoImage(photo_gem)
	Label(report_frame, image = gem, highlightthickness = 0, bd = 0, bg="#fff", fg="#404040").place(x=170, y=8)

	
	# hiển thị số Gem -------------------------------------------------------------------------------------------------------
	gem_text = Label(report_frame, text = number_of_gem.get(), font=('Vogue', 20, 'bold'), bg="#fff", fg="#404040")
	gem_text.place(x=220, y=10)

# -------------------------------------------------------------------------------------------------------------------

	def getHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if get_pic.get() == 'Resource/Buttons/Button_get1.png':
			# sẽ đổi button sang trạng thái: đã hover
			get_pic.set('Resource/Buttons/Button_get2.png')
			get = PhotoImage(file=get_pic.get())
			get_button.config(image = get)
			get_button.image = get

		# đã hover
		else:
			# set button về trạng thái ban đầu
			get_pic.set('Resource/Buttons/Button_get1.png')
			get = PhotoImage(file=get_pic.get())
			get_button.config(image = get)
			get_button.image = get

	# chuyển hướng đế giao diện tạo nhiệm vụ mới
	def getEvent():
		main.destroy()
		mission_type.mt()

	# hiển thị button [Get]
	# tạo biến ảnh [Get]
	get_pic = StringVar()
	get_pic.set('Resource/Buttons/Button_get1.png')

	# hiển thị biến ảnh [Get] ra màn hình
	photo_get = Image.open(get_pic.get())
	#photo_get = photo_get.resize((60, 25), Image.ANTIALIAS)
	get = ImageTk.PhotoImage(photo_get)
	get_button = Button(report_frame, image = get, command = getEvent, highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	get_button.place(x=150, y=55)


	# chuột còn ở trên button
	get_button.bind('<Enter>', getHover)
	# chuột rời button
	get_button.bind('<Leave>', getHover)

# -------------------------------------------------------------------------------------------------------------------

	def dailyBoxHover(event):
	# hình ảnh sẽ phản ánh

		# chưa hover
		if dailyBox_pic.get() == 'Resource/Buttons/Button_dailyBox1.png':
			# sẽ đổi button sang trạng thái: đã hover
			dailyBox_pic.set('Resource/Buttons/Button_dailyBox2.png')
			dailyBox = PhotoImage(file=dailyBox_pic.get())
			dailyBox_button.config(image = dailyBox)
			dailyBox_button.image = dailyBox

		# đã hover
		else:
			# set button về trạng thái ban đầu
			dailyBox_pic.set('Resource/Buttons/Button_dailyBox1.png')
			dailyBox = PhotoImage(file=dailyBox_pic.get())
			dailyBox_button.config(image = dailyBox)
			dailyBox_button.image = dailyBox

	def dailyBoxEvent():
		timer.dailybox()


	# hiển thị button [Daily box]
	# tạo biến ảnh [Daily box]
	dailyBox_pic = StringVar()
	dailyBox_pic.set('Resource/Buttons/Button_dailyBox1.png')

	# hiển thị biến ảnh [Daily box] ra màn hình
	photo_dailyBox = Image.open(dailyBox_pic.get())
	dailyBox = ImageTk.PhotoImage(photo_dailyBox)
	dailyBox_button = Button(report_frame, image = dailyBox, command = dailyBoxEvent, highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	dailyBox_button.place(x=215, y=55)


	# chuột còn ở trên button
	dailyBox_button.bind('<Enter>', dailyBoxHover)
	# chuột rời button
	dailyBox_button.bind('<Leave>', dailyBoxHover)

# -------------------------------------------------------------------------------------------------------------------

	def gameHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if game_pic.get() == 'Resource/Buttons/Button_game1.png':
			# sẽ đổi button sang trạng thái: đã hover
			game_pic.set('Resource/Buttons/Button_game2.png')
			game = PhotoImage(file=game_pic.get())
			game_button.config(image = game)
			game_button.image = game

		# đã hover
		else:
			# set button về trạng thái ban đầu
			game_pic.set('Resource/Buttons/Button_game1.png')
			game = PhotoImage(file=game_pic.get())
			game_button.config(image = game)
			game_button.image = game

	# chuyển hướng đế giao diện tạo nhiệm vụ mới
	def getEvent():
		main.destroy()
		mission_type.mt()

	# hiển thị button [Get]
	# tạo biến ảnh [Get]
	game_pic = StringVar()
	game_pic.set('Resource/Buttons/Button_game1.png')

	# hiển thị biến ảnh [Get] ra màn hình
	photo_game = Image.open(game_pic.get())
	game = ImageTk.PhotoImage(photo_game)
	game_button = Button(report_frame, image = game, command = getEvent, highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	game_button.place(x=209, y=295)


	# chuột còn ở trên button
	game_button.bind('<Enter>', gameHover)
	# chuột rời button
	game_button.bind('<Leave>', gameHover)

# -------------------------------------------------------------------------------------------------------------------


	# hiển thị các huân chương

	# huân chương [Process] =========================================================================================================
	photo_processmedal = Image.open('Resource/Medals/process_medal.png')
	photo_processmedal = photo_processmedal.resize((45, 60), Image.ANTIALIAS)
	processmedal = ImageTk.PhotoImage(photo_processmedal)
	Label(report_frame, image = processmedal, highlightthickness = 0, bd = 0, bg="#fff").place(x=10, y=100)

	processmedal_text1 = Label(report_frame, text = number_of_process.get(), font = ("Calibri", 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	processmedal_text1.place(x=60, y=110)

	# Red cube
	photo_red = Image.open('Resource/Red.png')
	photo_red = photo_red.resize((20, 20), Image.ANTIALIAS)
	red = ImageTk.PhotoImage(photo_red)
	Label(report_frame, image = red, highlightthickness = 0, bd = 0, bg="#fff").place(x=20, y=190)

	Label(report_frame, text = "process", font = ('Calibri', 15), highlightthickness = 0, bd = 0, bg="#fff").place(x=50, y=185)


	processmedal_text2 = Label(report_frame, text = number_of_process.get(), font = ('Calibri', 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	processmedal_text2.place(x=140, y=183)


	# huân chương [Skill] ===========================================================================================================
	photo_skillmedal = Image.open('Resource/Medals/skill_medal.png')
	photo_skillmedal = photo_skillmedal.resize((45, 60), Image.ANTIALIAS)
	skillmedal = ImageTk.PhotoImage(photo_skillmedal)
	Label(report_frame, image = skillmedal, highlightthickness = 0, bd = 0, bg="#fff").place(x=100, y=100)

	skillmedal_text1 = Label(report_frame, text = number_of_skill.get(), font = ("Calibri", 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	skillmedal_text1.place(x=150, y=110)

	# Blue cube
	photo_blue = Image.open('Resource/Blue.png')
	photo_blue = photo_blue.resize((20, 20), Image.ANTIALIAS)
	blue = ImageTk.PhotoImage(photo_blue)
	Label(report_frame, image = blue, highlightthickness = 0, bd = 0, bg="#fff").place(x=20, y=240)

	Label(report_frame, text = "skill", font = ('Calibri', 15), highlightthickness = 0, bd = 0, bg="#fff").place(x=50, y=235)


	skillmedal_text2 = Label(report_frame, text = number_of_skill.get(), font = ('Calibri', 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	skillmedal_text2.place(x=140, y=233)



	# huân chương [Daily] ===========================================================================================================
	photo_dailymedal = Image.open('Resource/Medals/daily_medal.png')
	photo_dailymedal = photo_dailymedal.resize((45, 60), Image.ANTIALIAS)
	dailymedal = ImageTk.PhotoImage(photo_dailymedal)
	Label(report_frame, image = dailymedal, highlightthickness = 0, bd = 0, bg="#fff").place(x=190, y=100)

	dailymedal_text1 = Label(report_frame, text = number_of_daily.get(), font = ("Calibri", 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	dailymedal_text1.place(x=240, y=110)

	# Yellow cube
	photo_yellow = Image.open('Resource/Yellow.png')
	photo_yellow = photo_yellow.resize((20, 20), Image.ANTIALIAS)
	yellow = ImageTk.PhotoImage(photo_yellow)
	Label(report_frame, image = yellow, highlightthickness = 0, bd = 0, bg="#fff").place(x=20, y=290)

	Label(report_frame, text = "daily", font = ('Calibri', 15), highlightthickness = 0, bd = 0, bg="#fff").place(x=50, y=285)


	dailymedal_text2 = Label(report_frame, text = number_of_daily.get(), font = ('Calibri', 20, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	dailymedal_text2.place(x=140, y=283)


	# tổng hợp số tasks đã hoàn thành
	Label(report_frame, text="Total", font=('Calibri', 16, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040").place(x=215, y=190)

	# dựa vào tổng các chữ số của số task, ta sẽ căn được vị trí của total tasks
	if len(number_of_tasks.get()) == 1:
		total_tasks_x = 224
	elif len(number_of_tasks.get()) == 2:
		total_tasks_x = 206
	elif len(number_of_tasks.get()) == 3:
		total_tasks_x = 186

	total_tasks = Label(report_frame, text=number_of_tasks.get(), font=('Calibri', 45, 'bold'), highlightthickness = 0, bd = 0, bg="#fff", fg="#404040")
	total_tasks.place(x=total_tasks_x, y=215)


	# tạo FRAME THỨ 2: Tạo to-do-list mới ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
	mission_frame = Frame(main, bg = "#404040", width = 500, height = 350)
	mission_frame.grid(column = 2, row = 2, sticky = tk.W)

	# MAIN 1: Manage and check your missions ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(mission_frame, text="Manage and check your missions", font=('Calibri', 24), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=1)
	# SUB TITLE: title phụ  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(mission_frame, text="there are so much things you have done", font=('Calibri', 14), bg="#404040", fg="#fff", anchor=N).grid(column=1, row=2)


	# ẢNH MINH HỌA CHÍNH: chiếc Cúp ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	photo = Image.open('Resource/Cup.png')
	photo = photo.resize((160, 160), Image.ANTIALIAS)
	cup = ImageTk.PhotoImage(photo)
	Label(mission_frame, image = cup, highlightthickness = 0, bd = 0).grid(column=1, row=3, pady=20)


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
		main.destroy()
		mission_type.mt()

	# tạo biến ảnh [New process]
	np_pic = StringVar()
	np_pic.set('Resource/Buttons/Button_newprocess1.png')

	# hiển thị biến ảnh [New process] ra màn hình
	np = PhotoImage(file=np_pic.get())
	new_process = Button(mission_frame, image = np, highlightthickness = 0, bd = 0, command=npEvent, activebackground="#404040")
	new_process.grid(column=1, row=4, sticky =tk.W, padx=60)

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
	check_what_you_have_done = Button(mission_frame, image = cwyhd, highlightthickness = 0, bd = 0, command=cwyhdEvent, activebackground="#404040")
	check_what_you_have_done.grid(column=1, row=4, sticky=tk.E, padx=60)

	# chuột còn ở trên button
	check_what_you_have_done.bind('<Enter>', cwyhdHover)
	# chuột rời button
	check_what_you_have_done.bind('<Leave>', cwyhdHover)


	# Dash-line ngăn cách 1 - [của frame 2 - Dòng 1]
	dash_line1 = Image.open('Resource/dash_line.png')
	dash_line1 = dash_line1.resize((500, 20), Image.ANTIALIAS)
	dash1 = ImageTk.PhotoImage(dash_line1)
	Label(main, image = dash1, highlightthickness = 0, bd = 0).place(x=300, y=93)

	# Dash-line ngăn cách 2 - [của frame 2 - Dòng 1]
	dash_line2 = Image.open('Resource/dash_line.png')
	dash_line2 = dash_line2.resize((500, 20), Image.ANTIALIAS)
	dash2 = ImageTk.PhotoImage(dash_line2)
	Label(main, image = dash2, highlightthickness = 0, bd = 0).place(x=300, y=439)


	# TẠO FRAME THỨ 3: Chân ---------------------------------------------------------------------------------------------------------------
	last_frame = Frame(main, bg = "#404040", width = 800, height = 150)
	last_frame.grid(column = 1, row = 3, columnspan = 2, sticky = tk.W)



	#Defining Background
	list_frame = Frame(main, bg = "#fff", width = 300, height = 500)
	list_frame.grid(column = 3, row = 2, rowspan = 2, sticky = tk.W)

	background = Canvas(list_frame, width=280, height=500, bg="#fff")
	background.grid(row=1, column=1)

	# tạo cuộn quay cho màn hình nếu dòng [mục đích] dài vượt qua [cấu hình] ban đầu của giao diện
	scroll_bar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=background.yview)
	scroll_bar.grid(row=1, column=1, sticky=tk.E, padx=10)

	background.configure(yscrollcommand=scroll_bar.set)

	second_frame = Frame(background, bg="#fff")
	background.create_window(0,0, window=second_frame)

	# ADDED
	second_frame.bind('<Configure>', lambda e: background.configure(scrollregion=background.bbox('all')))


	Label(second_frame, text="Process", font=('Calibri', 24), bg="#fff", fg="#404040").grid(column=1, row=1, pady=10)

	def taskButtonEvent(index, arr):
		#print(index)
		#print(my_to_do_list.iloc[index])
		#print(arr)

		if my_to_do_list['Done'].iloc[index] == True: # +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +
			#print('not done')
			arr['Done'][index] = False

			number_of_gem.set(str(int(number_of_gem.get()) - my_to_do_list['Checkpoint'].iloc[index]))
			gem_text.config(text=number_of_gem.get())

			number_of_tasks.set(str(int(number_of_tasks.get()) - 1))
			total_tasks.config(text=number_of_tasks.get())

			# dựa vào tổng các chữ số của số task, ta sẽ căn được vị trí của total tasks
			if len(number_of_tasks.get()) == 1:
				total_tasks_x = 224
			elif len(number_of_tasks.get()) == 2:
				total_tasks_x = 206
			elif len(number_of_tasks.get()) == 3:
				total_tasks_x = 186

			total_tasks.place(x=total_tasks_x, y=215)


			if my_to_do_list['Type'].iloc[index] == 'process':
				so = str(int(number_of_process.get()) - 1)
				#print('so:',so)
				
				# thay đổi giá trị của số task [Process] đã hoành thành
				number_of_process.set(so)

				# thay số task [Process] trên màn hình
				processmedal_text1.config(text = number_of_process.get())
				processmedal_text2.config(text = number_of_process.get())

			elif my_to_do_list['Type'].iloc[index] == 'skill':
				so = str(int(number_of_skill.get()) - 1)
				#print('so:',so)				
				
				# thay đổi giá trị của số task [Skill] đã hoành thành
				number_of_skill.set(so)

				# thay đổi số task [Skill] trên màn hình
				skillmedal_text1.config(text = number_of_skill.get())
				skillmedal_text2.config(text = number_of_skill.get())

			elif my_to_do_list['Type'].iloc[index] == 'daily':
				so = str(int(number_of_daily.get()) - 1)
				#print('so:',so)

				# thay đổi giá trị của số task [Daily] đã hoành thành				
				number_of_daily.set(so)

				# thay đổi số task [Daily] trên màn hình
				dailymedal_text1.config(text = number_of_daily.get())
				dailymedal_text2.config(text = number_of_daily.get())


		elif my_to_do_list['Done'].iloc[index] == False: # +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +
			#print('done')
			arr['Done'][index] = True

			number_of_gem.set(str(int(number_of_gem.get()) + my_to_do_list['Checkpoint'].iloc[index]))
			gem_text.config(text=number_of_gem.get())

			number_of_tasks.set(str(int(number_of_tasks.get()) + 1))
			total_tasks.config(text=number_of_tasks.get())

			# dựa vào tổng các chữ số của số task, ta sẽ căn được vị trí của total tasks
			if len(number_of_tasks.get()) == 1:
				total_tasks_x = 224
			elif len(number_of_tasks.get()) == 2:
				total_tasks_x = 206
			elif len(number_of_tasks.get()) == 3:
				total_tasks_x = 186

			total_tasks.place(x=total_tasks_x, y=215)


			# kiểm tra xem số Gem thu thập được mốc Level chưa
			if int(number_of_gem.get()) >= level_file['Gem'].iloc[int(number_of_level.get())]:
				number_of_level.set(str(int(number_of_level.get()) + 1))
				level.config(text=number_of_level.get())


			if my_to_do_list['Type'].iloc[index] == 'process':
				so = str(int(number_of_process.get()) + 1)
				#print('so:',so)

				# thay đổi giá trị của số task [Process] đã hoành thành
				number_of_process.set(so)

				# thay số task [Process] trên màn hình
				processmedal_text1.config(text = number_of_process.get())
				processmedal_text2.config(text = number_of_process.get())

			elif my_to_do_list['Type'].iloc[index] == 'skill':
				so = str(int(number_of_skill.get()) + 1)
				#print('so:',so)				

				# thay đổi giá trị của số task [Skill] đã hoành thành
				number_of_skill.set(so)
				
				# thay số task [Skill] trên màn hình
				skillmedal_text1.config(text = number_of_skill.get())
				skillmedal_text2.config(text = number_of_skill.get())

			elif my_to_do_list['Type'].iloc[index] == 'daily':
				so = str(int(number_of_daily.get()) + 1)
				#print('so:',so)				

				# thay đổi giá trị của số task [Daily] đã hoành thành
				number_of_daily.set(so)

				# thay số task [Daily] trên màn hình
				dailymedal_text1.config(text = number_of_daily.get())
				dailymedal_text2.config(text = number_of_daily.get())

			

		my_to_do_list['Done']  = pd.DataFrame(arr)
		your_experiments['Gem'].iloc[0] = int(number_of_gem.get())
		your_experiments['Level'].iloc[0] = int(number_of_level.get())

		#print(my_to_do_list)
		my_to_do_list.to_csv('my_todolist.csv', index=False)
		print(your_experiments)
		your_experiments.to_csv('your_experiments.csv', index=False)



	def showTask(task, date, but1, but2, image, line, color, done):

		# khung màu của Task	
		Label(second_frame, image = image, highlightthickness = 0, bd = 0).grid(column=1, row=dong, pady=10)

		# số thứ tự của Task
		Label(second_frame, text=str(dong-1), font=('Vogue', 22, 'bold'), bg=color, fg="#fff").place(x=add, y=vitri_y+10)

		# vạch ngăn cách của Task 
		Label(second_frame, image = line, highlightthickness = 0, bd = 0).place(x=45, y=vitri_y-5)

		# tên của Task
		# xử lí cho chuỗi khong dài quá 14 kí t

		# tạo frame thứ 1: Report, nếu khong sẽ làm hỏng bố cục của app
		string = ""
		dem = 0
		for char in task:
			string += char
			dem += 1
			if dem == 14:
				string += "..."
				break

		Label(second_frame, text=string, font=('Calibri', 16), bg=color, fg="#fff").place(x=65, y=vitri_y)

		# deadline của Task
		Label(second_frame, text="deadline:", font=('Calibri', 10), bg=color, fg="#fff").place(x=65, y=vitri_y+35)
		Label(second_frame, text=date, font=('Calibri', 12, 'bold'), bg=color, fg="#fff").place(x=118, y=vitri_y+33)

		# tạo button check hoàn thành task hay chưa
		if done == False:
			task_buttons.append(tk.Checkbutton(second_frame, image=but1, selectimage=but2, indicatoron=False, onvalue=True, offvalue=False, highlightthickness = 0, bd = 0, bg=color, activebackground=color, selectcolor=color))
			buttons_coordinates.append(vitri_y+28)
		elif done == True:
			task_buttons.append(tk.Checkbutton(second_frame, image=but2, selectimage=but1, indicatoron=False, onvalue=False, offvalue=True, highlightthickness = 0, bd = 0, bg=color, activebackground=color, selectcolor=color))
			buttons_coordinates.append(vitri_y+28)

	
	colors = ['Resource/Tasks/Black.png', 'Resource/Tasks/Red.png', 'Resource/Tasks/Blue.png', 'Resource/Tasks/Yellow.png']
	colors_hex = ['#404040', '#F36447', '#558ED5', '#EEC44C']
	lines = ['Resource/Tasks/line_black.png', 'Resource/Tasks/line_red.png', 'Resource/Tasks/line_blue.png', 'Resource/Tasks/line_yellow.png']
	buttons1_color = ['Resource/Buttons/Button_doneBlack1.png', 'Resource/Buttons/Button_doneRed1.png', 'Resource/Buttons/Button_doneBlue1.png', 'Resource/Buttons/Button_doneYellow1.png']
	buttons2_color = ['Resource/Buttons/Button_doneBlack2.png', 'Resource/Buttons/Button_doneRed2.png', 'Resource/Buttons/Button_doneBlue2.png', 'Resource/Buttons/Button_doneYellow2.png']

	dong=2
	vitri_y = 80

	# mảng lưu lại khung màu random của Task
	images = []
	# mảng lưu lại màu của các line ngăn cách trong Task
	images_line = []
	# mảng lưu lại các button trong Task
	task_buttons = []
	buttons_coordinates = []
	task_buttons1 = []
	task_buttons2 = []

	image_index = 0

	# vị trí của số thứ tự của Task
	add = 17
	for task, date, done, type_of_mission in zip(my_to_do_list['Name'], my_to_do_list['Deadline'], my_to_do_list['Done'], my_to_do_list['Type']):		

		# xác định loại màu mà các objects trong khung sẽ được định dạng
		# màu đỏ là: Skill
		if type_of_mission == "process":
			color = colors[1]
			to_do_list = Image.open(color)
			to_do_list = to_do_list.resize((250, 70), Image.ANTIALIAS)
			bar = ImageTk.PhotoImage(to_do_list)

			color = colors_hex[1]
			line = lines[1]
			button1 = buttons1_color[1]
			button2 = buttons2_color[1]

		# màu xanh là: Process
		elif type_of_mission == "skill":
			color = colors[2]
			to_do_list = Image.open(color)
			to_do_list = to_do_list.resize((250, 70), Image.ANTIALIAS)
			bar = ImageTk.PhotoImage(to_do_list)

			color = colors_hex[2]
			line = lines[2]
			button1 = buttons1_color[2]
			button2 = buttons2_color[2]

		# màu vàng là: Daily
		elif type_of_mission == "daily":
			color = colors[3]
			to_do_list = Image.open(color)
			to_do_list = to_do_list.resize((250, 70), Image.ANTIALIAS)
			bar = ImageTk.PhotoImage(to_do_list)

			color = colors_hex[3]
			line = lines[3]
			button1 = buttons1_color[3]
			button2 = buttons2_color[3]

		to_do_list_line = Image.open(line)
		to_do_list_line = to_do_list_line.resize((20, 70), Image.ANTIALIAS)
		bar2 = ImageTk.PhotoImage(to_do_list_line)

		to_do_list_button1 = Image.open(button1)
		to_do_list_button1 = to_do_list_button1.resize((30, 30), Image.ANTIALIAS)
		but1 = ImageTk.PhotoImage(to_do_list_button1)

		to_do_list_button2 = Image.open(button2)
		to_do_list_button2 = to_do_list_button2.resize((30, 30), Image.ANTIALIAS)
		but2 = ImageTk.PhotoImage(to_do_list_button2)

		# lưu lại khung màu
		images.append(bar)
		# lưu lại line ngăn cách của Task
		images_line.append(bar2)
		# lưu lại button Tick trạng thái 1
		task_buttons1.append(but1)
		# lưu lại button Tick trạng thái 2
		task_buttons2.append(but2)

		showTask(task, date, task_buttons1[image_index], task_buttons2[image_index], images[image_index], images_line[image_index], color, done)

		dong+=1
		vitri_y+=90
		image_index+=1

		if dong == 11:
			add -= 7

	# lưu các trạng thái của task gồm [hoàn thành] hoặc [chưa hoàn thành]
	modes = {'Done':[]}
	for mode in my_to_do_list['Done']:
		modes['Done'].append(mode)

	# hiển thị các Button Tick của Task
	for i in range(len(task_buttons)):
		task_buttons[i].config(command = lambda k=i: taskButtonEvent(k, modes))
		task_buttons[i].place(x=200, y=buttons_coordinates[i])

	main.mainloop()
