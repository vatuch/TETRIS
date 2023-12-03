import tkinter as tk
from _ast import Lambda
import pygame
from copy import deepcopy
from random import choice, randrange
from MainMenu import open_form1
if __name__ == '__main__':
    open_form1()

# Создание игрового поля заданного разрешения
width, height = 10, 18  # Ширина и высота в блоках
TILE = 45  # Размер одного блока
GAME_RES = width * TILE, height * TILE  # Разрешение игрового поля
RES = 750, 850  # Общее разрешение окна

FPS = 80  # Частота кадров в секунду (FPS)

pygame.init()  # Инициализация всех импортированных модулей pygame
screen = pygame.display.set_mode(RES)  # Создание окна с заданным разрешением
game_sc = pygame.Surface(GAME_RES)  # Создание поверхности для игрового поля
clock = pygame.time.Clock()  # Создание объекта для отслеживания времени

# Генерация сетки игрового поля
grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(width) for y in range(height)]

# Определение форм фигур
figure_pos = [
    [(-1, 0), (-2, 0), (0, 0), (1, 0)],  # Форма I
    [(0, -1), (-1, -1), (-1, 0), (0, 0)],  # Форма Z
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],  # Форма S
    [(0, 0), (-1, 0), (0, 1), (-1, -1)],  # Форма T
    [(0, 0), (0, -1), (0, 1), (-1, 1)],  # Форма L
    [(0, 0), (0, -1), (0, 1), (-1, -1)],  # Зеркальная форма L
    [(0, 0), (0, -1), (0, 1), (-1, 0)]  # Форма O
]

# Создание фигур из координат
figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in figure_pos] for figure_pos in figure_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for _ in range(width)] for _ in range(height)]

# Установки, связанные с падением фигур
drop_count, drop_speed, drop_limit = 0, 45, 1000

get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))  # Функция для получения случайного цвета

score, lines = 0, 0  # Текущий счет и количество полностью заполненных линий
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500} # Очки за уничтоженные линии
level = 1  # Уровень игры

# Шрифты
main_font = pygame.font.Font('Font\Gilroy-Regular.ttf', 30)
font = pygame.font.Font('Font\Dance.ttf', 50)

# Текстовые элементы
title_tetris = font.render('TETRIS', True, pygame.Color('#de5d83'))
title_score = font.render('score:', True, pygame.Color('#ffeeed'))

# Загрузка фоновых изображений
bg = pygame.image.load('image\Background_Second.jpg').convert()
game_bg = pygame.image.load('image\Background_First.jpg').convert()

# Инициализация фигур и их цветов
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

# Дополнительные текстовые элементы
title_record = font.render('record:', True, pygame.Color('#fffaf0'))
title_level = font.render('level:', True, pygame.Color('#fffaf0'))

# Загрузка звуковых эффектов
sound = pygame.mixer.Sound("sound\Bonus.mp3")
sound_game_over = pygame.mixer.Sound("sound\Game_Over.mp3")

# Переменная для управления паузой
paused = False

# кнопка паузы
def draw_button(msg, x, y, width, height, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color if button_rect.collidepoint(mouse) else hover_color, button_rect)

    text_surf = main_font.render(msg, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)

    if button_rect.collidepoint(mouse) and click[0]:
        return True
    return False


# проверка границ
def check_borders():
    if figure[i].x < 0 or figure[i].x > width - 1:
        return False
    elif figure[i].y > height - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


def get_record():
    try:
        with open('record') as f:
            return int(f.readline())
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
        return 0


def set_record(record, score):
    rec = max(record, int(score))
    with open('record', 'w') as f:
        f.write(str(rec))

#Основой цикл программы

