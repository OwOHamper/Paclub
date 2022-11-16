import pygame
import random

class Game:
    def __init__(self, screen, resolution, constants) -> None:
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.character_side = "left"

        self.constants = constants

        self.obstacles = []
        self.speed = 1
        self.last_three_obstacles = []
        self.counter = 0

    def reset(self):
        self.obstacles = []
        self.speed = 1
        self.character_side = "left"
        self.last_three_obstacles = []

    def set_params(self, display_obstacle, display_character, assets):
        self.display_obstacle = display_obstacle
        self.display_character = display_character
        self.assets = assets

    def update_side(self, side):
        if side == "right":
            if self.character_side == "left":
                self.character_side = "center"
            elif self.character_side == "center":
                self.character_side = "right"
        elif side == "left":
            if self.character_side == "right":
                self.character_side = "center"
            elif self.character_side == "center":
                self.character_side = "left"
 
    def add_obstacle(self):
        all_left = True
        all_right = True
        for obstacle in self.last_three_obstacles:
            if obstacle == "left":
                all_right = False
            elif obstacle == "right":
                all_left = False
        if all_left or all_right:
            if all_left:
                current_choice = "right"
            else:
                current_choice = "left"
        else:
            current_choice = random.choice(("left", "right"))
        self.last_three_obstacles.append(current_choice)
        if len(self.last_three_obstacles) > 3:
            self.last_three_obstacles.pop(0)
        self.obstacles.append({"position": current_choice, "top_offset": 0})
    
    def check_for_collision(self):
        for obstacle in self.obstacles:
            if pygame.Rect(self.calculate_character_hitbox_position()).colliderect(pygame.Rect(self.calculate_obstacle_position(obstacle))):
                return True
        return False

    def decrement_obstacles(self):
        for index, obstacle in enumerate(self.obstacles):
            self.obstacles[index]["top_offset"] += 5 * self.speed

    def draw_log(self):
        # pygame.draw.rect(self.screen, (105, 90, 76), pygame.Rect(self.width/2 - self.constants.LOG_SIZE/2, 0,
                                                                # self.constants.LOG_SIZE, self.height))
        pass

    def calculate_character_position(self):
        if self.character_side == "left":
            modifier = -1
        elif self.character_side == "right":
            modifier = 1
        else:
            modifier = 0
        # modifier = -1  elif self.character_side_on_left == "right" 1 else 0
        return (self.width/2 + modifier * self.constants.CHARACTER_OFFSET_FROM_LOG 
            - (self.assets.character[0].get_width()/2)
                + modifier * self.constants.LOG_SIZE
                ,
                self.height -
                self.assets.character[0].get_height()*2,

                self.assets.character[0].get_width(),
                
                self.assets.character[0].get_height())

    def calculate_character_hitbox_position(self):
        if self.character_side == "left":
            modifier = -1
        elif self.character_side == "right":
            modifier = 1
        else:
            modifier = 0
        # modifier = -1  elif self.character_side_on_left == "right" 1 else 0
        return (self.width/2 + modifier * self.constants.CHARACTER_OFFSET_FROM_LOG 
            - (self.constants.CHARACTER_SIZE/2)
                + modifier * self.constants.LOG_SIZE
                ,
                self.height -
                self.constants.CHARACTER_SIZE*2,

                self.constants.CHARACTER_SIZE,
                
                self.constants.CHARACTER_SIZE)

    def calculate_shield_position(self):
        if self.character_side == "left":
            modifier = -1
        elif self.character_side == "right":
            modifier = 1
        else:
            modifier = 0
        # modifier = -1  elif self.character_side_on_left == "right" 1 else 0
        return (self.width/2 + modifier * self.constants.CHARACTER_OFFSET_FROM_LOG 
            - (self.assets.shield.get_width()/2)
                + modifier * self.constants.LOG_SIZE
                ,
                self.height -
                self.assets.shield.get_height()*1.3,

                self.assets.shield.get_width(),
                
                self.assets.shield.get_height())

    def calculate_obstacle_position(self, obstacle):
        modifier = -1 if obstacle["position"] == "left" else 1
        if modifier == -1:
            obstacle_substraction = (self.constants.OBSTACLE_SIZE[0])
            obs_x = 0
        else:
            obstacle_substraction = 0
            obs_x = self.width - self.constants.OBSTACLE_SIZE[0]
        return (obs_x
                # self.width/2
                # - obstacle_substraction
                # + modifier * self.constants.LOG_SIZE/2
                ,
                obstacle["top_offset"] - self.constants.OBSTACLE_SIZE[1],

                self.constants.OBSTACLE_SIZE[0],
                
                self.constants.OBSTACLE_SIZE[1])

    def draw_character(self, shield, immunity):
        # pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.calculate_character_position()))
        pos = self.calculate_character_position()
        shield_pos = self.calculate_shield_position()
        self.screen.blit(self.assets.character[int(self.counter/5)], pos)
        if shield:
            self.assets.shield.set_alpha(150)
            self.screen.blit(self.assets.shield, shield_pos)
        if immunity:
            self.assets.shield.set_alpha(50)
            self.screen.blit(self.assets.shield, shield_pos)
        self.counter += 1
        if self.counter >= 5*len(self.assets.character):
            self.counter = 0

    def draw_obstacles(self):
        for index, obstacle in enumerate(self.obstacles):
            position = self.calculate_obstacle_position(obstacle)
            if position[1] > self.height:
                self.obstacles.pop(index)
        for obstacle in self.obstacles:
            position = self.calculate_obstacle_position(obstacle)
            # pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.calculate_obstacle_position(obstacle)))
            self.display_obstacle(position)