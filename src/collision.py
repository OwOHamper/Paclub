import pygame


class Collision:
    def __init__(self, calculate_character_position, Rocket, screen, constants, spawnable) -> None:
        self.calculate_character_position = calculate_character_position
        # self.calculate_rocket_position = calculate_rocket_position
        self.Rocket = Rocket
        self.screen = screen
        self.constants = constants

    def calculate_rocket_hitbox(self, rocket):
        return (self.Rocket.calculate_rocket_position(rocket)[0], 
        self.Rocket.calculate_rocket_position(rocket)[1] + self.constants.ROCKET_HITBOX_TOP_CUT,
        self.Rocket.rocket_size[2], self.Rocket.rocket_size[3] - self.constants.ROCKET_HITBOX_TOP_CUT)


    def check_rocket_collision(self):
        for rocket in self.Rocket.rockets:
            #temporary hitbox
            # pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.calculate_rocket_hitbox(rocket)))
            if pygame.Rect(self.calculate_character_position()).colliderect(
                pygame.Rect(self.calculate_rocket_hitbox(rocket))):
                return True
        return False