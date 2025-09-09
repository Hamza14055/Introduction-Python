import pygame
pygame.init()
SCREENWIDTH,SCREENHEIGHT =500,500
display_surface = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("My first Game")
Grey = (58,58,58)
bg_pic = pygame.transform.scale(
    pygame.image.load("C:\\Users\\Admin\\Desktop\\Python\\Pygame\\gameboy.png"
).convert_alpha(),(300,300))
bg_rect = bg_pic.get_rect(center=(SCREENWIDTH//2, SCREENHEIGHT//2))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(Grey)
    display_surface.blit(bg_pic, bg_rect)

    

    
    pygame.display.flip()

pygame.quit()


