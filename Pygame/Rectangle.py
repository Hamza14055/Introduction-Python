import pygame 
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done :
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            done = True
    pygame.draw.rect((screen),(1,125,250),pygame.Rect(30,30,60,60))
    pygame.display.flip()
        