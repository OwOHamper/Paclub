import pygame


class Font:
    def __init__(self, screen, resolution, constants):
        self.screen = screen
        self.constants = constants
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]

    def load_system_font(self, font_name, font_size):
        return pygame.font.SysFont(font_name, font_size)

    def load_font(self, font_name, font_size):
        match font_name:
            case "D3":
                return pygame.font.Font(self.constants.FONT_D3, font_size)

        return pygame.font.SysFont(font_name, font_size)


    def render_font(self, fontName, size, text, color, position, center=False, outline=0, outline_color=(0, 0, 0)):
        font = self.load_font(fontName, size)
        t = font.render(text, True, color)
        if center:
            if outline > 0:
                # t_font = self.load_font(fontName, size + outline)
                t_outline = font.render(text, True, outline_color)
                # t_outline = pygame.transform.smoothscale(t_outline, (t_outline.get_width() + outline, t_outline.get_height() + outline))
                orig_pos = (position[0] - t_outline.get_width() / 2, position[1] - t_outline.get_height() / 2)
                self.screen.blit(t_outline, (orig_pos[0] + outline, orig_pos[1] + outline))
                self.screen.blit(t_outline, (orig_pos[0] + outline, orig_pos[1] - outline))
                self.screen.blit(t_outline, (orig_pos[0] - outline, orig_pos[1] + outline))
                self.screen.blit(t_outline, (orig_pos[0] - outline, orig_pos[1] - outline))


            self.screen.blit(t, (position[0] - t.get_width() / 2, position[1] - t.get_height() / 2))
        else:
            if outline > 0:
                t_font = self.load_font(fontName, size + outline)
                t_outline = t_font.render(text, True, outline_color)
                orig_pos (position[0], position[1])
                self.screen.blit(t_outline, (position[0] + outline, position[1] + outline))
                self.screen.blit(t_outline, (position[0] + outline, position[1] - outline))
                self.screen.blit(t_outline, (position[0] - outline, position[1] + outline))
                self.screen.blit(t_outline, (position[0] - outline, position[1] - outline))
            self.screen.blit(t, position)
