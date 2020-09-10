# Импорт библиотеки pygame
import pygame
from Sudoku_backtracking import *
from copy import deepcopy


def drawing(sudoku):
    # Очищаем экран
    screen.fill(white)

    # делаем фон
    dog_surf = pygame.image.load('paper.jpg')
    dog_rect = dog_surf.get_rect(bottomright=(730, 590))
    screen.blit(dog_surf, dog_rect)

    # Рисуем сетку
    for i in range(0, d_board + 1, step):
        if (i // step) % 3 == 0:  # каждая тертья линия толстая
            wid = 5
        else:
            wid = 3
        pygame.draw.line(screen, grid_color, [0 + i + shift, 0 + shift], [0 + i + shift, d_board + shift], wid)
        pygame.draw.line(screen, grid_color, [0 + shift, 0 + i + shift], [d_board + shift, 0 + i + shift], wid)

    # рисуем кнопку выхода
    pygame.draw.ellipse(screen, [159, 72, 178], button)  # draw button

    font = pygame.font.Font(None, 38)  # задаем шрифт
    text = font.render('Exit', True, black)  # пишим текст
    screen.blit(text, [602, 83])

    # рисуем кнопку очистки судоку
    pygame.draw.ellipse(screen, [222, 179, 235], button_clear)  # draw button

    font = pygame.font.Font(None, 30)  # задаем шрифт
    text = font.render('Clear', True, black)  # пишим текст
    screen.blit(text, [602, 172])
    text = font.render('board', True, black)  # пишим текст
    screen.blit(text, [602, 190])

    # рисуем кнопку шаблона
    pygame.draw.ellipse(screen, [195, 92, 118], button_template)

    text = font.render('Solve', True, black)  # пишим текст
    screen.blit(text, [602, 272])
    text = font.render('template', True, black)  # пишим текст
    screen.blit(text, [587, 290 ])

    # пишем инстукцию
    font = pygame.font.Font(None, 25)
    text = font.render('Press "Enter"', True, black)
    screen.blit(text, [560, 410])
    text = font.render('to solve sudoku.', True, black)
    screen.blit(text, [560, 425])
    text = font.render('Press "Enter" twice', True, black)
    screen.blit(text, [560, 450])
    text = font.render('to show the result.', True, black)
    screen.blit(text, [560, 465])
    text = font.render('Press "Delete"', True, black)
    screen.blit(text, [560, 490])
    text = font.render('to delete last', True, black)
    screen.blit(text, [560, 505])
    text = font.render('input.', True, black)
    screen.blit(text, [560, 520])


    # вывод количества обновлений экрана
    font = pygame.font.Font(None, 20)  # задаем шрифт
    text = font.render("Frames: " + str(Frame), True, black)  # пишим текст
    screen.blit(text, [605, 10])  # выводим текст (колличество обновлений экрана)


    for i in range(0, d_board - step + 1, step):
        for j in range(0, d_board - step + 1, step):
            if sudoku[i // 60][j // 60][1]:  #
                font = pygame.font.Font(None, 40)
                num_col = [102, 0, 0]  # pink
            else:
                font = pygame.font.Font(pygame.font.match_font('chiller'), 36)
                num_col = [51, 51, 51]
            text = font.render(sudoku[i // 60][j // 60][0], True, num_col)
            screen.blit(text, [22 + j + shift, 20 + i + shift])


def solve(su):
    find = find_(su.board)
    if not find:
        return True

    for i in [str(i) for i in range(1, 10)]:
        if valid_(su.board, i, find):
            su.board[find[0]][find[1]][0] = i

            intermediate_steps.append(deepcopy(su.board))

            if solve(su):
                return True

            su.board[find[0]][find[1]][0] = "."
    return False


def print_2(self):
    print("_________________________")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(self[i][j][0])
            else:
                print(self[i][j][0], end=' ')


# Инициализируем движок pygame
pygame.init()

# Определяем несколько цветов, которые мы будем использовать (RGB)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
grid_color = [51, 25, 40]
pi = 3.141592653
Frame = 1
d_board, step, shift = 540, 540 // 9, 15
ind = 0
intermediate_steps = []
# Устанавливаем размеры окна
size = [730, 590]
screen = pygame.display.set_mode(size)

button = pygame.Rect(595, 75, 65, 40)  # кнопка выхода
button_clear = pygame.Rect(590, 165, 75, 52)  # кнопка очистки экаран
button_template = pygame.Rect(578, 265, 100, 58)  # кнопка  решения и отображения шаблона

# Устанавливаем заголовок окна
pygame.display.set_caption("Sudoku solver")

# Цикл работает пока пользователь не закроет окно
done = False
clock = pygame.time.Clock()

# Объявляем нашу судоку
su = sudoku(True)
while not done:
    # Следующяя строка ограничивает наш цикл 10 кадрами в секунду.
    # Если этого не сделать, то игра будет использовать
    # максимальное колличество ресурсов.
    clock.tick(60)

    for event in pygame.event.get():  # Проходимся по событиям
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            done = True  # Сигнализируем что цикл пора завершать
        elif event.type == pygame.KEYDOWN:
            if event.key == 8:
                su.del_last()
            elif event.key == 13 and su.full == 'full':
                solve(su)
                su.full = "solved"
                print(su.full, len(intermediate_steps))

            else:
                su.insert(chr(event.key))
            # print(event.key)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # prints current location of mouse
                done = True
                # print('button was pressed at {0}'.format(mouse_pos))
            elif button_clear.collidepoint(event.pos):
                su.clear()
                intermediate_steps.clear()
            elif button_template.collidepoint(event.pos):
                su = sudoku()
    # if su.full == "full":
    #     solve(su)
    #     su.full = "solved"

    if su.full != "solved":
        drawing(su.board)
    else:

        if ind < len(intermediate_steps):
            drawing(intermediate_steps[ind])
            ind = 5 + ind if len(intermediate_steps) - ind > 6 else 1 + ind
        else:
            intermediate_steps.clear()

    Frame += 1
    pygame.display.flip()

pygame.quit()
