from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from whenYouFinishedYourMission import wyfym
from PIL import Image, ImageTk
import pandas as pd


# file lưu dữ liệu: my_mission.csv
mission_describe = {'Type':[], 'Name':[], 'Deadline':[], 'Checkpoint':[], 'Describe':[], 'Done':['False']}
describe_of_the_mission = []

def ds(type_of_the_mission, name_of_the_mission, deadline_of_the_mission, checkpoint_of_the_mission):
	win = Tk()
	print(type_of_the_mission)

	describe_of_the_mission = []

	# MAIN 3: Describe ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

	# cấu hình của giao diện chính
	win.geometry("500x350+455+175")

	# set màu cho background
	win.config(bg="#404040")

	# khong cho phóng to màn hình
	#win.resizable(False, False)

	# xóa thanh navigate
	#win.overrideredirect(True)


	#Defining Background
	toolbar = Frame(win, width=500, height=350)
	toolbar.grid(row=1, column=1)

	describe_frame = Frame(win, width=500, height=350)
	describe_frame.grid(row=1, column=1)

	background = Canvas(describe_frame, width=500, height=350, bg="#404040")
	background.grid(row=1, column=1)

	# tạo cuộn quay cho màn hình nếu dòng [mục đích] dài vượt qua [cấu hình] ban đầu của giao diện
	scroll_bar = ttk.Scrollbar(describe_frame, orient=VERTICAL, command=background.yview)
	scroll_bar.grid(row=1, column=1, sticky=tk.E, padx=10)

	background.configure(yscrollcommand=scroll_bar.set)

	second_frame = Frame(background, bg="#404040")
	background.create_window(0,0, window=second_frame)

	# ADDED
	second_frame.bind('<Configure>', lambda e: background.configure(scrollregion=background.bbox('all')))

	def getToKnowYourGoal():
		
		global text_field
		global data
		global next_page

		# hiển thị khung nhập
		text_field=Label(second_frame, image = de, highlightthickness = 0, bd = 0)
		text_field.grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=60, pady=15)

		
		# trường nhập [mục đích] để lấy thông tin từ người dùng
		data=Entry(second_frame, font=('Calibri', 12), width=31, bg="#404040", fg="#fff", insertbackground="#fff", highlightthickness = 0, bd = 0)
		data.grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=85, pady=15)
		data.focus()

		# tạo button chuyển trang
		def next_page():
			# đọc lại dữ liệu cũ từ file
			da = pd.read_csv('my_todolist.csv')

			# lưu lại dữ liệu từ các frame trước
			mission_describe['Type'] = type_of_the_mission
			mission_describe['Name'] = name_of_the_mission
			mission_describe['Deadline'] = deadline_of_the_mission
			mission_describe['Checkpoint'] = checkpoint_of_the_mission
			
			string_describe = ""
			for i in range(0, len(describe_of_the_mission)):
				string_describe += str(i+1) + ' - ' + describe_of_the_mission[i] + '\n'

			mission_describe['Describe'].append(string_describe)

			print(mission_describe)
			# tạo dự liệu mới thành dạng ghi vào file
			my_mission = pd.DataFrame(mission_describe)

			# kết hợp dữ liệu cũ với dữ liệu mới thành 1
			all_data = pd.concat([da, my_mission])

			# cho hỗn hợp dữ liệu mới và dữ liệu cũ vào file data
			all_data.to_csv('my_todolist.csv', index=False)

			# xóa đi dữ liệu cũ
			mission_describe['Type'] = []
			mission_describe['Name'] = []
			mission_describe['Deadline'] = []
			mission_describe['Checkpoint'] = []
			mission_describe['Describe'] = []

			win.destroy()
			wyfym()

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

		next_page = Button(second_frame, image = np, highlightthickness = 0, bd = 0, command=next_page, activebackground="#404040")
		next_page.grid(column=1, row=int(row_varible.get()), sticky=tk.E, padx=40, pady=15)

		# chuột còn ở trên button
		next_page.bind('<Enter>', npHover)
		# chuột rời button
		next_page.bind('<Leave>', npHover)




	# MAIN TITLE: title chính ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
	Label(second_frame, text="Describe", font=('Calibri', 24), width=30, bg="#404040", fg="#fff", anchor=CENTER).grid(column=1, row=1, pady=20)

	Label(second_frame, text="Goal of the mission:",  font=("Calibri", 16), bg="#404040", fg="#fff",).grid(column=1, row=2, sticky=tk.W, padx=22)

	# biến lưu vị trí dòng của một nhiệm vụ mới được tạo
	row_varible = StringVar()
	row_varible.set("3")

	# biến lưu thứ tự
	number = StringVar()
	number.set("1")


	def addHover(event):
		# hình ảnh sẽ phản ánh

		# chưa hover
		if a_pic.get() == 'Resource/Buttons/Button_add1.png':
			# sẽ đổi button sang trạng thái: đã hover
			a_pic.set('Resource/Buttons/Button_add2.png')
			
			photo = Image.open(a_pic.get())
			photo = photo.resize((30, 30), Image.ANTIALIAS)
			add = ImageTk.PhotoImage(photo)
			button_add.config(image = add)
			button_add.image = add

		# đã hover
		else:
			# set button về trạng thái ban đầu
			a_pic.set('Resource/Buttons/Button_add1.png')
			photo = Image.open(a_pic.get())
			photo = photo.resize((30, 30), Image.ANTIALIAS)
			add = ImageTk.PhotoImage(photo)
			button_add.config(image = add)
			button_add.image = add

	# tạo [mục đích] hiện thị lên màn hình, sau khi người dùng đã nhập vào [trường nhập]
	def createGoal():

		# lấy dữ liệu từ trường nhập
		goal.set(data.get())
		# lấy dữ liệu từ trường nhập rồi cho vào biến file để ghi dữ liệu vào file csv
		
		describe_of_the_mission.append(data.get())

		# nếu như [trường nhập] khong có gì, sẽ khong thêm mới
		if len(goal.get()) == 0:
			pass	
		else:
			if len(goal.get()) > 45: # nếu như [trường nhập] có nhiều hơn 45 kí tự sẽ tạo xuống dòng
				s=""
				dem = 45
				for i in range(0, 45):
					s+=goal.get()[i]
				for i in range(45, len(goal.get())):
					if goal.get()[i] == " " and dem >= 45: # nếu một dòng dài hon 45 ki tu thi cho xuong dong
						s+='\n'
						dem=0
					else:
						s+=goal.get()[i]
						dem+=1
				goal.set(s)

			# xóa những gì đã nhập ở trường cũ
			data.destroy()
			text_field.destroy()
			next_page.destroy()

			# xóa button [add] hiện tại để hiển thị [mục đích] người dùng đã nhập
			button_add.destroy()

		# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
			# số thứ tự của [mục đích]
			Label(second_frame, text=number.get(),  font=("Calibri", 16, 'bold'), bg="#404040", fg="#fff",).grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=40, pady=15)
		# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
			# vạch ngăn cách
			line = Image.open('Resource/line.png')
			line = line.resize((2, 40), Image.ANTIALIAS)
			block_line = ImageTk.PhotoImage(line)
			Label(second_frame, image = block_line, highlightthickness = 0, bd = 0).grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=70, pady=15)
		# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
			# nội dung của mục đích, lấy được dữ liệu sau hoạt động của hàm getToKnowYourGoal()
			Label(second_frame, text=goal.get(),  font=("Calibri", 12), bg="#404040", fg="#fff",).grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=85, pady=15)
		# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~	
			row_varible.set(int(row_varible.get()) + 1) # xuống dòng để viết nhiệm vụ mới
			number.set(int(number.get())+1)				# tăng số thứ tự cho nhiệm vụ tiếp theo
			
			# tạo dấu + mới
			createNewButton()

	def createNewButton():
		# set button add ở trạng thái đầu: khong hover
		a_pic.set('Resource/Buttons/Button_add1.png')
		
		global goal
		goal=StringVar()
		getToKnowYourGoal()

		# tạo button thêm một [mục đích] mới
		global button_add # nếu khong khai báo biến toàn cục, sẽ khong thể xóa button cục bộ được gọi từ hàm createGoal
		button_add = Button(second_frame, image = add, highlightthickness = 0, bd = 0, command=createGoal, activebackground="#404040")
		button_add.grid(column=1, row=int(row_varible.get()), sticky=tk.W, padx=40, pady=15)

		# hiệu ứng của button sau khi hover	
		# chuột còn ở trên button
		button_add.bind('<Enter>', addHover)
		# chuột rời button
		button_add.bind('<Leave>', addHover)

	# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	global a_pic
	a_pic = StringVar()
	a_pic.set('Resource/Buttons/Button_add1.png')

	# khai báo biến ảnh của [khung nhập]
	data_entry = Image.open('Resource/Textbox/Textbox_name.png')
	data_entry = data_entry.resize((300, 40), Image.ANTIALIAS)
	de = ImageTk.PhotoImage(data_entry)

	# a là viết tắt của add
	# khai báo biến ảnh của button [add]
	a = Image.open(a_pic.get())
	a = a.resize((30, 30), Image.ANTIALIAS)
	add = ImageTk.PhotoImage(a)

	# tạo biến ảnh [Next page]
	np_pic = StringVar()
	np_pic.set('Resource/Buttons/Button_nextpage1.png')
	
	# hiển thị biến ảnh [Next page] ra màn hình
	np = PhotoImage(file=np_pic.get())


	# tạo một button mới
	createNewButton()

	win.mainloop()