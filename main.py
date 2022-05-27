from board import *
from horse_algorithm import *


def main():
    FPS = 30  # частота кадров в секунду

    running = True

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(GRAY)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    horse_image = pygame.image.load("images/horse3.png")

    cells = generation_cells()

    click_start_position = False
    position_x, position_y = 0, 0

    story_moves = []

    auto_move = False

    while running:
        next_move = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif click_start_position and event.type == pygame.KEYDOWN:  # управление клавишами
                if event.key == pygame.K_SPACE:
                    FPS = 2
                    auto_move = not auto_move

                if event.key == pygame.K_RIGHT:
                    FPS = 15
                    auto_move = False
                    next_move = True

                if event.key == pygame.K_LEFT and len(story_moves) > 1:
                    FPS = 15
                    auto_move = False
                    moves[position_y][position_x] = 0
                    position_x, position_y = story_moves[-2].get_coords_matrix
                    story_moves.pop()

                if event.key == pygame.K_UP:
                    FPS += 1

                    if FPS > 6: FPS = 6

                if event.key == pygame.K_DOWN:
                    FPS -= 1
                    if FPS < 2: FPS = 2

                if event.key == pygame.K_RETURN:
                    FPS = 150


            elif not click_start_position and event.type == pygame.MOUSEBUTTONDOWN:  # установка изначальной позиции
                cursor_position = event.pos

                for row in range(8):
                    for column in range(8):
                        cell_position = cells[row][column].get_coords
                        if cell_position[0] <= cursor_position[0] <= cell_position[0] + WIDTH_CELL and \
                                cell_position[1] <= cursor_position[1] <= cell_position[1] + HEIGHT_CELL:
                            story_moves += [cells[row][column]]
                            moves[row][column] = 1
                            position_x, position_y = column, row
                            click_start_position = True

        screen.fill(GRAY)

        print_board(cells, story_moves, screen)

        if click_start_position:
            screen.blit(horse_image, cells[position_y][position_x].get_horse_coords)

        if auto_move or next_move:

            x, y = new_move(moves, position_x, position_y)
            if (x, y) != (-1000, -1000):
                position_x, position_y = x, y
                moves[position_y][position_x] = 1
                story_moves += [cells[position_y][position_x]]

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
