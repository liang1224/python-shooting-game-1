import background as background
import pygame
from pathlib import Path
from code.player import Player

pygame.init()
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

#
running = True
fps = 120
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()

# import os
# current_path = os.path.dirname(__file__)
# image_path = os.path.join(current_path, 'icons')
# resource_path = os.path.join(current_path, 'res')

parent_path = Path(__file__).parents[1]
print(parent_path)
image_path = parent_path / 'res'
print(image_path)
icon_path = image_path / 'airplaneicon.png'
print(icon_path)

#
pygame.display.set_caption("1942偽")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((50, 50, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()

#
fps = 120
movingScale = 600 / fps
player = Player(playground=playground, sensitivity=movingScale)

while running:
    screen.blit(background, (0, 0))
    player.update()
    screen.blit(player.image, player.xy)
    pygame.display.update()
    dt = clock.tick(fps)