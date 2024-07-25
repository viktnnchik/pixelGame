import pygame

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 5
GRID_TOP = 100
GRID_LEFT = (SCREEN_WIDTH - (GRID_WIDTH * CELL_SIZE)) // 2

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Стоимость растений
SUNFLOWER_COST = 50
TURRET_COST = 100

# Шрифт
pygame.font.init()
FONT = pygame.font.Font(None, 36)
