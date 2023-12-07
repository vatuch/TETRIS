import sys
import tkinter as tk
import sqlite3
import pygame
from copy import deepcopy
from random import choice, randrange


def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        # Переход на другую форму
        message_label.configure(text="Успешная авторизация")
        root.destroy()
        return username
    else:
        message_label.configure(text="Ошибка авторизации")
        return None


def register():
    username = entry_username.get()
    password = entry_password.get()

    # Проверка зарегистрированного пользователя в базе данных

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
      (username TEXT, 
      password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    message_label.configure(text="Успешно зарегистрирован!")

root = tk.Tk()
root.overrideredirect(1)
bg_color = '#ffcbdb'
button_bg_color = '#de5d83'
button_fg_color = 'white'
button_font = ('Gilroy', 14)
window_width1 = 750
window_height1 = 850
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width1 / 2))
y = int((screen_height / 2) - (window_height1 / 2))
root.geometry(f'{window_width1}x{window_height1}+{x}+{y}')

root.config(bg=bg_color)
message_label = tk.Label(root, text="", font='Gilroy')
message_label.pack(side=tk.TOP, pady=(250, 10))

label_username = tk.Label(root, text="Введите имя пользователя", font='Gilroy', bg=bg_color, fg='#de5d83')
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Введите пароль", font='Gilroy', bg=bg_color, fg='#de5d83')
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_login = tk.Button(root, text="Войти", command=login, font='Gilroy', width=20, bg=button_bg_color,
                         fg=button_fg_color)
button_login.pack(padx=5, pady=10)

button_register = tk.Button(root, text="Зарегистрироваться", command=register, font='Gilroy', width=20,
                            bg=button_bg_color, fg=button_fg_color)
button_register.pack(padx=5, pady=10)

exit_button = tk.Button(root, text="Выйти", command=sys.exit, font='Gilroy', width=20, bg=button_bg_color,
                        fg=button_fg_color)
exit_button.pack(side=tk.TOP, pady=10)
root.mainloop()


def rectate():
    with open('record', 'r') as f:
        content = f.read()
        recc = tk.Tk()
        recc.overrideredirect(1)
        bg_color = '#ffcbdb'
        button_bg_color = '#de5d83'
        button_fg_color = 'white'
        button_font = ('Gilroy', 14)

        recc.configure(bg=bg_color)

        current_record = 0
        window_width = 750
        window_height = 850
        screen_width = recc.winfo_screenwidth()
        screen_height = recc.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        recc.geometry(f'{window_width}x{window_height}+{x}+{y}')
        frame = tk.Frame(recc, bg=bg_color)
        frame.pack(expand=True)

        title = tk.Label(recc, text=f"Самый большой счет:", bg=bg_color, fg=button_bg_color, font='Gilroy')
        title.pack(side=tk.TOP, pady=(20, 10))

        recctit = tk.Label(recc, text="", bg=bg_color, fg=button_bg_color, font='Gilroy')
        recctit.pack(side=tk.TOP, pady=(20, 10))

        recctit.config(text=content)  # Добавляем эту строку

        def close_recc():
            recc.destroy()

        exit_button = tk.Button(recc, text="Выйти", command=close_recc,
                                bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=20)
        exit_button.pack(side=tk.TOP, pady=10)


def open_form1():
    root = tk.Tk()
    root.overrideredirect(1)
    root.title("Tetris Game")
    bg_color = '#ffcbdb'
    button_bg_color = '#de5d83'
    button_fg_color = 'white'
    button_font = ('Gilroy', 14)

    root.configure(bg=bg_color)

    current_record = 0
    window_width = 750
    window_height = 850
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(expand=True)

    title = tk.Label(frame, text=f"TETRIS GAME", bg=bg_color, fg=button_bg_color, font=('Dance', 54))
    title.pack(side=tk.TOP, pady=(20, 20))

    def close_form1():
        root.destroy()

    button = tk.Button(frame, text="Начать игру", command=close_form1,
                       bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=20)
    button.pack(side=tk.TOP, pady=10)

    record_button = tk.Button(frame, text="Таблица рекордов ", command=rectate,
                              bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=20)
    record_button.pack(side=tk.TOP, pady=10)

    exit_button = tk.Button(frame, text="Выйти", command=sys.exit,
                            bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=20)
    exit_button.pack(side=tk.TOP, pady=10)

    root.mainloop()
    root.mainloop()
    root.mainloop()


