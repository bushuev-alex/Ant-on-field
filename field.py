import numpy as np



class Ant:

    def __init__(self, field: tuple, coords: tuple):
        self.field = np.ones(field, dtype=int)
        self.coords = np.array((coords[0]-1, coords[1]-1), dtype=int)
        self.step = np.array([1, 0])
        self.direction = -1

    def move(self) -> bool:

        # меняем направление в зависимости от цвета точки
        if self.field[self.coords[0], self.coords[1]] == 1:
            self.direction = self.change_direction(1)
        else:
            self.direction = self.change_direction(0)

        # инвертируем пиксель
        self.field[self.coords[0], self.coords[1]] = abs(self.field[self.coords[0], self.coords[1]] - 1)

        # перемещаемся вперед
        self.step = np.flip(m=self.step)
        self.coords += (self.step * self.direction)

        # проверка достижения границы/края
        if (self.coords[0] in [0, self.field.shape[1]]) or (self.coords[1] in [0, self.field.shape[1]]):
            return False  # если достиг границы/края
        return True

    def change_direction(self, x: int) -> int:
        if x == 1:
            if self.step[0] == 1 and self.direction == -1:
                return 1
            elif self.step[0] == 0 and self.direction == 1:
                return 1
            elif self.step[0] == 1 and self.direction == 1:
                return -1
            elif self.step[0] == 0 and self.direction == -1:
                return -1
        elif x == 0:
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
    ant = Ant(field_, (4, 4))
    print(ant)
