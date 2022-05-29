from board import *
from horse_algorithm import *


def main():
    FPS = 30  # частота кадров в секунду

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(GRAY)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    horse_image = pygame.image.load("images/horse3.png")
    cells = generation_cells()

    position_x, position_y = 0, 0

    story_moves = []

    running = True
    click_start_position = False  # начальная позиция выбрана или нет
    auto_move = False  # автоходы
    tapLeft = False  # нажатие на стрелку влево
    next_move = False  # следующий ход по конпке

    while not click_start_position:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                click_start_position = True

            if event.type == pygame.MOUSEBUTTONDOWN:  # установка изначальной позиции
                cursor_position = event.pos

                for row in range(COUNT_CELL_IN_RAW):
                    for column in range(COUNT_CELL_IN_RAW):
                        cell_position = cells[row][column].get_coords
                        if cell_position[0] <= cursor_position[0] <= cell_position[0] + WIDTH_CELL and \
                                cell_position[1] <= cursor_position[1] <= cell_position[1] + HEIGHT_CELL:
                            story_moves += [cells[row][column]]
                            moves[row][column] = 1
                            position_x, position_y = column, row
                            click_start_position = True

        screen.fill(GRAY)
        print_board(cells, story_moves, screen)

        clock.tick(FPS)
        pygame.display.flip()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif (event.type == pygame.KEYDOWN):  # управление клавишами
                if event.key == pygame.K_SPACE:
                    FPS = 2
                    auto_move = not auto_move

                if event.key == pygame.K_RIGHT:  # нажатие на стрелку вправо
                    FPS = 8
                    auto_move = False
                    next_move = True

                if event.key == pygame.K_LEFT:  # нажатие на стрелку влево
                    FPS = 10
                    auto_move = False
                    tapLeft = True

                if event.key == pygame.K_UP:  # ускорение для автохода
                    FPS += 1

                    if FPS > 6: FPS = 6

                if event.key == pygame.K_DOWN:
                    FPS -= 1
                    if FPS < 2: FPS = 2

                if event.key == pygame.K_RETURN:  # переход в самый конец
                    FPS = 150

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    tapLeft = False
                    next_move = False

        if tapLeft and len(story_moves) > 1:  # ход назад
            moves[position_y][position_x] = 0
            position_x, position_y = story_moves[-2].get_coords_matrix
            story_moves.pop()

        if auto_move or next_move:  # следующий ход коня

            x, y = new_move(moves, position_x, position_y)
            if (x, y) != (-1000, -1000):
                position_x, position_y = x, y
                moves[position_y][position_x] = 1
                story_moves += [cells[position_y][position_x]]

        screen.fill(GRAY)  # отрисовка
        print_board(cells, story_moves, screen)
        screen.blit(horse_image, cells[position_y][position_x].get_horse_coords)

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
