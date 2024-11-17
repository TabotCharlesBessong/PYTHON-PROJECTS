import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60
SPACE_WIDTH, SPACE_HEIGHT =  55,40
VEL = 5
BORDER = pygame.Rect(WIDTH//2 - 5 ,0,10,HEIGHT)
BULLET_VEL = 7
MAX_BULLET = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# setting bg

# Get the path to the assets directory
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets") 

# Load the image file
SPACE_IMG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))
YELLOW_SPACE_IMG = pygame.image.load(os.path.join(assets_path, "spaceship_yellow.png"))
YELLOW_SPACE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACE_IMG,(SPACE_WIDTH,SPACE_HEIGHT)),90)
RED_SPACE_IMG = pygame.transform.rotate(pygame.image.load(os.path.join(assets_path, "spaceship_red.png")),270)
RED_SPACE = pygame.transform.scale(RED_SPACE_IMG,(SPACE_WIDTH,SPACE_HEIGHT))

pygame.display.set_caption("SPACE FIGHTERS")


# Load the image file
BG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets):
  WIN.blit(BG,(0,0))
  # WIN.fill((255,255,255))
  pygame.draw.rect(WIN,(0,0,0),BORDER)
  WIN.blit(YELLOW_SPACE,(yellow.x,yellow.y))
  WIN.blit(RED_SPACE,(red.x,red.y))
  
  for bullet in red_bullets:
    pygame.draw.rect(WIN,(255,0,0),bullet)
    
  for bullet in yellow_bullets:
    pygame.draw.rect(WIN,(255,0,0),bullet)
  pygame.display.update()

def yellow_movement_handled(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
      yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
      yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
      yellow.y -= VEL
    if keys_pressed[pygame.K_z] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
      yellow.y += VEL

def red_movement_handled(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
      red.x -= VEL
    if (
        keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH
    ):  # RIGHT
      red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
      red.y -= VEL
    if (
        keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 5
    ):  # DOWN
      red.y += VEL
      
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
  for bullet in yellow_bullets:
    bullet.x += BULLET_VEL
    if red.colliderect(bullet):
      pygame.event.post(pygame.event.Event(RED_HIT))
      yellow_bullets.remove(bullet)
    elif bullet.x > WIDTH:
      yellow_bullets.remove(bullet)
      
  for bullet in red_bullets:
    bullet.x -= BULLET_VEL
    if yellow.colliderect(bullet):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
      red_bullets.remove(bullet)
    elif bullet.x < 0:
      red_bullets.remove(bullet)

def main():
  red = pygame.Rect(700,300,SPACE_WIDTH,SPACE_HEIGHT)
  yellow = pygame.Rect(100,300,SPACE_WIDTH,SPACE_HEIGHT)
  
  red_bullets = []
  yellow_bullets = []
  
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLET:
          bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height // 2 - 2, 10, 5)
          yellow_bullets.append(bullet)
        if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLET:
          bullet = pygame.Rect(red.x ,red.y + red.height // 2 - 2, 10, 5)
          red_bullets.append(bullet)
    
    # yellow.x += 1
    
    print(red_bullets,yellow_bullets)
    
    keys_pressed = pygame.key.get_pressed()
    yellow_movement_handled(keys_pressed,yellow)
    red_movement_handled(keys_pressed,red)
    
    handle_bullets(yellow_bullets,red_bullets,yellow,red)
    
    draw_window(red,yellow,red_bullets,yellow_bullets)
        
  pygame.quit()

if __name__ == "__main__":
  main()