while True:
    record = get_record()
    dx, rorate = 0, False
    screen.blit(bg, (0, 0))
    screen.blit(game_sc, (20, 20))
    game_sc.blit(game_bg, (0, 0))
    # задержка при линиях

    for i in range(lines):
        pygame.time.wait(200)

    # изменения через клавиатуру
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                drop_limit = 100
            elif event.key == pygame.K_UP:
                rorate = True
            elif event.key == pygame.K_ESCAPE:
                paused = not paused
    if not paused:

        # передвежение вдоль оси x
        figure_old = deepcopy(figure)
        for i in range(4):
            if figure[i].x + dx < 0 or figure[i].x + dx >= width:
                figure = deepcopy(figure_old)
                break
            figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

        # передвижение вдоль оси y

        drop_count += drop_speed
        if drop_count > drop_limit:
            drop_count = 0
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i].y += 1
                if not check_borders():
                    for i in range(4):
                        field[figure_old[i].y][figure_old[i].x] = color
                    figure, color = next_figure, next_color
                    next_figure, next_color = deepcopy(choice(figures)), get_color()
                    drop_limit = 1000
                    break

        # поворот фигур
        centre = figure[0]
        figure_old = deepcopy(figure)
        if rorate:
            for i in range(4):
                x = figure[i].y - centre.y
                y = figure[i].x - centre.x
                figure[i].x = centre.x - x
                figure[i].y = centre.y + y
            if not check_borders():
                    figure = deepcopy(figure_old)
                    break

        # удаление заполненной линии

        line, lines = height - 1, 0
        for row in range(height - 1, -1, -1):
            count = 0
            for i in range(width):
                if field[row][i]:
                    count += 1
                field[line][i] = field[row][i]
            if count < width:
                line -= 1
            else:
                drop_speed += 3
                lines += 1
                if lines > 0:
                    sound.play()

        # начисление очков
        score += scores[lines]

        # проверка для уровня
        if lines >= 3:
            level = 2
            drop_speed += 10
        elif lines >= 10:
            level = 3
            drop_speed += 20
        elif lines >= 20:
            level = 4
            drop_speed += 50
        elif lines >= 45:
            level = 5
            drop_speed += 100

        # создание сетки
        [pygame.draw.rect(game_sc, (255, 255, 255), i_rect, 1) for i_rect in grid]  # отрисовка элементов с границами

        # зарисовка фигуры
        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(game_sc, color, figure_rect)

        # заполнение
        for y, raw in enumerate(field):
            for x, col in enumerate(raw):
                if col:
                    figure_rect.x, figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(game_sc, col, figure_rect)

        # следующая фигура
        for i in range(4):
            figure_rect.x = next_figure[i].x * TILE + 390
            figure_rect.y = next_figure[i].y * TILE + 185
            pygame.draw.rect(screen, next_color, figure_rect)
        pass

        # надписи
        pause_text = 'Продолжить' if paused else 'Пауза'
        if draw_button(pause_text, 530, RES[1] / 2 - 30, 200, 60, ('#ffcbdb'), ('#de5d83')):
            paused = not paused

        screen.blit(title_tetris, (530, 10))
        screen.blit(title_level, (530, 70))
        screen.blit(main_font.render(str(level), True, pygame.Color('white')), (530, 130))
        screen.blit(title_score, (515, 750))
        screen.blit(main_font.render(str(score), True, pygame.Color('white')), (515, 790))
        screen.blit(title_record, (515, 630))
        screen.blit(main_font.render(str(record), True, pygame.Color('white')), (515, 700))

        # конец игры
        # достижение границы поля
        for i in range(width):
            if field[0][i]:
                set_record(record, score)
                field = [[0 for i in range(width)] for i in range(height)]
                drop_count, drop_speed, drop_limit = 0, 45, 1000
                score = 0
                for i_rect in grid:
                    pygame.draw.rect(game_sc, get_color(), i_rect)
                    screen.blit(game_sc, (20, 20))
                    pygame.display.flip()
                    sound_game_over.play()
                    clock.tick(200)

        pygame.display.flip()
        clock.tick(FPS)

