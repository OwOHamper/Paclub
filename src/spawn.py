import pygame



class Spawn:
    def __init__(self, screen, resolution, constants) -> None:
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.constants = constants

        self.spawnables = []
        # {"position": "left", "top_offset": 0, "type": "powerup"}

    def add_spawnable(self, position, typeE):
        self.spawnables.append({"position": position, "top_offset": 0, "type": typeE})

    def get_spawnable_size(self, spawnable):
        if spawnable["type"] == "powerup":
            return (25, 25)
        # elif spawnable["type"] == "obstacle":
            # return (25, 25)

    def calculate_spawnable_position(self, spawnable):
        if spawnable["position"] == "left":
            modifier = -1
        elif spawnable["position"] == "right":
            modifier = 1
        else:
            modifier = 0
        size = self.get_spawnable_size(spawnable)
        
        return  (self.width/2 + modifier * self.constants.CHARACTER_OFFSET_FROM_LOG 
                - (size[0]/2)
                + modifier * self.constants.LOG_SIZE
                ,
                spawnable["top_offset"] - size[1],

                *size)

    def decrement_spawnables(self, speed):
        for index, spawnable in enumerate(self.spawnables):
            self.spawnables[index]["top_offset"] += 5 * speed
    
    def display_spawnables(self):
        for index, spawnable in enumerate(self.spawnables):
            position = self.calculate_spawnable_position(spawnable)
            if position[1] > self.height:
                self.spawnables.pop(index)

        for spawnable in self.spawnables:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.calculate_spawnable_position(spawnable)))
            # self.display_rocket(self.calculate_rocket_position(spawnable))