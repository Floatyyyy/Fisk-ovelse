import pygame
from Vektor import Vector

# Initialiser Pygame
pygame.init()

# Skærmindstillinger
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load fiskens billede
fish_image = pygame.image.load('Fish.png')

# Startposition for fisken
position = Vector(100, 100)

# Hastighed (velocity) for fisken
velocity = Vector(1, 1)

# Spil loop
running = True
while running:
    # Håndterer hændelser (event handling)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Opdater fiskens position
    position = position + velocity

    # Tjek for grænser (hvis fisken rammer kanten, vend om)
if position.x < 0 or position.x > screen_width - fish_image.get_width():
    velocity = Vector(-velocity.x, velocity.y)  
if position.y < 0 or position.y > screen_height - fish_image.get_height():
    velocity = Vector(velocity.x, -velocity.y)  


    # Fyld skærmen med sort farve (sletter tidligere tegning)
    screen.fill((0, 0, 0))

    # Tegn fisken på den nye position
    screen.blit(fish_image, (position.x, position.y))

    # Opdater skærmen
    pygame.display.flip()

    # Begræns hastigheden af løkken (FPS)
    pygame.time.Clock().tick(60)

# Luk Pygame ordentligt ned
pygame.quit()

  


