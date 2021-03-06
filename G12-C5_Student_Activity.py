# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:34:46 2021

@author: dell
"""

import pygame, random, sys, math

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Asteroid")
background_image = pygame.image.load("bg2.jpg").convert()
player_image = pygame.image.load("s4.png").convert_alpha()



#Color or rectangle

player=pygame.Rect(200,200,30,30)


enemy=pygame.Rect(100,100,30,30)
enemy_image = pygame.image.load("e3.png").convert_alpha()

xvel=[]
yvel=[]

angle=0
change=0
distance=5
forward=False

enemycount=10

enemies=[]

for i in range(1,enemycount):
    
  enemies.append(pygame.Rect(random.randint(0,400),random.randint(0,600),20,20))
  
  xvel.append(random.randint(-3,3))
  yvel.append(random.randint(-3,3))



def newxy(oldx,oldy,distance,angle):
  angle=math.radians(angle+90)
  nx=oldx+(distance*math.cos(angle))
  ny=oldy-(distance*math.sin(angle))
  return nx, ny
 
    
while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
          
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        change= 0  
      if event.key == pygame.K_UP:
        forward = False   
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        change =6
      if event.key ==pygame.K_RIGHT:
        change = -6
      if event.key == pygame.K_UP:
        forward = True
    
  i=0
  
  for enemy in enemies:
      
    enemy.x+=xvel[i]
    
    enemy.y+=yvel[i]
     
    if enemy.x < -250 or enemy.x > 650: 
        
      xvel[i] = -1*xvel[i]
    
    if enemy.y < -250 or enemy.y > 850:  
      yvel[i]=-1*yvel[i]
        
    i+=1    
    screen.blit(enemy_image,enemy)      
  
  if forward:
      player.x, player.y=newxy(player.x, player.y, distance, angle)  
 
  angle += change
  newimg=pygame.transform.rotate(player_image,angle)  
  
 
  screen.blit(newimg , player)
 

  pygame.display.update()
  clock.tick(30)
