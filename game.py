import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Enzo")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('snail/snail1.png').convert_alpha()



snail_rect = snail_surf.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('graphics/player/bichito.png')
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        #if event.type == pygame.MOUSEMOTION:
         #   print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

   
    if    game_active:
       screen.blit(sky_surface,(0,0))
       screen.blit(ground_surface,(0,300))
       pygame.draw.rect(screen,'#c0e8ec',score_rect)
       pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
       screen.blit(score_surf,score_rect)
       
       snail_rect.x -= 4
       if snail_rect.right <= 0: snail_rect.left = 800
       screen.blit(snail_surf,snail_rect)
   
       # Player
       player_gravity += 1
       player_rect.x += 2
       if player_rect.left >= 800: player_rect.left = 0
       player_rect.y += player_gravity
       # Jump
       if player_rect.bottom >= 300: player_rect.bottom = 300
       screen.blit(player_surf,player_rect)
   
       # Collision
       if snail_rect.colliderect(player_rect):
           #pygame.quit()
           #exit()
           game_active = False
           print('perdiste')
    else:
       screen.fill('Yellow')
        # 1:52

    pygame.display.update()
    clock.tick(60)






