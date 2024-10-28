import pygame
import time
import random
import os


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

pygame.display.set_caption("Space Dodge")

# setting bg

# Get the path to the assets directory
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# Load the image file
BG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))


def draw(player):
  WIN.blit(BG,(0,0))
  pygame.draw.rect(WIN,(255,0,0),player)
  pygame.display.update()

# main game loop
def main():
  run = True
  
  player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
  
  clock = pygame.time.Clock()
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
      player.x -= PLAYER_VEL
      
    if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
      player.x += PLAYER_VEL
    
    draw(player)
    
  pygame.quit()

if __name__ == "__main__":
  main()
