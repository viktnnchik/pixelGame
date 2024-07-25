import pygame
from settings import CELL_SIZE, GRID_LEFT

# Создание изображения для зомби
zombie_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
zombie_image.fill((255, 0, 0))  # Красный цвет для зомби
pygame.draw.rect(zombie_image, (0, 0, 0), (CELL_SIZE // 4, CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))  # Черный прямоугольник

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(zombie_image, (self.x, self.y))

    def move(self):
        self.x -= 2
        if self.x < GRID_LEFT:
            return True
        return False

    def eat_plant(self, plants):
        for plant in plants:
            if plant.x < self.x < plant.x + CELL_SIZE and plant.y == self.y:
                plants.remove(plant)
                return True
        return False
