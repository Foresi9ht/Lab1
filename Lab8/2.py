from tkinter import *
import pygame
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 120
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# Класс для представления змейки
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []  # координаты змейки
        self.squares = []      # квадраты (сегменты) змейки на холсте

        # Инициализация координат и создание сегментов змейки на холсте
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for i, (x, y) in enumerate(self.coordinates):
            x = int(x)
            y = int(y)
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Класс для представления еды на игровом поле
class Food:

    def __init__(self):

        # Генерация случайных координат для еды
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Создание еды на холсте
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Функция для обработки следующего хода игры
def next_turn(snake, food):

    x, y = snake.coordinates[0]

    # Изменение координат в соответствии с направлением движения
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Добавление новой головы змейки
    snake.coordinates.insert(0, (x, y))

    # Создание нового сегмента змейки на холсте
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    # Проверка на съедание еды
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        # Удаление хвоста змейки, если еда не съедена
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Проверка на столкновения с границами или самой собой
    if check_collisions(snake):
        game_over()
    else:
        # Вызов следующего хода через определенный интервал времени
        window.after(SPEED, next_turn, snake, food)

# Функция для изменения направления движения змейки
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Функция для проверки столкновений
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

# Функция для завершения игры
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

# Создание основного окна
window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

# Метка для отображения счета
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# Холст для рисования игровых элементов
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Вычисление позиции окна по центру экрана
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Привязка клавиш к функции изменения направления змейки
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Создание змейки и еды, запуск игры
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
