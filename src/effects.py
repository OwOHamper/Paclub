import pygame



class Effects:
    def __init__(self, screen, resolution, constants, assets) -> None:
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.constants = constants

        self.effects = []
        # {"status": "power-shield", "time_started": 0, "total_duration": 10}
        self.assets = assets
        self.shield = False
        self.game_over = False

    def reset(self):
        self.effects = []
        self.shield = False

    def add_effect(self, typeE):
        self.effects.append({"status": typeE, "time_started": pygame.time.get_ticks(), "total_duration": self.constants.EFFECTS[typeE]["total_duration"]})

    def handle_effects(self):
        for index, effect in enumerate(self.effects):
            # if effect["time_started"] > effect["total_duration"]:
            #     self.effects.pop(index)
            # else:
            #     self.effects[index]["time_started"] += 1
            match effect["status"]:
                # case "powerup":
                    # return (25, 25)
                case "powerup-shield":
                    self.shield = True
                    self.effects.pop(index)
                case "powerup-stamina":
                    pass
                case "shield-pop-immunity":
                    if self.effects[index]["time_started"] + self.constants.EFFECTS["shield-pop-immunity"]["total_duration"] < pygame.time.get_ticks():
                        self.game_over = False
                    else:
                        self.effects.pop(index)
                    
                # case "powerup-stamina":
                    # return self.assets.potions.get("green")


    # def calculate_spawnable_position(self, spawnable):
    #     if spawnable["position"] == "left":
    #         modifier = -1
    #     elif spawnable["position"] == "right":
    #         modifier = 1
    #     else:
    #         modifier = 0
    #     image = self.get_spawnable_image(spawnable)
    #     size = (image.get_width(), image.get_height())
        
    #     return  (self.width/2 + modifier * self.constants.CHARACTER_OFFSET_FROM_LOG 
    #             - (size[0]/2)
    #             + modifier * self.constants.LOG_SIZE
    #             ,
    #             spawnable["top_offset"] - size[1],

    #             *size)

    # def decrement_spawnables(self, speed):
        # for index, spawnable in enumerate(self.spawnables):
            # self.spawnables[index]["top_offset"] += 5 * speed
    
    # def display_effects(self):
        # for index, spawnable in enumerate(self.spawnables):
            # position = self.calculate_spawnable_position(spawnable)
            # if position[1] > self.height:
                # self.spawnables.pop(index)

        # for spawnable in self.spawnables:
            # image = self.get_spawnable_image(spawnable)
            # pos = self.calculate_spawnable_position(spawnable)
            # self.screen.blit(image, pos[:2])   
            # pygame.draw.rect(self.screen, (50, 50, 120), pygame.Rect(pos))
    
    