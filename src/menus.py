import pygame


class Menus:
    def __init__(self, resolution, constants, assets) -> None:
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.constants = constants
        self.assets = assets

    def check_for_hover(self, mouse_pos, button, button_pos):
        # print(button.get_rect())
        # print(button_pos)
        rect_sum = [rect + button_pos[index%2] for index, rect in enumerate(button.get_rect())]
        if mouse_pos[0] > rect_sum[0] and mouse_pos[0] < rect_sum[2] and mouse_pos[1] > rect_sum[1] and mouse_pos[1] < rect_sum[3]:
            return True
        else:
            return False

    def check_for_click(self, mouse_pos, button, button_pos):
        if self.check_for_hover(mouse_pos, button, button_pos):
            return True
        else:
            return False

    def get_button_position(self, button, y_offset=0):
        return (self.width/2 - button.get_width()/2, self.height/2 - button.get_height() + y_offset)