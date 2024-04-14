# Импорт библиотеки pygame
import pygame

# Инициализация pygame
pygame.init()

# Установка количества кадров в секунду
fps = 60

# Создание объекта часов для управления частотой кадров
timer = pygame.time.Clock()

# Установка ширины и высоты окна
WIDTH = 800
HEIGHT = 600

# Инициализация переменных для рисования
active_size = 0
active_color = 'white'
eraser_color = 'white'
drawing_mode = 'circle'
painting = []

# Создание игрового окна
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Установка заголовка окна
pygame.display.set_caption('Paint!')

# Функция для отрисовки меню
def draw_menu(size, color, mode):
    # Отрисовка фона меню
    pygame.draw.rect(screen, 'grey', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Отрисовка кистей
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    brush_list = [xl_brush, l_brush]

    # Отрисовка вариантов цвета
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    eraser = pygame.draw.rect(screen, eraser_color, [WIDTH - 90, 10, 25, 25])
    color_rect = [blue, red, green, yellow, eraser]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), 'eraser']

    # Подсветка активной кнопки режима рисования
    if mode == 'circle':
        pygame.draw.rect(screen, 'lightgray', [200, 10, 80, 50])
    pygame.draw.rect(screen, 'black', [200, 10, 80, 50], 3)
    pygame.draw.circle(screen, 'black', (240, 35), 20)

    if mode == 'rectangle':
        pygame.draw.rect(screen, 'lightgray', [300, 10, 80, 50])
    pygame.draw.rect(screen, 'black', [300, 10, 80, 50], 3)
    pygame.draw.rect(screen, 'black', [310, 20, 60, 30])

    return brush_list, color_rect, rgb_list

# Функция для отрисовки рисунка
def draw_painting(paints):
    for paint in paints:
        if paint[0] == 'rectangle':
            pygame.draw.rect(screen, paint[1], paint[2])
        else:
            pygame.draw.circle(screen, paint[0], paint[1], paint[2])

# Основной игровой цикл
run = True
while run:
    timer.tick(fps)  # Ограничение частоты кадров

    # Заливка экрана белым цветом
    screen.fill('white')

    # Получение позиции мыши и статуса левой кнопки мыши
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    # Обработка рисования
    if left_click and mouse[1] > 70:
        if drawing_mode == 'circle':
            color_to_use = eraser_color if pygame.mouse.get_pressed()[2] else active_color
            painting.append((color_to_use, mouse, active_size))
        elif drawing_mode == 'rectangle':
            painting.append(('rectangle', active_color, pygame.Rect(mouse[0] - active_size, mouse[1] - active_size, active_size * 2, active_size * 2)))

    # Отрисовка рисунка
    draw_painting(painting)

    # Отрисовка меню и обработка событий
    brushes, colors, rgbs = draw_menu(active_size, active_color, drawing_mode)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Проверка выбора размера кисти
            for i in range(len(brushes)):
                if brushes[i].collidepoint(mouse_pos):
                    active_size = 20 - (i * 5)
            # Проверка выбора цвета
            for i in range(len(colors)):
                if colors[i].collidepoint(mouse_pos):
                    mode_or_color = rgbs[i]
                    if mode_or_color == 'rectangle' and drawing_mode != 'rectangle':
                        drawing_mode = 'rectangle'
                    elif mode_or_color == 'circle':
                        drawing_mode = 'circle'
                    else:
                        active_color = mode_or_color

            # Проверка выбора режима рисования
            if 200 < mouse_pos[0] < 280 and 10 < mouse_pos[1] < 60:
                drawing_mode = 'circle'
            elif 300 < mouse_pos[0] < 380 and 10 < mouse_pos[1] < 60:
                drawing_mode = 'rectangle'

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
