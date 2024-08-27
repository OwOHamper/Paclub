import pygame
from src.game import Game
from src.assets import Assets
from src.rocket import Rocket
from src.collision import Collision
from src.spawn import Spawn
from src.effects import Effects
from src.menus import Menus
from src.font import Font


import src.constants as constants


import random


width = 480
height = 853 #width/9*16
# height = 1000
score = 0
obstacle_frequency = constants.OBSTACLE_FREQUENCY
powerup_frequency = random.randint(*constants.POWERUOP_FREQUENCY_RANGE)
last_obstacle = pygame.time.get_ticks()
last_powerup = pygame.time.get_ticks()


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paclub")
clock = pygame.time.Clock()

game = Game(screen, (width, height), constants)
assets = Assets(screen, (width, height), constants)
assets.load_images()
rocket = Rocket(assets.display_rocket, assets.get_rocket_size(), (width, height))

spawn = Spawn(screen, (width, height), constants, assets)

collision = Collision(game.calculate_character_hitbox_position, rocket, screen, constants, spawn)

effects = Effects(screen, (width, height), constants, assets)

game.set_params(assets.display_obstacle, assets.display_character, assets)

menus = Menus((width, height), constants, assets)

font = Font(screen, (width, height), constants)

warningFont = font.load_system_font("Beyond Calibri", 40)

