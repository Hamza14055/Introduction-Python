import pygame
pygame.init()
clock = pygame.time.Clock()
sprite_height = 40
sprite_width = 30
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
x,y = 100,100
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT    :
            done = True
    pressed = pygame.key.get_pressed()
    if pressed [pygame.K_RIGHT]: x+=3
    if pressed [pygame.K_LEFT]: x-=3
    if pressed [pygame.K_UP]:y-=3
    if pressed [pygame.K_DOWN]:y+=3
    x = min(max (0,x), SCREEN_WIDTH-sprite_width)
    y = min(max(0,y),SCREEN_HEIGHT-sprite_height)
    screen.fill((255,0,0))
    
    pygame.draw.rect(screen,(255,255,0),pygame.Rect(x,y,sprite_width,sprite_height))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
