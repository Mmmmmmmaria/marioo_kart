
# jeu_de_course

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.05
CAR_WIDTH = 30
CAR_HEIGHT = 50


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)

# Couleurs des menus

COLOR_BUTTON = (40, 40, 70)
COLOR_BUTTON_HOVER = (70, 70, 110)

COLOR_PLAYER1 = (255, 60, 60)
COLOR_PLAYER2 = (60, 120, 255)

# États du jeu

class GameState:
    MENU = "menu"
    SELECT_TRACK = "select_track"
    RACING = "racing"
    PAUSE = "pause"
    VICTORY = "victory"
