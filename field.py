import numpy as np
from typing import NamedTuple


# class Coordinates(NamedTuple):
#     row: int
#     col: int


class Ant:

    def __init__(self, field: tuple, coords: tuple):
        self.field = np.zeros(field, dtype=int)
        self.coords = np.array((coords[0]-1, coords[1]-1), dtype=int)
        self.step = np.array([1, 0])
        self.direction = -1

    def move(self) -> bool:
        if self.field[self.coords[0], self.coords[1]] == 0:
            self.direction = self.change_direction(0)  # меняем направление
        else:
            self.direction = self.change_direction(1)  # меняем направление
        self.field[self.coords[0], self.coords[1]] = abs(self.field[self.coords[0], self.coords[1]] - 1)  # инверт пиксель
        self.step = np.flip(m=self.step)  # перемещаемся вперед
        step_ = self.step * self.direction
        self.coords += step_
        # print(self.field, '\n', (self.step, self.direction))
        # print()
        if self.coords[0] in [0, 1023] or self.coords[1] in [0, 1023]:
            return False
        return True

    def change_direction(self, x: int) -> int:
        if x == 0:
            if self.step[0] == 1 and self.direction == -1:
                return 1
            elif self.step[0] == 0 and self.direction == 1:
                return 1
            elif self.step[0] == 1 and self.direction == 1:
                return -1
            elif self.step[0] == 0 and self.direction == -1:
                return -1
        elif x == 1:
            if self.step[0] == 1 and self.direction == -1:
                return -1
            if self.step[0] == 0 and self.direction == 1:
                return -1
            elif self.step[0] == 1 and self.direction == 1:
                return 1
            elif self.step[0] == 0 and self.direction == -1:
                return 1

    def __str__(self) -> str:
        return (f"{self.field},\n"
                f"{self.coords},\n"
                f" {self.direction}")


if __name__ == '__main__':
    field_ = (8, 8)
    # coordinates = Coordinates(512, 512)
    ant = Ant(field_, (4, 4))
    print(ant)
