from logics import *
import pygame
import sys
from database import get_best, cur

GAMERS_DB = get_best()


def draw_top_gamers():
    font_top = pygame.font.SysFont("simsun", 30)
    font_gamer = pygame.font.SysFont("simsun", 24)
    text_head = font_top.render("Best tries:", True, COLOR_TEXT)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{index + 1}.{name} - {score}"
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (250, 30 + 30 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("simsun", 48)
    font_delta = pygame.font.SysFont("simsun", 32)
    text_score = font_score.render("Score:", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (170, 65))
    pretty_print(mas)
    draw_top_gamers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0),
    128: (255, 130, 0),
    # 256:
    # 512:
    # 1024:
    # 2048:
}
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
score = 0
USERNAME = None

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))

# for gamer in get_best():
#   print(gamer)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def draw_intro():
    img2048 = pygame.image.load('IMG2048.png')
    font = pygame.font.SysFont("stxingkai", 70)
    text_welcom = font.render("Welcome!", True, WHITE)
    name = 'Enter name'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcom, (230, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    img2048 = pygame.image.load('IMG2048.png')
    font = pygame.font.SysFont("stxingkai", 65)
    text_game_over = font.render("Game over!", True, WHITE)
    text_score = font.render(f"You have {score} points ", True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "New record"
    else:
        text = f"Record {best_score}"
    text_record = font.render(text, True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        pygame.display.update()


draw_intro()

draw_interface(score)
pygame.display.update()
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                print(f'Мы заполнили элемент под номером {random_num}')
            pretty_print(mas)
            draw_interface(score, delta)
            pygame.display.update()

    print(USERNAME)

draw_game_over()