import pygame
import random

#General setup
pygame.init()
clock = pygame.time.Clock()

#Setting window
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")
icon = pygame.image.load("pong.png")
pygame.display.set_icon(icon)

background = pygame.image.load('1195724.jpg')


#Speed
ball_speed_x = 9
ball_speed_y = 9
player_speed = 9
def ball_restart():
    global ball_speed_x ,ball_speed_y
    ball.x = screen_width/2-15
    ball.y = screen_height/2-15
    ball_speed_x = 9 * random.choice((1,-1))
    ball_speed_y = 9 * random.choice((1,-1))
#Definition
score_player1 = 0
score_player2 = 0


y = screen_height/2-100
x = screen_height/2-100
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
def ball_animation():
    global ball_speed_y, ball_speed_x,score_player1,score_player2
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1.05

    if ball.right >= screen_width:
        score_player1 += 1
        ball_restart()
    if ball.left <= 0:
        score_player2 += 1
        ball_restart()
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1.05


def player_animation():
    #Movement
    keys = pygame.key.get_pressed()
    global x,y
    if keys[pygame.K_UP]:
        y -= player_speed
    if keys[pygame.K_DOWN]:
        y += player_speed
    if keys[pygame.K_w]:
        x -= player_speed
    if keys[pygame.K_s]:
        x += player_speed

    if x <= 0:
        x =0
    if x >= screen_height-200:
        x = screen_height-200
    if y <= 0:
        y = 0
    if y >= screen_height-200:
        y = screen_height-200
    
    

run = True
while run:
    #Game setup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Updating window
    
    screen.blit(background, (0,0))
    pygame.display.flip()
    clock.tick(60)


    #Graphics
    screen.fill("black")
    pygame.draw.ellipse(screen,(255,255,255),ball)
    player1 = pygame.draw.rect(screen,(255,255,255),(0,x,9,200))
    player2 = pygame.draw.rect(screen,(255,255,255),(screen_width-10,y,9,200))
    pygame.draw.line(screen,(255,255,255),(screen_width/2-1,0),(screen_width/2-1,screen_height),2)
    font1 = pygame.font.SysFont("comicsans",50)
    text1 = font1.render("Score:" + str(score_player1),1,(225,225,225))
    font2 = pygame.font.SysFont("comicsans",50)
    text2 = font2.render("Score:" + str(score_player2),1,(225,225,225))
    screen.blit(text1,(0,0))
    screen.blit(text2,(screen_width-text2.get_width(),0))


    pygame.display.update()
    
    
    #Animation
    ball_animation()
    player_animation()
