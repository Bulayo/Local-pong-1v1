import pygame, sys

def draw_img():

    WIN.blit(bg_surf, bg_rect)
    WIN.blit(ball_surf, ball_rect)
    WIN.blit(p1_surf, p1_rect)
    WIN.blit(p2_surf, p2_rect)


def player_movement():
    global p1_y, p2_y
    
    vel = 5
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_w] and p1_rect.top >= 4):
        p1_rect.y -= vel

    elif (keys[pygame.K_s] and p1_rect.bottom <= 745):
        p1_rect.y += vel

    if (keys[pygame.K_UP] and p2_rect.top >= 4):
        p2_rect.y -= vel

    elif (keys[pygame.K_DOWN] and p2_rect.bottom <= 745):
        p2_rect.y += vel    


pygame.init()

WIDTH, HEIGHT = 800, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
game_icon = pygame.image.load("assets/game_icon.png").convert_alpha()
pygame.display.set_icon(game_icon)
bg_surf = pygame.image.load("assets/pong_background.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft= (0, 0))

FPS = 60
clock = pygame.time.Clock()

p1_x, p1_y = WIDTH - 780, HEIGHT//2
p2_x, p2_y = WIDTH - 20, HEIGHT//2

p1_surf = pygame.image.load("assets/blue.png").convert_alpha()
p1_rect = p1_surf.get_rect(center= (p1_x, p1_y))
p2_surf = pygame.image.load("assets/red.png").convert_alpha()
p2_rect = p2_surf.get_rect(center= (p2_x, p2_y))
ball_surf = pygame.image.load("assets/pong-ball3.png").convert_alpha()
ball_rect = ball_surf.get_rect(center= (WIDTH/2, HEIGHT/2))


while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    draw_img()
    player_movement()
  
    pygame.display.update()