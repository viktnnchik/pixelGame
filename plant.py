import time
import pygame
from settings import CELL_SIZE, SUNFLOWER_COST, TURRET_COST, SCREEN_WIDTH

# Создание изображений для растений
sunflower_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
sunflower_image.fill((255, 255, 0))  # Желтый цвет для подсолнуха
pygame.draw.circle(sunflower_image, (0, 255, 0), (CELL_SIZE // 2, CELL_SIZE // 2), CELL_SIZE // 4)  # Зеленый центр

turret_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
turret_image.fill((0, 0, 255))  # Синий цвет для пулемета
pygame.draw.rect(turret_image, (255, 0, 0), (CELL_SIZE // 4, CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))  # Красный прямоугольник

bullet_image = pygame.Surface((CELL_SIZE // 4, CELL_SIZE // 4))
bullet_image.fill((0, 0, 0))  # Черный цвет для снаряда

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 5

    def draw(self, screen):
        screen.blit(bullet_image, (self.x, self.y))

    def check_collision(self, zombie):
        if zombie.x < self.x < zombie.x + CELL_SIZE and zombie.y < self.y < zombie.y + CELL_SIZE:
            return True
        return False

class Plant:
    def __init__(self, x, y, plant_type):
        self.x = x
        self.y = y
        self.type = plant_type
        self.last_action_time = time.time()
        self.bullets = []

    def draw(self, screen):
        if self.type == 'sunflower':
            screen.blit(sunflower_image, (self.x, self.y))
        elif self.type == 'turret':
            screen.blit(turret_image, (self.x, self.y))
            for bullet in self.bullets:
                bullet.draw(screen)

    def action(self, score, zombies):
        current_time = time.time()
        if self.type == 'sunflower':
            if current_time - self.last_action_time >= 3:
                score += 50
                self.last_action_time = current_time
        elif self.type == 'turret':
            if current_time - self.last_action_time >= 5:
                self.shoot()
                self.last_action_time = current_time
            self.update_bullets(zombies)
        return score

    def shoot(self):
        self.bullets.append(Bullet(self.x + CELL_SIZE, self.y + CELL_SIZE // 2))

    def update_bullets(self, zombies):
        for bullet in self.bullets[:]:
            bullet.move()
            for zombie in zombies[:]:
                if bullet.check_collision(zombie):
                    zombies.remove(zombie)
                    self.bullets.remove(bullet)
                    break
            if bullet.x > SCREEN_WIDTH:
                self.bullets.remove(bullet)
