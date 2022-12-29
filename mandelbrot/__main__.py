from PIL import Image
from mandelbrot.fractal import draw_mandelbrot


SIZE_W = 30000
SIZE_H = 30000



def main():
    bitmap = Image.new("RGB", (SIZE_W, SIZE_H), "white")
    pixels = bitmap.load()

    draw_mandelbrot(pixels, SIZE_W, SIZE_H)

    bitmap.save("../bin/mandel.jpg")


if __name__ == "__main__":
    main()
