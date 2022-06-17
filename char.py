#self o day la astronaut
import time

class charac:
	# build atribute for the character
    def __init__(self):
        self.name = "Astronaut"
        self.HP = 50
        self.high = 10
        self.time = 0.4
        self.x=270
        self.y=70
        self.questions = []

	# xac dinh toa do an dao cho character
	    
	# xac dinh hinh anh cho character
        self.image = ["images/design1.png","images/design2.png","images/design3.png"]
        self.p = 0
        self.place = ['place/90 up.png','place/half 45 right up1.png','place/45 right up.png','place/half 45 right up2.png','place/90 right.png','place/half 45 right down1.png','place/45 right down.png','place/half 45 right down2.png','place/90 down.png','place/half 45 left down1.png','place/45 left down.png','place/half 45 left down2.png','place/90 left.png','place/half 45 left up1.png','place/45 left up.png','place/half 45 left up2.png']
        
        self.place_x =[285,360,437,475,500,490,437,360,285,190,113,60,40,60,113,180]
        self.place_y =[70,80,117,175,285,385,456,480,500,490,446,375,285,180,127,80,70]
        
        self.w =[35,55,35,55,55,45,35,55,35,55,35,55,55,55,35,35]
        self.h =[55,65,55,65,35,45,55,65,55,65,55,65,35,65,55,55]
        self.motion = 0

	# build method for character,
    def stand (self):  # chuyen dong 1
    	
       	#self.image = "images/design1.jpg"
        self.motion = 1                    # chuyen sang chuyen dong 2

    def walk (self):  # chuyen dong 2
            
        #self.image1 = "images/design2.jpg"
        self.motion = 0                    # chuyen ve chuyen dong 1

    def jump (self):  # chuyen dong co dieu kien (duoc kich hoat khi dung key_pressed)

        self.y = 30
        #self.image = "images/design3"       # chuyen hoat anh 3
       
        self.motion = 2
       
    
    def fall(self):
        self.y = 70           #self.y = 70     # sau khi jump thi roi xuong vi tri ban dau
        self.motion = 0  
    
    def get_question (self, problem):
        print(problem.question)	
        self.questions.append(problem)

    def answer (self):
        an = input("Enter your answer: ")
        return an.upper()

    def die_or_alive (self, lucky_num):
        if lucky_num == 0:
            self.HP += self.questions[len(self.questions)-1].HP
        elif lucky_num == 1:
            self.HP += self.questions[len(self.questions)-1].HP

    def touch(self, obj):
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None

    def touch_in_Earth(self, obj, d):
        offset_x = int(obj.x - self.place_x[d])
        offset_y = int(obj.y - self.place_y[d])
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None





















