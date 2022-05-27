from help_class import *

pygame.init()

WIDTH = 728  # ширина игрового окна
HEIGHT = 728  # высота игрового окна

HEIGHT_CELL = 76
WIDTH_CELL = 76
COUNT_CELL_IN_RAW = 8
BORDER = 13

LIGHT_BLUE = (77, 146, 165)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BEIGE = (230, 218, 166)
BROWN = (162, 95, 42)
RED = (255, 0, 0)
DARK_BROWN = (120, 60, 0)
SIZE_FONT = 20
test_surface = pygame.Surface((10, 10))
test_surface.fill(RED)

font = pygame.font.Font(None, SIZE_FONT)

ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def print_cells(cells, screen):
    for index_cells in range(8):  # отрисовка клеток
        for index_cell in range(8):
            surface = cells[index_cells][index_cell].get_surface
            coords = cells[index_cells][index_cell].get_coords
            screen.blit(surface, coords)


def print_number_move(story_moves, screen):
    for index in range(len(story_moves)):  # отрисовка номера хода
        screen.blit(font.render(f"{index + 1}", True, BLACK), story_moves[index].get_number_coords)


def print_border(screen):
    y = (HEIGHT // 2 - COUNT_CELL_IN_RAW // 2 * HEIGHT_CELL) - BORDER + 2  # отрисовка рамки
    x = (WIDTH // 2 - COUNT_CELL_IN_RAW // 2 * WIDTH_CELL) - BORDER + 2
    pygame.draw.rect(screen, DARK_BROWN, (x - 2, y - 2, WIDTH_CELL * 8 + BORDER * 1.8, HEIGHT_CELL * 8 + BORDER * 1.8),
                     BORDER)


def print_coords_on_border(cells, screen):
    for number in range(8):  # отрисовка цифр и букв на рамке
        x = cells[7 - number][0].get_coords[0] - SIZE_FONT // 2  # цифры
        y = cells[7 - number][0].get_coords[1] + HEIGHT_CELL // 2 - BORDER // 2
        screen.blit(font.render(f"{number + 1}", True, LIGHT_BLUE), (x, y))

        x = cells[7][number].get_coords[0] + WIDTH_CELL // 2  # буквы
        y = cells[7][number].get_coords[1] + HEIGHT_CELL - BORDER // 3
        screen.blit(font.render(f"{ABC[number]}", True, LIGHT_BLUE), (x, y))


def print_board(cells, story_moves, screen):
    print_cells(cells, screen)
    print_number_move(story_moves, screen)
    print_border(screen)
    print_coords_on_border(cells, screen)


def generation_cells():  # генерация клеток
    cells = [[0 for i in range(8)] for j in range(8)]

    for index_cells in range(8):
        y = (HEIGHT // 2 - COUNT_CELL_IN_RAW // 2 * HEIGHT_CELL) + (HEIGHT_CELL * index_cells)
        for index_cell in range(8):
            x = (WIDTH // 2 - COUNT_CELL_IN_RAW // 2 * WIDTH_CELL) + (WIDTH_CELL * index_cell - 1)

            surf = My_Surface(HEIGHT_CELL, WIDTH_CELL, index_cell, index_cells)

            if index_cells % 2 == 0 and index_cell % 2 == 0 or index_cells % 2 == 1 and index_cell % 2 == 1:
                surf.get_surface.fill(BEIGE)

            if index_cells % 2 == 1 and index_cell % 2 == 0 or index_cells % 2 == 0 and index_cell % 2 == 1:
                surf.get_surface.fill(BROWN)

            surf.set_coords(x, y)

            cells[index_cells][index_cell] = surf

    return cells
