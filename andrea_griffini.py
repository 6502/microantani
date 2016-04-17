from microbit import display
import microbit

d = 0

m = [[12,13,14,15,16],
     [11, 2, 3, 4,17],
     [10, 1, 0, 5,18],
     [ 9, 8, 7, 6,19],
     [24,23,22,21,20]]

L = [0, 1, 2, 3, 4]

while True:
    for y in L:
        for x in L:
            v = (d + m[y][x]) % 10
            display.set_pixel(x, y, v)
    d = (d + 1) % 25
    microbit.sleep(100)
