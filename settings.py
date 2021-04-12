import pygame

class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('images/deep_stars.jpg')
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 200
        # Game setting: 3; Test setting: 300; CRT Refresh mode: 3000
        #self.bullet_width = 3
        #self.bullet_height = 15

        # Testing laser bullets
        self.bullet_width = 5
        self.bullet_height = 500

        self.bullet_color = (255, 95, 31) # Neon orange
        self.bullets_allowed = 1

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100 # Change back to 10 for regular gameplay
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1