if __name__ == '__main__':
    open_form1()


    width, height = 10, 18
    TILE = 45
    GAME_RES = width * TILE, height * TILE
    RES = 950, 850

    FPS = 80

    pygame.init()  #
    screen = pygame.display.set_mode(RES, pygame.NOFRAME)
    game_sc = pygame.Surface(GAME_RES)
    clock = pygame.time.Clock()
    grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(width) for y in range(height)]


    figure_pos = [
        [(-1, 0), (-2, 0), (0, 0), (1, 0)],
        [(0, -1), (-1, -1), (-1, 0), (0, 0)],
        [(-1, 0), (-1, 1), (0, 0), (0, -1)],
        [(0, 0), (-1, 0), (0, 1), (-1, -1)],
        [(0, 0), (0, -1), (0, 1), (-1, 1)],
        [(0, 0), (0, -1), (0, 1), (-1, -1)],
        [(0, 0), (0, -1), (0, 1), (-1, 0)]
    ]


    figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in figure_pos] for figure_pos in figure_pos]
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
    field = [[0 for _ in range(width)] for _ in range(height)]
    drop_count, drop_speed, drop_limit = 0, 45, 1000

    get_color = lambda: (
        randrange(30, 256), randrange(30, 256), randrange(30, 256))

    score, lines = 0, 0
    scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
    level = 1

    main_font = pygame.font.Font('Font\Gilroy-Regular.ttf', 30)
    font = pygame.font.Font('Font\Dance.ttf', 50)


    title_tetris = font.render('TETRIS', True, pygame.Color('#de5d83'))
    title_score = font.render('score:', True, pygame.Color('#ffeeed'))


    bg = pygame.image.load('image\Background_Second.jpg').convert()
    game_bg = pygame.image.load('image\Background_First.jpg').convert()


    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
    color, next_color = get_color(), get_color()


    title_record = font.render('record:', True, pygame.Color('#fffaf0'))
    title_level = font.render('level:', True, pygame.Color('#fffaf0'))

    title_image = pygame.image.load('image/avatar.jpg')

    sound = pygame.mixer.Sound("sound\Bonus.mp3")
    sound_game_over = pygame.mixer.Sound("sound\Game_Over.mp3")
    main_sound = pygame.mixer.Sound("sound\Main_Sound.mp3")

    paused = False
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


def draw_button_exit(msg, x, y, width, height, color, hover_color):
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

def start_game():
    global figure, next_figure, color, next_color, figure_rect, field, drop_count, score, lines, level
    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
    color, next_color = get_color(), get_color()
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
    field = [[0 for _ in range(width)] for _ in range(height)]
    drop_count, score, lines, level = 0, 0, 0, 1
    pygame.time.set_timer(pygame.USEREVENT, 1000)


def draw_button_again(msg, x, y, width, height, color, hover_color):
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


def save_record(score):
    record = get_record()
    if score > record:
        with open('record', 'w') as f:
            f.write(str(score))


def restart_game():
    save_record(score)
    start_game()


def draw_start_again_button():
    if draw_button("Начать сначала", 480, 480, 260, 50, ('#ffcbdb'), ('#de5d83')):
        restart_game()

def draw_button_exit():
    if draw_button("Выйти из игры", 480, 550, 260, 50, ('#ffcbdb'), ('#de5d83')):
        sys.exit()


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

while True:
    #main_sound.play()
    record = get_record()
    dx, rorate = 0, False
    screen.blit(bg, (0, 0))
    screen.blit(game_sc, (20, 20))
    game_sc.blit(game_bg, (0, 0))

    for i in range(lines):
        pygame.time.wait(200)


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
                if paused:
                    if paused:
                        screen.fill((0, 0, 0))
                        text_surface = font.render("Для снятия паузы нажмите Esc", True, ('#de5d83'))
                        screen.blit(text_surface, (250, 250))
                        pygame.display.update()

    if not paused:
        figure_old = deepcopy(figure)
        for i in range(4):
            if figure[i].x + dx < 0 or figure[i].x + dx >= width:
                figure = deepcopy(figure_old)
                break
            figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

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

        score += scores[lines]

        if lines == 1:
            level = 2
            drop_speed += 10
        elif lines == 5:
            level = 3
            drop_speed += 20
        elif lines == 10:
            level = 4
            drop_speed += 25
        elif lines == 25:
            level = 5
            drop_speed += 30

        [pygame.draw.rect(game_sc, (255, 255, 255), i_rect, 1) for i_rect in grid]  # отрисовка элементов с границами

        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(game_sc, color, figure_rect)

        for y, raw in enumerate(field):
            for x, col in enumerate(raw):
                if col:
                    figure_rect.x, figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(game_sc, col, figure_rect)

        if score > record:
            set_record(record, score)

        for i in range(4):
            figure_rect.x = next_figure[i].x * TILE + 390
            figure_rect.y = next_figure[i].y * TILE + 185
            pygame.draw.rect(screen, next_color, figure_rect)
        pass

        draw_start_again_button()
        draw_button_exit()

        pause_text = 'Продолжить' if paused else 'Пауза'
        if draw_button(pause_text, 480, RES[1] / 2 - 30, 260, 50, ('#ffcbdb'), ('#de5d83')):
            paused = not paused

        screen.blit(title_tetris, (530, 10))
        screen.blit(title_level, (530, 70))
        screen.blit(main_font.render(str(level), True, pygame.Color('white')), (530, 130))
        screen.blit(title_score, (515, 750))
        screen.blit(main_font.render(str(score), True, pygame.Color('white')), (515, 790))
        screen.blit(title_record, (515, 630))
        screen.blit(main_font.render(str(record), True, pygame.Color('white')), (515, 700))
        screen.blit(title_image, (780, 15))
        title_image = pygame.transform.scale(title_image, (130, 128))
        font = pygame.font.Font('Font/Gilroy-Regular.ttf', 25)


        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username = 'Player'")
        result = cursor.fetchone()
        conn.close()
        text = font.render(result[0], 'Example Text', True, )

        text_rect = text.get_rect(center=(850, 160))
        screen.blit(text, text_rect)
        pygame.display.flip()

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
