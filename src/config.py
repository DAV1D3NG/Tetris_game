import pygame

high_score_file = "data/highscore.txt"

# --- RGB COLORS DEFINITION ---
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GHOST_COLOR = (100, 100, 100)
PANEL_COLOR = (111, 111, 111)

# --- UI LAYOUT CONSTANTS ---
# Commands Constants
COMMANDS_START_Y = 70
COMMAND_LINE_HEIGHT = 20
COMMAND_COUNT = 9

# Audio Constants (Y-Coordinates)
AUDIO_START_Y = COMMANDS_START_Y + COMMAND_LINE_HEIGHT * COMMAND_COUNT + 120
MUSIC_CHECKBOX_Y = AUDIO_START_Y
MUSIC_SLIDER_Y = MUSIC_CHECKBOX_Y + 30
SFX_CHECKBOX_Y = MUSIC_CHECKBOX_Y + 50
SFX_SLIDER_Y = SFX_CHECKBOX_Y + 30

# --- CONFIGURATION ---
# Gaming grid Configuration
CELL_SIZE = 30
COLUMNS = 15
ROWS = 30

# Lateral panel Configuration
PANEL_WIDTH = 9 * CELL_SIZE

# Window Configuration
TOTAL_WIDTH = CELL_SIZE * COLUMNS + PANEL_WIDTH
TOTAL_HEIGHT = CELL_SIZE * ROWS
FPS = 60

# Font and Text Configuration
pygame.font.init()
LARGE = pygame.font.SysFont('arial', 50)
MEDIUM = pygame.font.SysFont('arial', 30)
SMALL = pygame.font.SysFont('arial', 20)
COMMAND_LINES = [
    "Commands:",
    "← / A: move left",
    "→ / D: move right",
    "↑ / W: rotate",
    "↓ / S: soft drop",
    "SPACE: hard drop",
    "P    : pause",
    "R    : restart",
    "M    : mute/unmute music",
    "K    : mute/unmute SFX",
    "ESC  : exit"
]
RENDERED_COMMANDS = [SMALL.render(line, True, BLACK) for line in COMMAND_LINES]

# --- TETROMINO CONFIGURATION ---
# Shape colors
COLORS = [
    (0, 255, 255),  # I: Hero (Cyan)
    (128, 0, 128),  # T: Teewee (Purple)
    (0, 0, 255),    # J: Blue Ricky (Blue)
    (255, 165, 0),  # L: Orange Ricky (Orange)
    (0, 255, 0),    # S: Rhode Island Z (Green)
    (255, 0, 0),    # Z: Cleveland Z (Red)
    (255, 255, 0)   # O: Smashboy (Yellow)
]

# Shape rotations (stored as string matrices)
SHAPES = [
    # I Shape
    [
        ["....",
         "XXXX",
         "....",
         "...."],
        ["..X.",
         "..X.",
         "..X.",
         "..X."]
    ],
    # T Shape
    [
        [".X.",
         "XXX",
         "..."],
        [".X.",
         ".XX",
         ".X."],
        ["...",
         "XXX",
         ".X."],
        [".X.",
         "XX.",
         ".X."]
    ],
    # L Shape
    [
        ["X..",
         "XXX",
         "..."],
        [".XX",
         ".X.",
         ".X."],
        ["...",
         "XXX",
         "..X"],
        [".X.",
         ".X.",
         "XX."]
    ],
    # J Shape
    [
        ["..X",
         "XXX",
         "..."],
        [".X.",
         ".X.",
         ".XX"],
        ["...",
         "XXX",
         "X.."],
        ["XX.",
         ".X.",
         ".X."]
    ],
    # S Shape
    [
        [".XX",
         "XX.",
         "..."],
        [".X.",
         ".XX",
         "..X"]
    ],
    # Z Shape
    [
        ["XX.",
         ".XX",
         "..."],
        ["..X",
         ".XX",
         ".X."]
    ],
    # O Shape
    [
        ["XX",
         "XX"]
    ]
]