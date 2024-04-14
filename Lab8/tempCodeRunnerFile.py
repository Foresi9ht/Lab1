# Проверка выбора режима рисования
            if 200 < mouse_pos[0] < 280 and 10 < mouse_pos[1] < 60:
                drawing_mode = 'circle'
            elif 300 < mouse_pos[0] < 380 and 10 < mouse_pos[1] < 60:
                drawing_mode = 'rectangle'