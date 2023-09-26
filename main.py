from field import Ant
import numpy as np
from PIL import Image
import seaborn as sns


field = (1024, 1024)
coords = (512, 512)
ant = Ant(field=field, coords=coords)


while True:
    if not ant.move():
        break


data = Image.fromarray(ant.field.astype(dtype=bool))  # .convert('L')
data.save("ant_field.bmp")
print(sum(ant.field[ant.field == 1]))
print(ant.field)
