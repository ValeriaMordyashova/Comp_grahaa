import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Угол наклона плоскости в градусах
slope_angle = 30

# Преобразование угла наклона в радианы
slope_angle_rad = math.radians(slope_angle)

# Длина наклонной линии
line_length = 300

# Начальные координаты цилиндра в верхнем правом углу
start_x = 800
start_y = 100

# Радиус цилиндра
radius = 20

# Создание окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Скатывание цилиндра")

# Цикл обработки событий
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Вычисление новых координат цилиндра после скатывания
    new_x = start_x - radius * math.cos(slope_angle_rad)
    new_y = start_y + radius * math.sin(slope_angle_rad)

    # Отрисовка цилиндра
    pygame.draw.circle(screen, RED, (int(start_x), int(start_y)), radius)

    # Отрисовка наклонной линии
    pygame.draw.line(screen, BLACK, (800, 120), (3, 580), 2)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для симуляции времени
    pygame.time.delay(50)

    # Обновление начальных координат
    start_x = new_x
    start_y = new_y

    # Проверка достижения левой стороной цилиндра
    if start_x - radius <= 0:
        running = False

    # Ограничение частоты обновления экрана
    clock.tick(30)

# Завершение программы
pygame.quit()
sys.exit()
