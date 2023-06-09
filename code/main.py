import pygame
from pathlib import Path
from code.player import Player
from code.mymissile import MyMissile

pygame.init()
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

# import os
# current_path = os.path.dirname(__file__)
# image_path = os.path.join(current_path, 'icons')
# resource_path = os.path.join(current_path, 'res')

#
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

#
running = True
fps = 120
clock = pygame.time.Clock()

movingScale = 600 / fps
player = Player(playground=playground, sensitivity=movingScale)

#
keyCountX = 0
keyCountY = 0
Missiles = []

#
launchMissile = pygame.USEREVENT + 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #
        if event.type == launchMissile:
            m_x = player.xy[0] + 20
            m_y = player.xy[1]
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
            m_x = player.xy[0] + 80
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))

        #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()

            if event.key == pygame.K_SPACE:
                m_x = player.x + 20
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player.x + 80
                Missiles.append(MyMissile(playground, (m_x, m_y), movingScale))

                pygame.time.set_timer(launchMissile, 400)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1

            #
            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile, 0)

    screen.blit(background, (0, 0))

    Missiles = [item for item in Missiles if item.available]
    for m in Missiles:
        m.update()
        screen.blit(m.image, m.xy)

    player.update()
    screen.blit(player.image, player.xy)

    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()
