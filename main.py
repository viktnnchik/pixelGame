import pygame
import random
from settings import *
from plant import Plant, sunflower_image, turret_image
from zombie import Zombie, zombie_image
from utils import draw_text


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs Zombies")

plant_positions = []
zombie_positions = []
plants = []
zombies = []
score = 150


clock = pygame.time.Clock()


def spawn_zombie():
    x_pos = SCREEN_WIDTH
    y_pos = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE + GRID_TOP
    zombies.append(Zombie(x_pos, y_pos))

def draw_objects():
    for plant in plants:
        plant.draw(screen)
    for zombie in zombies:
        zombie.draw(screen)

def update_zombie_positions():
    global game_over
    for zombie in zombies[:]:
        if zombie.move():
            game_over = True
        if zombie.eat_plant(plants):
            zombies.remove(zombie)
            break

game_over = False
selected_plant = None

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y < CELL_SIZE:
                if x < CELL_SIZE:
                    selected_plant = 'sunflower'
                elif x < 2 * CELL_SIZE:
                    selected_plant = 'turret'
            else:
                if selected_plant:
                    grid_x = x - (x % CELL_SIZE)
                    grid_y = y - (y % CELL_SIZE)
                    if GRID_LEFT <= grid_x < GRID_LEFT + GRID_WIDTH * CELL_SIZE and GRID_TOP <= grid_y < GRID_TOP + GRID_HEIGHT * CELL_SIZE:
                        if selected_plant == 'sunflower' and score >= SUNFLOWER_COST:
                            plants.append(Plant(grid_x, grid_y, 'sunflower'))
                            plant_positions.append([grid_x, grid_y])
                            score -= SUNFLOWER_COST
                        elif selected_plant == 'turret' and score >= TURRET_COST:
                            plants.append(Plant(grid_x, grid_y, 'turret'))
                            plant_positions.append([grid_x, grid_y])
                            score -= TURRET_COST
                        selected_plant = None

    screen.fill(WHITE)

    screen.blit(sunflower_image, (0, 0))
    draw_text(f"50", FONT, BLACK, screen, 0, CELL_SIZE)
    screen.blit(turret_image, (CELL_SIZE, 0))
    draw_text(f"100", FONT, BLACK, screen, CELL_SIZE, CELL_SIZE)
    draw_text(f"Score: {score}", FONT, BLACK, screen, SCREEN_WIDTH - 150, 10)

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            rect = pygame.Rect(GRID_LEFT + col * CELL_SIZE, GRID_TOP + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    if random.random() < 0.005: 
        spawn_zombie()

    update_zombie_positions()
    draw_objects()

    for plant in plants:
        score = plant.action(score, zombies)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
