import pygame 
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 800))
screen_width = screen.get_width()
screen_height = screen.get_height()
clock = pygame.time.Clock()

# load background image
background = pygame.image.load('pong.png').convert_alpha()
background = pygame.transform.rotate(background, 90)
background = pygame.transform.smoothscale(background, (screen_width, screen_height))

# load game points 
pygame.font.init()
font = pygame.font.Font("ARCADECLASSIC.TTF", 36) 
player1_points = 0
player2_points = 0

running = True
dt = 0
player1_width = 50
player2_width = 50
ball_radius = 10

#ball speed
ball_dx = 3
ball_dy = 3

#game objects
player1 = pygame.Rect((screen_width - player1_width) / 2, 50, 70, 20)
player2 = pygame.Rect((screen_width - player2_width) / 2, 740, 70, 20)
ball = pygame.Rect(screen_width / 2, screen_height / 2, 10, 10)
pygame.mouse.set_visible(0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # points text
    text = font.render(str(player1_points) + " : " + str(player2_points), True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(text, ((screen_width / 2) - 25, (screen_height / 2)))

    # draw game objects
    pygame.draw.rect(screen, (0, 0, 255), player1)
    pygame.draw.rect(screen, (255, 0, 0), player2)
    pygame.draw.circle(screen, (255, 255, 255), ball.center, ball.width / 2)

    # ball movement
    ball.x = ball.x + ball_dx
    ball.y = ball.y + ball_dy

    if ball.left < 0 or ball.right > screen_width:
        ball_dx *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dy *= -1
    if ball.top < 0:
        player2_points += 1
        ball.x = screen_width / 2
        ball.y = screen_height / 2
        ball_dx = random.choice([-1, 1]) * 3
        ball_dy = random.choice([-1, 1]) * 3
        ball_dx = ball_dx * 1.15
        ball_dy = ball_dy * 1.15
        ball_radius = ball_radius * 1.25
        ball.width = ball.height = ball_radius
        pygame.draw.circle(screen, (255, 255, 255), ball.center, ball_radius)
    if ball.bottom > screen_height:
        player1_points += 1
        ball.x = screen_width / 2
        ball.y = screen_height / 2
        ball_dx = random.choice([-1, 1]) * 3
        ball_dy = random.choice([-1, 1]) * 3
        ball_dx = ball_dx * 1.15
        ball_dy = ball_dy * 1.15
        ball_radius = ball_radius * 1.25
        ball.width = ball.height = ball_radius
        pygame.draw.circle(screen, (255, 255, 255), ball.center, ball_radius)

    # player wins
    if player1_points == 7 or player2_points == 7:
        screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1.x -= 300 * dt
        if player1.x < 0:
            player1.x = 0
    if keys[pygame.K_d]:
        player1.x += 300 * dt
        if player1.x > screen_width - player1.width:
            player1.x = screen_width - player1.width

    if keys[pygame.K_LEFT]:
        player2.x -= 300 * dt
        if player2.x < 0:
            player2.x = 0
    if keys[pygame.K_RIGHT]:
        player2.x += 300 * dt
        if player2.x > screen_width - player2.width:
            player2.x = screen_width - player2.width

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()