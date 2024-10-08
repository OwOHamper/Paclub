BACKGROUND_COLOR = "#a1a09f"
LOG_SIZE = 100

#character
CHARACTER_SIZE = 80
CHARACTER_OFFSET_FROM_LOG = 10
OBSTACLE_SIZE = (190, 48)

OBSTACLE_FREQUENCY = 1000

BACKGROUND_PATH = "assets/background.png"
CHARACTER_PATH = "assets/steve.png"
OBSTACLE_PATH = "assets/tnt-large.png"
ROCKET_PATH = "assets/rocket_fireball.png"

BLUE_POTION_PATH = "assets/blue-potion.png"
GREEN_POTION_PATH = "assets/green-potion.png"
PINK_POTION_PATH = "assets/pink-potion.png"
YELLOW_POTION_PATH = "assets/yellow-potion.png"

DANGER_PATH = "assets/danger.png"

DISPLAY_TITLE_PATH = "assets/paclub.png"
PLAY_BUTTON_PATH = "assets/play.png"
PLAY_BUTTON_HOVER_PATH = "assets/play-hover.png"
OPTIONS_BUTTON_PATH = "assets/options.png"
OPTIONS_BUTTON_HOVER_PATH = "assets/options-hover.png"
QUIT_BUTTON_PATH = "assets/quit.png"
QUIT_BUTTON_HOVER_PATH = "assets/quit-hover.png"

FONT_D3 = "fonts/D3Petitbitmapism.ttf"


CENTER_TIME_LIMIT = 2000

STAMINA_GAIN = 30
STAMINA_LOSS = 10

ROCKET_HITBOX_TOP_CUT = 75

POWERUOP_FREQUENCY_RANGE = (25000, 30000)

EFFECTS = {
    "powerup-shield": {
        "total_duration": 0,
        "chance": 0.3
    },
    "powerup-stamina": {
        "total_duration": 10000,
        "multiplier": 1/3,
        "chance": 1
    },
    "shield-pop-immunity": {
        "total_duration": 1000,
    }
}

SHIELD_POP_IMMUNITY = 1000
SHIELD_PATH = "assets/shield.png"


stamina_bar = (252, 65, 3)
boosted_stamina_bar = (90, 252, 3)