import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
eraser_color = 'white'  
drawing_mode = 'circle'
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint!')
painting = []

def draw_menu(size, color):
    pygame.draw.rect(screen, 'grey', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [80, 20, 30, 30])
    brush_list = [xl_brush, l_brush]
    
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH -35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH -35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH -60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH -60, 35, 25, 25])
    eraser = pygame.draw.rect(screen, eraser_color, [WIDTH -90, 10, 25, 25])
    color_rect = [blue, red, green, yellow, eraser]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), 'eraser']
    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    for paint in paints:
        if paint[0] == 'rectangle':
            pygame.draw.rect(screen, paint[1], paint[2])
        else:
            pygame.draw.circle(screen, paint[0], paint[1], paint[2])


run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        if drawing_mode == 'circle':
            color_to_use = eraser_color if pygame.mouse.get_pressed()[2] else active_color
            painting.append((color_to_use, mouse, active_size))
        elif drawing_mode == 'rectangle':
            painting.append(('rectangle', active_color, pygame.Rect(mouse[0] - active_size, mouse[1] - active_size, active_size * 2, active_size * 2)))
    draw_painting(painting)
    if mouse[1] > 70:
        if drawing_mode == 'circle':
            color_to_use = eraser_color if pygame.mouse.get_pressed()[2] else active_color
            pygame.draw.circle(screen, color_to_use, mouse, active_size)
        elif drawing_mode == 'rectangle':
            pygame.draw.rect(screen, active_color, (mouse[0] - active_size, mouse[1] - active_size, active_size * 2, active_size * 2))
    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    mode_or_color = rgbs[i]
                    if mode_or_color == 'rectangle':
                        drawing_mode = 'rectangle'
                    elif mode_or_color == 'circle':
                        drawing_mode = 'circle'
                    else:
                        active_color = mode_or_color
                
    pygame.display.flip()
pygame.quit()
