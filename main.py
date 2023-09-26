from field import Ant
from PIL import Image


field = (1024, 1024)
coords = (512, 512)
ant = Ant(field=field, coords=coords)


while True:
    if not ant.move():
        break


data = Image.fromarray(ant.field.astype(dtype=bool))  # .convert('L')
data.save("ant_track.bmp")
print("Quantity of black pixels =", (1024*1024) - sum(ant.field[ant.field == 1]))

