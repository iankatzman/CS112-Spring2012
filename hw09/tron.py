#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *

class tron_p1:
     def __init__(self, surface, x, y, length):
         self.surface = surface
         self.x = x
         self.y = y
         self.length = length
         self.dir_x = 0
         self.dir_y = -1
         self.body = []
         self.crashed = False
 
     def key_event_p1(self, event):
          if event.key == pygame.K_w and self.dir_y != 1: 
               self.dir_x = 0
               self.dir_y = -1
          elif event.key == pygame.K_d and self.dir_x != -1:
               self.dir_x = 1
               self.dir_y = 0
          elif event.key == pygame.K_s and self.dir_y != -1:
               self.dir_x = 0
               self.dir_y = 1
          elif event.key == pygame.K_a and self.dir_x != 1:
               self.dir_x = -1
               self.dir_y = 0

     def move(self):
         self.x += self.dir_x
         self.y += self.dir_y
 
         if (self.x, self.y) in self.body: 
             self.crashed = True
 
         self.body.insert(0, (self.x, self.y))

      
     def draw(self):
         for x, y in self.body:
             self.surface.set_at((x, y), (255, 0, 0))


class tron_p2:
     def __init__(self, surface, x, y, length):
         self.surface = surface
         self.x = x
         self.y = y
         self.length = length
         self.dir_x = 0
         self.dir_y = -1
         self.body = []
         self.crashed = False
 
     def key_event_p2(self, event):
          if event.key == pygame.K_UP and self.dir_y != 1:
               self.dir_x = 0
               self.dir_y = -1
          elif event.key == pygame.K_RIGHT and self.dir_x != -1:
               self.dir_x = 1
               self.dir_y = 0
          elif event.key == pygame.K_DOWN and self.dir_y != -1:
               self.dir_x = 0
               self.dir_y = 1
          elif event.key == pygame.K_LEFT and self.dir_x != 1:
               self.dir_x = -1
               self.dir_y = 0

     def move(self):
         self.x += self.dir_x
         self.y += self.dir_y
 
         if (self.x, self.y) in self.body:
             self.crashed = True
 
         self.body.insert(0, (self.x, self.y))
        
     def draw(self):
         for x, y in self.body:
             self.surface.set_at((x, y), (0, 0, 255))
 
width = 700
height = 600
 
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
end_game = False

p1 = tron_p1(screen, width/3, height/2, 500) 
p2 = tron_p2(screen, width/2, height/2, 500) 

print "Controls: "
print "Player one is Red and uses w,a,s,d to move."
print "Player two is blue and uses the arrow keys to move."
print "Avoid the edges of the screen, the other player and your own trail."

while end_game == False:

     while running == True:

          screen.fill((0, 0, 0)) 
    
          p1.move()
          p1.draw()

          if p1.crashed or (p1.x <= 0) or (p1.x >= width-1) or (p1.y <= 0) or (p1.y >= height-1):
               print "Player one crashes!"
               running = False

          if (p1.x, p1.y) in p2.body:
               p1.crashed = True
               print "Player one crashes!"
               running = False

          for event in pygame.event.get():
               
               if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                    end_game = True
                    print "Thanks for playing!"

               elif event.type == pygame.KEYDOWN:
                    p1.key_event_p1(event)

                    p2.key_event_p2(event)
 
          p2.move()
          p2.draw()

          if p2.crashed or (p2.x <= 0) or (p2.x >= width-1) or (p2.y <= 0) or (p2.y >= height-1):
               print "Player two crashes!"
               running = False

          if (p2.x, p2.y) in p1.body:
               p2.crashed = True
               print "Player two crashes!"
               running = False

          pygame.display.flip()
          clock.tick(250)

     for event in pygame.event.get():
          if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
               end_game = True
               print "Thanks for playing!"

