import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,420))
pygame.display.set_caption('pong')
screen.fill((255,255,255))
clock = pygame.time.Clock()
game_active = True
rawline = "fonts/rawline.ttf"
wall = pygame.Rect(300,150,640,25)
wall.topleft = (0,100)
wall_y = 1
# vars for held down keys
left = False
right = False
#score
font = pygame.font.Font(rawline,25)
score_count = 0 
score_surf = font.render (str(score_count),font,(255,255,255)).convert_alpha()
score_rect = score_surf.get_rect(bottomright = (50,50))

#paddle
paddle_surf = pygame.surface.Surface((150,12)).convert_alpha()
paddle_y = 400
paddle_rect = paddle_surf.get_rect(midbottom = (320,paddle_y))
paddle_surf.fill((255,255,255))

# ball
ball_y = 4
ball_x = 4
ball_surf = pygame.surface.Surface((25,25)).convert_alpha()
ball_surf.fill((255,255,255))
ball_rect = ball_surf.get_rect(midbottom = (320,150))

# the white backround
backround_surf = pygame.surface.Surface((640,480)).convert_alpha()
backround_surf.fill((0,0,0))

# defines the reset function
def reset():
  paddle_rect.midbottom = 320,paddle_y
  ball_rect.midbottom = 320,150 
  wall.topleft = (0,100)
  ball_y = 4
  ball_x = 4
  
# defines the game over function    
def game_over():
  final_score_font = pygame.font.Font(rawline,40)
  gameover_font = pygame.font.Font('fonts/pixel_type.ttf',150)
  gameover = gameover_font.render('game over',gameover_font,'red')
  gameover_rect = gameover.get_rect(midbottom = (320,190))

  
  final_score = final_score_font.render('score = '+str(score_count),final_score_font,(255,255,255))
  final_txt_rect2 = final_score.get_rect(midbottom = (320,250))
  
  enter = pygame.font.Font(rawline,18)
  enter_surf = enter.render('press [enter] to restart',enter,(255,255,255))
  enter_rect = enter_surf.get_rect(bottomleft= (220,275))
  screen.fill((0,0,0))
  
  screen.blit(gameover,gameover_rect)
  screen.blit(final_score ,final_txt_rect2)
  screen.blit(enter_surf,enter_rect)
  
screen_wait = 1

while  True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_active == True:  
      
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            left = True
          if event.key == pygame.K_RIGHT:
            right = True
      
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left = False
        if event.key == pygame.K_RIGHT:
            right = False

    if game_active == False:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          reset()
          screen_wait = 1
          score_count = 0
          game_active = True
          
  if game_active:    
# moves the ball 
    ball_rect.x = ball_rect.x + ball_x
    ball_rect.y = ball_rect.y + ball_y
    wall.y  += wall_y
    score_surf = font.render ('your score = '+str(score_count),font,(255,255,255))  

# detects if keys are held down
    if right == True:
      paddle_rect.x += 5
      
    elif left == True:
      paddle_rect.x -= 5
    # makes the paddle unable to go off the screen
    if paddle_rect.right >=  640 or paddle_rect.left <= 0 :
      if paddle_rect.left <= 0 :
        paddle_rect.left = 0
      if paddle_rect.right >= 640:
        paddle_rect.right = 640 
        
  # blits all the surfaces  
    
    screen.blit(backround_surf,(0,0))
    screen.blit(score_surf,(score_rect))  
    screen.blit(paddle_surf,paddle_rect)
    screen.blit(ball_surf,ball_rect)
    pygame.draw.rect(screen,(255,255,255),wall,0)


  # waits 2 seconds at the start of the program  
    if screen_wait == 1:
      pygame.display.flip()
      pygame.display.update()
      pygame.time.delay(2000)
      screen_wait = 2
  #####################################   
  #bouncing of the window
     
  # top and bottom 
    if ball_rect.colliderect(wall) and ball_y <0:
      score_count += 1
      ball_y *= -1
  
  # sides of window  
    if ball_rect.left <= 0 or ball_rect.right >= 640:
      ball_x *= -1
  #####################################
    if wall.bottom >= 200 :
      wall_y *= -1
    elif wall.top <= 90:
      wall_y *= -1
  # detects when ball collides with the paddle
    collision_tolerance = 10

    if ball_rect.colliderect(paddle_rect):
      if abs(paddle_rect.top - ball_rect.bottom )< collision_tolerance and ball_y >0:
        ball_y *= -1
      if abs(paddle_rect.left - ball_rect.right) < collision_tolerance and ball_x <0:
        ball_x *= -1
      if abs(paddle_rect.right - ball_rect.left )< collision_tolerance and ball_x <0:
        ball_x *= -1
      if ball_rect.collidepoint(paddle_rect.topleft) and ball_x >0:
        ball_y *=-1
        ball_x *= -1
      if ball_rect.collidepoint(paddle_rect.topright)  and ball_x <0:
        ball_y *=-1
        ball_x *= -1  
      elif ball_rect.colliderect(paddle_rect) and ball_y > 0 and ball_x <0:
        ball_y *= -1
      
# detects when the ball  goes behind the paddle 
    if ball_rect.top >= 400:
      game_active = False

  else:
    game_over()
  
  clock.tick(60) 
  pygame.display.flip()   
  pygame.display.update()
