import pygame
from pathlib import Path


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
