import pygame, sys

def draw_img():
    global START_GAME, GAME_END, point_font, point_2, point_rect_1, point_rect_2

    point_font = FONT.render(f"{p1_score}", False, "white")
    point_2 = FONT.render(f"{p2_score}", False, "white")
    point_rect_1 = point_font.get_rect(topleft= (300, 50))
    point_rect_2 = point_font.get_rect(topleft= (500, 50))

    WIN.blit(bg_surf, bg_rect)
    WIN.blit(point_font, point_rect_1)
    WIN.blit(point_2, point_rect_2)
    WIN.blit(ball_surf, ball_rect)
    WIN.blit(p1_surf, p1_rect)
    WIN.blit(p2_surf, p2_rect)
    if START_GAME is False:
        WIN.blit(button_surf, button_rect)


def player_movement():
    global p1_y, p2_y
    
    if START_GAME:
        vel = 6
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] and p1_rect.top >= 4):
            p1_rect.y -= vel

        elif (keys[pygame.K_s] and p1_rect.bottom <= 745):
            p1_rect.y += vel

        if (keys[pygame.K_UP] and p2_rect.top >= 4):
            p2_rect.y -= vel

        elif (keys[pygame.K_DOWN] and p2_rect.bottom <= 745):
            p2_rect.y += vel 
   

# https://nwachukwu.itch.io/full-pong-game-sound-kit
speed = [4, 4]
def ball_movement():
    global speed, WIDTH, HEIGHT

    if START_GAME:
        global p1_score, p2_score

        ball_rect.move_ip(speed)

        if ball_rect.left <= -40:
            p2_score += 1
            reset()

        if ball_rect.right >= WIDTH + 40:
            p1_score += 1
            reset()

        if ball_rect.colliderect(p1_rect) or ball_rect.colliderect(p2_rect):
            HIT_SOUND.play()
            speed[0] = -speed[0]

        if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
            HIT_SOUND.play()
            speed[1] = -speed[1]


def reset():

    ball_rect.x = WIDTH/2
    ball_rect.y = HEIGHT/2


def restart():
    global START_GAME, p1_score, p2_score

    ball_rect.x = WIDTH/2
    ball_rect.y = HEIGHT/2
    p1_rect.x = WIDTH - 780
    p1_rect.y = HEIGHT//2
    p2_rect.x = WIDTH - 20
    p2_rect.y = HEIGHT//2
    p1_score = 0
    p2_score = 0
    START_GAME = False

pygame.init()

WIDTH, HEIGHT = 800, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
game_icon = pygame.image.load("assets/game_icon.png").convert_alpha()
pygame.display.set_icon(game_icon)
bg_surf = pygame.image.load("assets/pong_background.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft= (0, 0))
button_surf = pygame.image.load("assets/play-button.png").convert_alpha()
button_rect = button_surf.get_rect(center= (WIDTH/2, HEIGHT/2))
FONT = pygame.font.Font("assets/pixel-font.ttf", 50)
p1_score = 0
p2_score = 0


FPS = 60
clock = pygame.time.Clock()

GAME_MUSIC = pygame.mixer.Sound("assets/song.mp3")
GAME_MUSIC.play(loops= 1_000)
HIT_SOUND = pygame.mixer.Sound("assets/bounce.wav")

p1_x, p1_y = WIDTH - 780, HEIGHT//2
p2_x, p2_y = WIDTH - 20, HEIGHT//2

p1_surf = pygame.image.load("assets/blue.png").convert_alpha()
p1_rect = p1_surf.get_rect(center= (p1_x, p1_y))
p2_surf = pygame.image.load("assets/red.png").convert_alpha()
p2_rect = p2_surf.get_rect(center= (p2_x, p2_y))
ball_surf = pygame.image.load("assets/pong-ball3.png").convert_alpha()
ball_rect = ball_surf.get_rect(center= (WIDTH/2, HEIGHT/2))

START_GAME = False

while True:

    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        elif (event.type == pygame.MOUSEBUTTONDOWN):
            if (button_rect.collidepoint(mouse_pos) and START_GAME is False):
                START_GAME = True

        elif (keys[pygame.K_ESCAPE]):
            restart()

    draw_img()
    player_movement()
    ball_movement()
  
    pygame.display.update()