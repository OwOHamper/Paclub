import pygame



class Spawn:
    def __init__(self, screen, resolution, constants, assets) -> None:
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.constants = constants

        self.spawnables = []
        self.assets = assets
        # {"position": "left", "top_offset": 0, "type": "powerup"}

    def reset(self):
        self.spawnables = []

    def add_spawnable(self, position, typeE):
        self.spawnables.append({"position": position, "top_offset": 0, "type": typeE})

    def get_spawnable_image(self, spawnable):
        match spawnable["type"]:
            case "powerup":
                return (25, 25)
            case "powerup-shield":
                return self.assets.potions.get("blue")
            case "powerup-stamina":
                return self.assets.potions.get("green")

    def calculate_spawnable_position(self, spawnable):
        if spawnable["position"] == "left":
            modifier = -1
        elif spawnable["position"] == "right":
            modifier = 1
        else:
            modifier = 0
        image = self.get_spawnable_image(spawnable)
        size = (image.get_width(), image.get_height())
        
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
            image = self.get_spawnable_image(spawnable)
            pos = self.calculate_spawnable_position(spawnable)
            self.screen.blit(image, pos[:2])   
            # pygame.draw.rect(self.screen, (50, 50, 120), pygame.Rect(pos))
    
