import tkinter as tk
import sys
def open_form1():
    root = tk.Tk()
    root.title("Меню")

    #цвет фона окна
    bg_color = '#ffcbdb'
    button_bg_color = '#de5d83' 
    button_fg_color = 'white'  # Цвет текста на кнопках - белый
    button_font = ('Arial', 14)  # Шрифт и размер текста на кнопках



    root.configure(bg=bg_color)

    window_width = 750
    window_height = 850

    #размеры экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Рассчитываем позицию x и y
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Устанавливаем размеры окна и позицию его на экране
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # Фрейм для размещения кнопок по центру
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(expand=True)

    # Добавляем заголовок "Тетрис"
    title = tk.Label(frame, text="ТЕТРИС", bg=bg_color, fg=button_bg_color, font='Arial' )
    title.pack(side=tk.TOP, pady=(20, 10))

    # Функция закрытия окна form1
    def close_form1():
        root.destroy()

    button = tk.Button(frame, text="Начать игру", command=close_form1,
                       bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=15)
    button.pack(side=tk.TOP, pady=10)

    # Кнопка "Выйти" с измененным цветом фона и текста
    exit_button = tk.Button(frame, text="Выйти", command=sys.exit,
                            bg=button_bg_color, fg=button_fg_color, font=button_font, height=2, width=15)
    exit_button.pack(side=tk.TOP, pady=10)

    root.mainloop()
