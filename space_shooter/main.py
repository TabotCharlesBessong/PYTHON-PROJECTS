import pygame 
from os.path import join

from random import randint, uniform

class Player(pygame.sprite.Sprite):
  def __init__(self,groups):
    super().__init__(groups)
    self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
    self.rect = self.image.get_frect(center = (640, 360))
    self.direction = pygame.math.Vector2()
    self.speed = 300
    
    # cooldown timer for firing
    self.can_shoot = True
    self.laser_shoot_time = 0
    self.cooldown_duration = 400
    
  def laser_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_shoot_time >= self.cooldown_duration * 1000:
        self.can_shoot = True
    
  def update(self, dt):
    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    self.direction = self.direction.normalize() if self.direction else self.direction
    self.rect.center += self.direction * self.speed * dt
    
    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE] and self.can_shoot :
      # print('fire laser')
      Laser(laser_surf,self.rect.midtop, all_sprites)
      self.can_shoot = False
      self.laser_shoot_time = pygame.time.get_ticks()
    self.laser_timer()
      
      
class Star(pygame.sprite.Sprite):
  def __init__(self, groups,surf):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
    
    
class Laser(pygame.sprite.Sprite):
  def __init__(self,surf,pos,groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(midbottom = pos)
    
  def update(self,dt):
    self.rect.centery -= 400 * dt
    if self.rect.bottom < 0:
      self.kill()
      
class Meteor(pygame.sprite.Sprite):
  def __init__(self,surf,pos,groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(center = pos)
    self.start_time = pygame.time.get_ticks()
    self.lifetime = 3000
    self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
    self.speed = randint(400, 500)
    
  def update(self,dt):
    self.rect.center += self.direction * self.speed * dt
    if pygame.time.get_ticks() - self.start_time > self.lifetime:
      self.kill()

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.Clock()

# plain surface 
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# sprites
all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
  Star(all_sprites, star_surf)
player = Player(all_sprites)

# imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,WINDOW_HEIGHT - 20))

# custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)  # every half second

while running:
  dt = clock.tick() / 1000
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == meteor_event:
      x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
      Meteor(meteor_surf, (x, y), all_sprites)
  # update
  all_sprites.update(dt)

  # draw the game
  display_surface.fill('darkgray')
  all_sprites.draw(display_surface)
  pygame.display.update()

pygame.quit()