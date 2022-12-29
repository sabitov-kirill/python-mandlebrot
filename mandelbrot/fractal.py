from decimal import *
from complex import Complex

getcontext().prec = 150

MAGIC_CONST = 4
MAX_ITERATIONS = 255


def get_mandelbrot(Z, V):
    counter = 0

    while Z.len2() < MAGIC_CONST and counter < MAX_ITERATIONS:
        Z = Z * Z + V
        counter += 1

    return counter


def draw_mandelbrot(pixels, w, h):
    height, width = h, w

    x0, y0 = Decimal(0.47), Decimal(0.47 - 0.5)
    x1, y1 = Decimal(-0.47), Decimal(-0.47 - 0.5)

    C = Complex(Decimal(0.47), Decimal(0.30)) # forever

    for y in range(height):
        for x in range(width):
            xs = Decimal(x) / width * (x1 - x0) + x0
            ys = Decimal(y) / height * (y1 - y0) + y0
            n = get_mandelbrot(Complex(xs, ys), C)

            r = n
            b = n % 47
            g = n * n % 102

            pixels[x, y] = int(r) + (int(g) << 8) + (int(b) << 16)
