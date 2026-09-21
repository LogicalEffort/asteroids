import asteroid
from asteroid import Asteroid
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from asteroidfield import AsteroidField
import pygame
import sys


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_Field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)




    while True: #Game Loop
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        #limits FPS to 60
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