current_background_offset = 0
center_time = 0
shield_pop_time = 0
running = True
game_over = False
display_warning = False
# send_warning = False
state = "menu"
while running:
    match state:
        case "menu":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((195, 104, 77))
            #play
            play_button_position = menus.get_button_position(assets.play_button)
            if menus.check_for_hover(pygame.mouse.get_pos(), assets.play_button, play_button_position):
                screen.blit(assets.play_button_hover, menus.get_button_position(assets.play_button_hover))
                if pygame.mouse.get_pressed()[0]:
                    state = "game"
                    game_over = False
                    display_warning = False
                    game.reset()
                    rocket.reset()
                    effects.reset()
                    spawn.reset()
                    center_time = 0
                    score = 0
                    shield_pop_time = 0
                    current_background_offset = 0
                    obstacle_frequency = constants.OBSTACLE_FREQUENCY
                    last_obstacle = pygame.time.get_ticks()
            else:
                screen.blit(assets.play_button, play_button_position)

            

            #options
            options_button_position = menus.get_button_position(assets.options_button, 115)
            if menus.check_for_hover(pygame.mouse.get_pos(), assets.options_button, options_button_position):
                screen.blit(assets.options_button_hover, menus.get_button_position(assets.options_button_hover, 115))
            else:
                screen.blit(assets.options_button, options_button_position)
            #quit
            quit_button_position = menus.get_button_position(assets.quit_button, 230)
            if menus.check_for_hover(pygame.mouse.get_pos(), assets.quit_button, quit_button_position):
                screen.blit(assets.quit_button_hover, menus.get_button_position(assets.quit_button_hover, 230))
            else:
                screen.blit(assets.quit_button, quit_button_position)

            if game_over:
                font.render_font("D3", 28, "GAME OVER", (255, 255, 255), (width/2, height/3.3), center=True, outline=1)
                font.render_font("D3", 28, f"SCORE: {score}", (255, 255, 255), (width/2, height/3.3+25), center=True, outline=1)
                # font.render_font(basicFont, "Press any key to play again", (255, 255, 255), (width/2, height/2 + 50), center=True)

        case "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game.update_side("left")
                    elif event.key == pygame.K_RIGHT:
                        game.update_side("right")
                    # elif game_over:
                    #     game_over = False
                    #     display_warning = False
                    #     game.reset()
                    #     rocket.reset()
                    #     effects.reset()
                    #     spawn.reset()
                    #     center_time = 0
                    #     score = 0
                    #     shield_pop_time = 0
                    #     current_background_offset = 0
                    #     obstacle_frequency = constants.OBSTACLE_FREQUENCY
                    #     last_obstacle = pygame.time.get_ticks()

            if not game_over:
                time_now = pygame.time.get_ticks()
                if time_now - last_obstacle > obstacle_frequency / game.speed:
                    # obstacle_frequency = time_now + 500
                    game.add_obstacle()
                    score += 1
                    last_obstacle = time_now
                if time_now - last_powerup > powerup_frequency / game.speed:
                    spawn.add_spawnable(random.choice(("left", "center", "right")), effects.get_effect_drop())
                    last_powerup = time_now
                    powerup_frequency = random.randint(*constants.POWERUOP_FREQUENCY_RANGE)

                #effects handling
                effects.handle_effects()

                if game.character_side == "center":
                    center_time += constants.STAMINA_GAIN * effects.stamina_multiplier
                    #warming
                    display_warning = center_time >= constants.CENTER_TIME_LIMIT / 2
                    if center_time >= constants.CENTER_TIME_LIMIT:
                        rocket.add_rocket()
                        center_time = 0

                    if center_time > constants.CENTER_TIME_LIMIT:
                        center_time = constants.CENTER_TIME_LIMIT
                else:
                    center_time -= constants.STAMINA_LOSS
                    display_warning = center_time >= constants.CENTER_TIME_LIMIT / 2
                    if center_time < 0:
                        center_time = 0

                if game.check_for_collision():
                    game_over = True
                if collision.check_rocket_collision() and game.character_side == "center":
                    game_over = True
                spawnable_collision = collision.check_spawnable_collision()
                if spawnable_collision.get("collision"):
                    effects.add_effect(spawnable_collision["type"])
                screen.fill(constants.BACKGROUND_COLOR)
                game.decrement_obstacles()
                rocket.decrement_rockets(game.speed)
                spawn.decrement_spawnables(game.speed)

                current_background_offset += 5 * game.speed
                if current_background_offset > height:
                    current_background_offset = 0
                assets.display_background(current_background_offset)
                assets.display_background(current_background_offset - height)

                game.draw_obstacles()
                spawn.display_spawnables()
                game.draw_character(effects.shield, effects.immunity)
                rocket.display_rockets()

                if game.speed < 2.0:
                    game.speed += 0.001
                elif game.speed < 2.5:
                    game.speed += 0.0005
                elif game.speed < 3.0:
                    game.speed += 0.0001

                scoretext = font.render_font("Beyond Calibri", 28, f"Score: {score}", (0,0,0), (0,0))
                scoretext = font.render_font("Beyond Calibri", 28, f"Speed: {round(game.speed, 2)}", (0,0,0), (0,25))
            
                # print(100*(center_time/constants.CENTER_TIME_LIMIT))

                #stamina bar

                if effects.stamina_multiplier == 1:
                    stamina_color = constants.stamina_bar
                else:
                    stamina_color = constants.boosted_stamina_bar
                # progress bar background
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,height-25,190,15))
                # progress bar
                pygame.draw.rect(screen, stamina_color, pygame.Rect(0,height-25,190*(center_time/constants.CENTER_TIME_LIMIT),15))
                # outline
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0,height-25,190,15), 1)

                # if send_warning:
                    # assets.display_rocket((150, 150))
                if display_warning:
                    # assets.display_image(assets.danger, (width/2 - assets.danger.get_width()/2 - 15, assets.danger.get_height() - 15,assets.danger.get_width() + 30,assets.danger.get_height() + 30))
                    warning = warningFont.render("<!>", 1, (255,0,0))
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width/2 - warning.get_width()/2 - 15, warning.get_height() - 15,warning.get_width() + 30,warning.get_height() + 30), 0, 5)
                    screen.blit(warning, (width/2 - warning.get_width()/2, warning.get_height()))
                    # font.render_font(warningFont, "<!>", (255, 0, 0), (width/2, 15), center=True)
                
                #shield popping
                if game_over and effects.shield:
                    game_over = False
                    effects.shield = False
                    shield_pop_time = pygame.time.get_ticks()
                    effects.add_effect("shield-pop-immunity")

                #check for shield popping immunity
                if game_over and effects.immunity:
                    game_over = False

                if game_over:
                    state = "menu"




    pygame.display.update()
    clock.tick(60)
