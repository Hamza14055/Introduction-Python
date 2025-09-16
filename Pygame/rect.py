import pygame 
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT =500,500
Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.font.init()
font = pygame.font.SysFont('Arial', 30) 
done = False
while not done :
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            done = True
    text_surface = font.render("Hello!", True, (255, 255, 255))
    rect = pygame.Rect(100,60,100,60)
    rect.center=(SCREEN_WIDTH //2 ,SCREEN_HEIGHT //2 )
    pygame.draw.rect(Screen,(255,0,0),rect)
    Screen.blit(text_surface,(50,50))

    pygame.display.flip()
