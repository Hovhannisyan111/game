"""
This file is for new game: pygame
Created by: Arman Hovhannisyan
Date: 18 May

"""

import pygame
import random
import time

pygame.font.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gmae")

backround = pygame.transform.scale(pygame.image.load("back2.jpg"), (width, height))
dino_right = pygame.image.load("dinor.png")
dino_left = pygame.image.load("dinor.png")

dino_h = 30
dino_w = 20

star_w = 10
star_h = 20
star_v = 3

font = pygame.font.SysFont("roman", 30)

def back(player, finish_time, stars):
    window.blit(backround, (0, 0))

    time_text = font.render(f"Time: {round(finish_time)}", 1, "white")
    window.blit(time_text, (10, 10))
    pygame.draw.rect(window, "orange",player)
    
    for star in stars:
        pygame.draw.rect(window, "white", star)

    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(200, height - dino_h, dino_w, dino_h)

    clock = pygame.time.Clock() 
    start_time = time.time()
    finish_time = 0
    
    star1 = 2000
    star_count = 0

    stars = []
    hit = False


    while run:
        star_count += clock.tick(100)
        finish_time = time.time() - start_time

        if star_count > star1:
            for _ in range(5):
                star_x = random.randint(0, width - star_w)
                star = pygame.Rect(star_x, - star_h, star_w, star_h)
                stars.append(star)
            
            star1 = max(200, star1 - 50)
            star_count =  0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and player.right < width:
            player.move_ip(1,0)
        elif key[pygame.K_LEFT] and player.left > 0:
            player.move_ip(-1,0)

        for star in stars[:]:
            star.y += star_v
            if star.y > height:
                stars.remove(star)
            elif star.y + star_h >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lose = font.render("You lose", 1, "red")
            window.blit(lose, (width/2 - lose.get_width()/2, lose.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        back(player, finish_time, stars)
    pygame.quit()


if __name__ == "__main__":
    main()
