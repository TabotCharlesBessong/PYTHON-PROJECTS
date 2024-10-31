import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("SPACE FIGHTERS")

# setting bg

# Get the path to the assets directory
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# Load the image file
BG = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "space.png")),(WIDTH,HEIGHT))

def draw_window():
  WIN.fill((255,255,255))
  pygame.display.update()

def main():
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    
    draw_window()
        
  pygame.quit()
  
if __name__ == "__main__":
  main()