# self o day la vat can, item, problems

class minibox:
	def __init__(self, ques, ans, blood):
		self.image = "images/minibox.png"
		self.HP = blood
		self.question = ques
		self.answer = ans
		self.x = 270
		self.y = 30
		self.ITEM_WIDTH = 35
		self.ITEM_HEIGHT = 35

	def check_answer (self, char_answer):
		if self.answer in char_answer:
			print("Correct !")
			return 0
		else:
			self.HP = -self.HP
			print("Wrong !")
			return 1
class apple:
	def __init__(self,talk_something, char_x, char_y):
		self.image = "images/apple.png"
		self.x = char_x
		self.y = char_y
		self.question = talk_something
		self.ITEM_WIDTH = 35
		self.ITEM_HEIGHT = 35

class sparkle:
	def __init__(self, comment, ans, pts):
		self.x = 270
		self.y = 30
		self.HP = pts
		self.point = pts * 10
		self.answer = ans
		self.question = comment
		self.image = "images/sparkle.png"
		self.ITEM_WIDTH = 35
		self.ITEM_HEIGHT = 35
	
	def check_answer (self, char_answer):
		if self.answer in char_answer:
			print("Correct !")
			return 0
		else:
			self.HP = -self.HP
			print("Wrong !")
			return 1


class energy:
	def __init__(self, alert, char_x, char_y):

		self.image = "images/energy.png"
		self.x = char_x
		self.y = char_y
		self.question = alert
		self.ITEM_WIDTH = 35
		self.ITEM_HEIGHT = 35

class spaceship:
	def __init__(self,alert,x,y):
		self.name = "SpaceShip"
		self.image = "images/spaceship.png"
		self.question = alert
		self.x = x
		self.y = y
		self.ITEM_WIDTH = 55
		self.ITEM_HEIGHT = 65
class earth:
	def __init__(self,x,y):
		self.image = "images/earth.png"
		self.x = x
		self.y = y
		self.ITEM_WIDTH = 55
		self.ITEM_HEIGHT = 55

