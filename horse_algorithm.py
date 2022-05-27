moves = [[0 for i in range(8)] for j in range(8)]

def check_value(min_value, current_value, x, y, min_x, min_y):
    if current_value < min_value:
        min_value = current_value
        min_x = x
        min_y = y

    return min_x, min_y, min_value


def new_move(moves, position_x, position_y):
    min_value, min_x, min_y = 1000, 0, 0

    for axis_x in range(position_x - 2, position_x + 2 + 1, 4):

        if 0 <= position_y - 1 < 8 and 0 <= axis_x < 8 and moves[position_y - 1][axis_x] != 1:  # убирает точки, которые выъодят за границу доски и на которых конь уже был
            value_rating = calculate_rating(moves, axis_x, position_y - 1)  # подсчёт значения рейтинга
            min_x, min_y, min_value = check_value(min_value, value_rating, axis_x, position_y - 1, min_x,
                                                  min_y)  # проверка на минимальное значение
            # print(axis_x, position_y - 1, value_rating)

        if 0 <= position_y + 1 < 8 and 0 <= axis_x < 8 and moves[position_y + 1][axis_x] != 1:
            value_rating = calculate_rating(moves, axis_x, position_y + 1)
            min_x, min_y, min_value = check_value(min_value, value_rating, axis_x, position_y + 1, min_x, min_y)
            # print(axis_x, position_y + 1, value_rating)

    for axis_y in range(position_y - 2, position_y + 2 + 1, 4):

        if 0 <= position_x - 1 < 8 and 0 <= axis_y < 8 and moves[axis_y][position_x - 1] != 1:
            value_rating = calculate_rating(moves, position_x - 1, axis_y)
            min_x, min_y, min_value = check_value(min_value, value_rating, position_x - 1, axis_y, min_x, min_y)
            # print(position_x - 1, axis_y, value_rating)

        if 0 <= position_x + 1 < 8 and 0 <= axis_y < 8 and moves[axis_y][position_x + 1] != 1:
            value_rating = calculate_rating(moves, position_x + 1, axis_y)
            min_x, min_y, min_value = check_value(min_value, value_rating, position_x + 1, axis_y, min_x, min_y)
            # print(position_x + 1, axis_y, value_rating)

    if min_value == 1000:
        return -1000, -1000

    return min_x, min_y


def check_rating(x, y, moves):
    if 0 <= x < 8 and 0 <= y < 8 and (moves[y][x] != 1):
        return 1
    return 0


# position_x, position_y - координаты клетки, рейтинг которой надо посчитать
def calculate_rating(moves, position_x, position_y):
    value_rating = 0

    for axis_x in range(position_x - 2, position_x + 2 + 1, 4):
        value_rating += check_rating(axis_x, position_y + 1, moves)
        value_rating += check_rating(axis_x, position_y - 1, moves)

    for axis_y in range(position_y - 2, position_y + 2 + 1, 4):
        value_rating += check_rating(position_x - 1, axis_y, moves)
        value_rating += check_rating(position_x + 1, axis_y, moves)

    return value_rating

