from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN

from method import Method
from char import charac
from obj import minibox, apple, energy, spaceship, sparkle, earth

import time
import pyttsx3

class GAME (Method):
    
    def __init__ (self):
        self.runway = 1
        self.player = charac()
        print()
        
        self.bag = [
                      minibox("Where is Fuji Moutain ?", "JAPAN", 40),
                      minibox("Which moutain is the highest moutain in the world ?", "HIMALAYA", 40),
                      minibox("What is the real color of the Sun ?","WHITE", 20),
                      minibox("Who is the first women got 2 Nobel's prize ?", "MARIE CURIE", 20),
                      minibox("Who is the first person in VietNam get Fields prize ?", "NGO BAO CHAU", 50),
                      minibox("How do we call the cell of brain is ?","NEURON", 20),
                      minibox("Who invented the light bud ?","THOMAS EDISON", 50)
                    
                   ]
        self.material = [ apple("Graviton is very important !", 437, 117),
                          apple("Colected all the energy, you can come back Earth !",285,500),
                          apple("Some Sparkle can instead for energy...", 40, 180)
                        ]
        self.energy = [ energy("When you can see the Earth icon... you will pass !",360,500),
                        energy("Before get Earth icon, let's find the SpaceShip !",500,285),
                        energy("Try hard to run, your SpaceShip is in the runway...", 120, 135)
                      ]
        self.sparkle = [ sparkle("What is the third planet in Solar System ?", "EARTH", 90),
                         sparkle("How many planets in Solar System ?", "7", 50)
                       ]
        self.weapon = [ spaceship("Ready to come home !",285,500)
                      ]
        self.gateway = [ earth(113,400)
                       ]

        self.start_game()
    def while_not_done(self):
        
        self.draw_topic()
        self.show_new_frame()
        
        robot= pyttsx3.init()
        print("Hello! Welcome to Game! My name is " + self.player.name + ". Nice to meet you!")
        robot.say("Hello! Welcome to Game! My name is " + self.player.name + ". Nice to meet you!")
        robot.runAndWait()
        
        self.draw_frame()
        
        while True:
            
            
            if self.check_if_user_quit():
                self.close_window()        
            
            
            
            if len(self.bag) == 0:
                self.runway = self.runway + 2000
                    
            
            if self.player.HP <= 0:
                self.stop_mus()
                
                self.draw_alert_of_end_game()
                self.end_game_sound()
                self.show_new_frame()
                time.sleep(4.2)
                self.close_window()

            
            key = self.get_key_pressed()
             

            if self.runway % 31 == 0 or self.runway % 32 == 0 or self.runway % 33 == 0 or self.runway % 34 == 0 or self.runway % 35 == 0:
                if len(self.bag) >= 1: 
                    self.prepare_item(self.bag[0])
                    self.draw_item(self.bag[0])
                    self.show_new_frame() 
                    #key = self.get_key_pressed()
                    if self.player.touch(self.bag[0]):
                        self.stop_mus()
                        self.draw_frame()                
                        self.draw_question(self.bag[0])
                        self.show_new_frame()
                        self.read_question()
                        self.play()
                        self.player.fall()
                                        #self.player.fall()
                        self.runway = self.runway + 5
                        #self.draw_frame()
            
            if len(self.material) == 0 and self.runway >= 500:
                j=0
                if len(self.energy) >= 1:
                    for i in self.energy:
                        self.prepare_item(i)
                        self.draw_item(i)
                    
                    self.show_new_frame()
                    for i in self.energy:
                        if self.player.touch_in_Earth(i, self.player.p):
                            self.draw_frame()
                            self.draw_question(i)
                            self.show_new_frame()
                            self.energy.remove(i)
                            self.runway = self.runway + 1000
            

            if self.runway % 400 == 0 or self.runway % 401 == 0 or self.runway % 403 == 0 or self.runway % 404 == 0 or self.runway % 405 == 0:
                j=0
                if len(self.sparkle) >=1:
                    self.prepare_item(self.sparkle[j])
                    self.draw_item(self.sparkle[j])
                    self.show_new_frame()

                    if self.player.touch(self.sparkle[j]):
                        self.draw_frame()
                        self.draw_question(self.sparkle[j])
                        self.show_new_frame()
                        self.player.get_question(self.sparkle[j])
                        che = self.sparkle[j].check_answer(self.player.answer())
                        
                        if che == 0:
                            self.runway = self.runway +  self.sparkle[j].point
                        elif che == 1:
                            self.player.HP = self.player.HP + self.sparkle[j].HP

                        self.sparkle.remove(self.sparkle[j])
            
            if self.runway >= 9800 and len(self.weapon) == 0:
                self.prepare_item(self.gateway[0])
                self.draw_item(self.gateway[0])
                self.show_new_frame()
                if self.player.touch_in_Earth(self.gateway[0], self.player.p):
                    self.draw_result()
                    self.show_new_frame()
                    time.sleep(10)
                    self.close_window()

            if self.runway >= 5000:
                if len(self.weapon) >= 1:
                    self.prepare_item(self.weapon[0])
                    self.draw_item(self.weapon[0])
                    self.show_new_frame()

                    if self.player.touch_in_Earth(self.weapon[0], self.player.p):
                        self.runway = self.runway + 2000
                        self.draw_frame()
                        self.draw_question(self.weapon[0])
                        self.show_new_frame()
                        time.sleep(5)

                        self.weapon.remove(self.weapon[0])

            if self.runway % 50 == 0 or self.runway % 51 == 0 or self.runway % 52 == 0:
                if len(self.material) >= 1:
                    i=0
                    self.prepare_item(self.material[i])
                    self.draw_item(self.material[i])
                    self.show_new_frame()

                    if self.player.touch_in_Earth(self.material[i], self.player.p):
                        self.draw_frame()
                        self.draw_question(self.material[i])
                        self.show_new_frame()
                        self.material.remove(self.material[i])
                        self.runway = self.runway + 100
                        #self.draw_frame()


            if key[K_UP]:
                self.player.jump()
                #self.player.motion = 0
                
                self.draw_frame()
                self.show_new_frame()
                
            elif key[K_DOWN]:
                
                self.player.fall()
                self.draw_frame()
                
                
                
            elif key[K_LEFT]:
                if self.player.motion == 0:
                    self.runway = self.runway + 1
                    self.player.stand()
                    
                    self.draw_frame()
                    
                elif self.player.motion == 1:
                    self.runway = self.runway + 1
                    self.player.walk()
                    
                    self.draw_frame()
            
            elif key[K_RIGHT]:
                self.draw_background()
                self.draw_runway(self.runway)
                self.draw_guide()
                self.draw_player_hp()
                self.prepare_player_place(self.player.p, self.player.place_x[self.player.p], self.player.place_y[self.player.p], self.player.w[self.player.p], self.player.h[self.player.p])
                self.show_new_frame()
                self.player.p +=1

                if self.player.p == 16:
                    self.player.p = 0
                    self.prepare_player_place(self.player.p, self.player.place_x[15], self.player.place_y[15], self.player.w[15], self.player.h[15]) 
                    self.draw_frame()


                
            
    def read_question(self): 
        i=0
        robot = pyttsx3.init()
        self.player.get_question(self.bag[i])
        robot.say(self.bag[i].question)
        robot.runAndWait()
        che = self.bag[i].check_answer(self.player.answer())  
        
        
        self.player.die_or_alive(che)
        print("HP: ",self.player.HP)
        self.bag.remove(self.bag[i])
        print()

    def draw_frame(self):
        
        self.prepare_player()
        self.draw_background()
        self.draw_player()
        self.draw_guide()
        self.draw_player_hp()
        self.draw_runway(self.runway)
        self.show_new_frame()


#game = GAME()
#game.while_not_done()
