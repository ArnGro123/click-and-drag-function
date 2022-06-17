import pygame
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

selected = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        if event.type == MOUSEBUTTONDOWN:
            selected = True
            first_coord = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONUP:
            selected = False
    
    display.fill("black")

    if selected == True:
        second_coord = pygame.mouse.get_pos()
        width = abs(second_coord[0]-first_coord[0])
        height = abs(second_coord[1]-first_coord[1])

        if first_coord[0] > second_coord[0] and first_coord[1] > second_coord[1]:
            pygame.draw.rect(display,"blue",(second_coord[0],second_coord[1],width,height))
        
        elif first_coord[0] < second_coord[0] and first_coord[1] > second_coord[1]:
            pygame.draw.rect(display,"blue",(first_coord[0],first_coord[1]-height,width,height))

        elif first_coord[0] < second_coord[0] and first_coord[1] < second_coord[1]:
            pygame.draw.rect(display,"blue",(first_coord[0],first_coord[1],width,height))
        
        elif first_coord[0] > second_coord[0] and first_coord[1] < second_coord[1]:
            pygame.draw.rect(display,"blue",(first_coord[0]-width,first_coord[1],width,height))
        
    
    pygame.display.update()
    clock.tick(30)
