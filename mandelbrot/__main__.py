from PIL import Image


def main():
    bitmap = Image.new("RGB", (500, 500), "white")
    # TODO: implement rendering
    bitmap.save("mandel.jpg")


if __name__ == "__main__":
    main()
