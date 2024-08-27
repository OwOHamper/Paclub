import pygame



class Assets:
    def __init__(self, screen, resolution, constants) -> None:
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]

        self.constants = constants

        # self.currect_offsets = [0, ]

    def load_image(self, path):
        return pygame.image.load(path).convert_alpha()

    def display_image(self, image, position):
        self.screen.blit(image, position)

    def scale_image(self, image, scale):
        return pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    
    def rotate_image(self, image, angle):
        return pygame.transform.rotate(image, angle)

    def load_images(self):
        self.character = []
        for i in range(1, 14):
            self.character.append(self.load_image(f"assets/steve/{i+1}.png"))
        self.background = self.load_image(self.constants.BACKGROUND_PATH)
        self.obstacle = self.load_image(self.constants.OBSTACLE_PATH)
        self.rocket = self.load_image(self.constants.ROCKET_PATH)
        self.rocket = self.scale_image(self.rocket, 0.5)
        self.rocket = self.rotate_image(self.rocket, 135)
        # self.rocket.resize()

        self.blue_potion = self.load_image(self.constants.BLUE_POTION_PATH)
        self.green_potion = self.load_image(self.constants.GREEN_POTION_PATH)
        self.pink_potion = self.load_image(self.constants.PINK_POTION_PATH)
        self.yellow_potion = self.load_image(self.constants.YELLOW_POTION_PATH)

        self.potions = {
            "blue": self.blue_potion,
            "green": self.green_potion,
            "pink": self.pink_potion,
            "yellow": self.yellow_potion
        }
        self.shield = self.load_image(self.constants.SHIELD_PATH)
        self.shield = self.scale_image(self.shield, 0.4)
        self.danger = self.load_image(self.constants.DANGER_PATH)

        # self.display_title = self.load_image(self.constants.DISPLAY_TITLE_PATH)
        self.play_button = self.load_image(self.constants.PLAY_BUTTON_PATH)
        self.play_button_hover = self.load_image(self.constants.PLAY_BUTTON_HOVER_PATH)
        self.options_button = self.load_image(self.constants.OPTIONS_BUTTON_PATH)
        self.options_button_hover = self.load_image(self.constants.OPTIONS_BUTTON_HOVER_PATH)
        self.quit_button = self.load_image(self.constants.QUIT_BUTTON_PATH)
        self.quit_button_hover = self.load_image(self.constants.QUIT_BUTTON_HOVER_PATH)


    def display_background(self, offset):
        self.display_image(self.background, (0, offset))

    def display_obstacle(self, position):
        self.display_image(self.obstacle, position)

    def display_character(self, position):
        self.display_image(self.character, position)
    
    def display_rocket(self, position):
        self.display_image(self.rocket, position)

    def get_rocket_size(self):
        return self.rocket.get_rect()
