import pygame
import math 
pygame.init()

screen = pygame.display.set_mode([480, 800])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0, 0 , 0))

        pygame.draw.ellipse(screen, (75,240,252), (135, 175, 60, 80))
        pygame.draw.ellipse(screen, (75, 240, 252), (300, 175, 60, 80))
        pygame.draw.arc(screen, (0,255,255) , (150, 450, 180, 100), math.pi, 2*math.pi,8)
     
        pygame.display.flip()

pygame.quit()