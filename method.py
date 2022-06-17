import pygame
import sys
from pygame.locals import K_ESCAPE, QUIT

# Dinh nghia cac thong so cho game

WIDTH = 800
HEIGHT = 600

INFO_BOARD_X = 640
FPS = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PLAYER_WIDTH = 35
PLAYER_HEIGHT = 55



icon= pygame.image.load("images/Space.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Flying Moon")



class Method:

	def start_game(self):
		pygame.init()

		self.clock = pygame.time.Clock()

		# khoi tao thong so cho game
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
		self.font = pygame.font.SysFont("Courier New", 14)
		self.mainfont = pygame.font.SysFont("Courier New", 33)
		pygame.mixer.music.load("sound/background1.mp3")
		pygame.mixer.music.play(-1, 0.0)


		self.playing = True

		self.prepare_player()


	def check_if_user_quit(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				return True

			key = self.get_key_pressed()
			if key[K_ESCAPE]:
				return True
		return False

	def stop_mus(self):
		pygame.mixer.music.stop ()
	def end_game_sound(self):
		pygame.mixer.music.load("sound/end_game.mp3")
		pygame.mixer.music.play(-1, 0.0)
		
	def play(self):
		pygame.mixer.music.load("sound/background1.mp3")
		pygame.mixer.music.play(-1, 0.0)

	def stop_game(self):
		self.playing = False

# dong cua so game
	def close_window(self):
		pygame.quit()

	def get_key_pressed(self):
		return pygame.key.get_pressed()

	def show_new_frame(self):
		pygame.display.flip()
		self.clock.tick(FPS)

	def draw_topic(self):
		self.topic = pygame.image.load("images/topic.png").convert_alpha()
		self.topic = pygame.transform.scale(self.topic,(WIDTH, HEIGHT))
		self.screen.blit(self.topic,(0,0))

	def draw_background(self):
		self.screen.fill(BLACK)
		self.background = pygame.image.load("images/background.jpg").convert_alpha()
		self.background = pygame.transform.scale(self.background,(600,700))
		self.screen.blit(self.background,(0,0))
	
	def draw_player_hp(self):
		HP = self.mainfont.render("HP: " + str(self.player.HP), 1, WHITE)
		self.screen.blit(HP, (INFO_BOARD_X, 17))
	

	def draw_guide(self):
		self.guide1 = pygame.image.load("images/guide1.png").convert_alpha()
		self.guide1 = pygame.transform.scale(self.guide1,(100, 100))
		self.screen.blit(self.guide1,(600,100))

		self.guide2 = pygame.image.load("images/guide2.png").convert_alpha()
		self.guide2 = pygame.transform.scale(self.guide2,(100, 100))
		self.screen.blit(self.guide2,(600,200))

		self.guide3 = pygame.image.load("images/guide3.png").convert_alpha()
		self.guide3 = pygame.transform.scale(self.guide3,(100, 100))
		self.screen.blit(self.guide3,(600,300))

		self.guide4 = pygame.image.load("images/guide4.png").convert_alpha()
		self.guide4 = pygame.transform.scale(self.guide4,(100, 100))
		self.screen.blit(self.guide4,(600,400))

	
	def draw_result(self):
		self.result = pygame.image.load("images/result.jpg").convert_alpha()
		self.result = pygame.transform.scale(self.result,(WIDTH, HEIGHT))
		self.screen.blit(self.result,(0,0))

	def draw_alert_of_end_game(self):
		self.alert = pygame.image.load("images/alert.png").convert_alpha()
		self.alert = pygame.transform.scale(self.alert, (WIDTH, HEIGHT))
		self.screen.blit(self.alert, (0,0))



	def draw_runway(self, points):
		points = self.mainfont.render(str(points), 1, WHITE)
		self.screen.blit(points, (0,0))

	def draw_player(self):
		self.screen.blit(self.player.Image, (self.player.x, self.player.y))
    
	def prepare_player(self):
		Image = pygame.image.load(self.player.image[self.player.motion]).convert_alpha()
		self.player.Image = pygame.transform.scale(
			Image, (PLAYER_WIDTH, PLAYER_HEIGHT)
			)
		self.player.mask = pygame.mask.from_surface(self.player.Image)
	
	def prepare_player_place(self, i, x, y, width, height):
		Image = pygame.image.load(self.player.place[i]).convert_alpha()
		self.player.Image = pygame.transform.scale(
			Image, (width, height)
			)
		self.screen.blit(self.player.Image, (x,y))
		

		self.player.mask = pygame.mask.from_surface(self.player.Image)

	#def draw_condition(self, x, y):



	def draw_item(self, item):
		self.screen.blit(item.Image, (item.x, item.y))
	
	def prepare_item(self, item):
		Image = pygame.image.load(item.image).convert_alpha()
		item.Image = pygame.transform.scale(
			Image, (item.ITEM_WIDTH, item.ITEM_HEIGHT)
			)
		item.mask = pygame.mask.from_surface(item.Image)
	
	def draw_question(self, item):
		ques = self.font.render(str(item.question), 1, WHITE)
		self.screen.blit(ques, (((70 - len(item.question))/2) * 10, 10))





