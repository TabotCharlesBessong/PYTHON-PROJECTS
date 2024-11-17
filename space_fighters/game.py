import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60
SPACE_WIDTH, SPACE_HEIGHT =  55,40
VEL = 5
BORDER = pygame.Rect(WIDTH/2 - 5 ,0,10,HEIGHT)

# setting bg

# Get the path to the assets directory
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets") 

# Load the image file
# YELLO_SPACE_IMG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))
YELLOW_SPACE_IMG = pygame.image.load(os.path.join(assets_path, "spaceship_yellow.png"))
YELLOW_SPACE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACE_IMG,(SPACE_WIDTH,SPACE_HEIGHT)),90)
RED_SPACE_IMG = pygame.transform.rotate(pygame.image.load(os.path.join(assets_path, "spaceship_red.png")),270)
RED_SPACE = pygame.transform.scale(RED_SPACE_IMG,(SPACE_WIDTH,SPACE_HEIGHT))

pygame.display.set_caption("SPACE FIGHTERS")


# Load the image file
BG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))

def draw_window(red,yellow):
  WIN.fill((255,255,255))
  pygame.draw.rect(WIN,(0,0,0),BORDER)
  WIN.blit(YELLOW_SPACE,(yellow.x,yellow.y))
  WIN.blit(RED_SPACE,(red.x,red.y))
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

def main():
  red = pygame.Rect(700,300,SPACE_WIDTH,SPACE_HEIGHT)
  yellow = pygame.Rect(100,300,SPACE_WIDTH,SPACE_HEIGHT)
  
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    
    # yellow.x += 1
    
    keys_pressed = pygame.key.get_pressed()
    yellow_movement_handled(keys_pressed,yellow)
    red_movement_handled(keys_pressed,red)
    
    draw_window(red,yellow)
        
  pygame.quit()

if __name__ == "__main__":
  main()
