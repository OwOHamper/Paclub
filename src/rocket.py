import pygame




class Rocket:
    def __init__(self, display_rocket, rocket_size, resolution):
        self.display_rocket = display_rocket
        self.rocket_size = rocket_size
        self.rockets = []
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]


    def reset(self):
        self.rockets = []

    def add_rocket(self):
        self.rockets.append({"top_offset": 0})


    def calculate_rocket_position(self, rocket):
        return (self.width/2 - self.rocket_size[2]/2, rocket["top_offset"] - self.rocket_size[2])

    def display_rockets(self):
        for index, rocket in enumerate(self.rockets):
            position = self.calculate_rocket_position(rocket)
            if position[1] > self.height:
                self.rockets.pop(index)

        for rocket in self.rockets:
            self.display_rocket(self.calculate_rocket_position(rocket))
        
    def decrement_rockets(self, speed):
        for index, rocket in enumerate(self.rockets):
            self.rockets[index]["top_offset"] += 15 * speed
