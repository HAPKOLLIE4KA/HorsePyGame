import pygame


class My_Surface():

    def __init__(self, height, width, matrix_x, matrix_y):
        self._height = height
        self._width = width
        self._coords = (0, 0)
        self._horse_coords = (0, 0)
        self._number_coords = (0, 0)
        self._surface = pygame.Surface((height, width))
        self._coords_matrix = (matrix_x, matrix_y)

    @property
    def get_surface(self) -> pygame.Surface:
        return self._surface

    @property
    def get_coords(self):
        return self._coords

    @property
    def get_horse_coords(self):
        return self._horse_coords

    @property
    def get_number_coords(self):
        return self._number_coords

    @property
    def get_coords_matrix(self):
        return self._coords_matrix

    def set_coords(self, coord_x, coord_y):
        self._coords = (coord_x, coord_y)

        self._horse_coords = (coord_x + self._width // 4, coord_y + self._height // 4)

        self._number_coords = (coord_x + 3, coord_y + 3)

    def __str__(self):
        return str(self._surface)
