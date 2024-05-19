"""
This file is for new game: pygame
Created by: Arman Hovhannisyan
Date: 18 May

"""

import pygame

pygame.init()

screen_w = 800
screen_h = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("My game")
player = pygame.Rect((300, 250, 50, 50))


run = True
while run:
    
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
