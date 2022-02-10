import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,420))
pygame.display.set_caption('pong')
screen.fill((255,255,255))
clock = pygame.time.Clock()
game_active = True

#wall
wall = pygame.Rect(300,150,640,25)
wall.bottomleft = (0,100)

#score
font = pygame.font.Font('font.ttf',50)
score_count = 0 
score_surf = font.render (str(score_count),font,(255,255,255)).convert_alpha()
score_rect = score_surf.get_rect(topright = (50,50))

#paddle
paddle_surf = pygame.surface.Surface((150,25)).convert_alpha()
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
  ball_y = 4
  ball_x = 4
  
# defines the game over function    
def game_over():
  final_font2 = pygame.font.Font('normal_font.ttf',40)
  
  
  
  
  final_font = pygame.font.Font('font.ttf',150)
  final_text = final_font.render('game over',final_font,'red')
  final_txt_rect = final_text.get_rect(midbottom = (320,190))

  
  final_text2 = final_font2.render('score = '+str(score_count),final_font2,(255,255,255))
  final_txt_rect2 = final_text2.get_rect(midbottom = (320,250))
  
  enter = pygame.font.Font('normal_font.ttf',25)
  enter_surf = enter.render('press [enter] to restart',enter,(255,255,255))
  enter_rect = enter_surf.get_rect(bottomleft= (220,275))
  screen.fill((0,0,0))
  
  screen.blit(final_text,final_txt_rect)
  screen.blit(final_text2,final_txt_rect2)
  screen.blit(enter_surf,enter_rect)
  
screen_wait = 1

while  True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_active == True:  
      
      if event.type == pygame.MOUSEMOTION:
          paddle_rect.centerx = event.pos[0] 

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
    score_surf = font.render (str(score_count),font,(255,255,255))  

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
    if ball_rect.top <= 100 or ball_rect.bottom >= 480:
      ball_y *= -1
  
  # sides of window  
    if ball_rect.left <= 0 or ball_rect.right >= 640:
      ball_x *= -1
  #####################################
  # detects when ball collides with the paddle
    collision_tolerance = 10

    if ball_rect.colliderect(paddle_rect):
      score_count += 1
      if abs(paddle_rect.top - ball_rect.bottom )< collision_tolerance and ball_y >0:
        ball_y *= -1
      if abs(paddle_rect.left - ball_rect.right) < collision_tolerance and ball_y <0:
        ball_rect.x *= -1
      if abs(paddle_rect.right - ball_rect.left )< collision_tolerance and ball_x <0:
        ball_rect.x *= -1
      
          
# detects when the ball  goes behind the paddle 
    if ball_rect.top >= 400:
      game_active = False

  else:
    game_over()
  
  clock.tick(60) 
  pygame.display.flip()   
  pygame.display.update()
  
