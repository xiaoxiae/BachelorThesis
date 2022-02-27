import numpy as np
from scipy import ndimage
from PIL import Image, ImageFilter, ImageOps, ImageDraw
from math import sqrt


def is_local_maximum(array, x, y):
    value = array[y][x]

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if not (0 <= nx < len(array[0])) or not (0 <= ny < len(array)):
                continue

            if array[ny][nx] > value:
                return False

    return True


def pyramid(im, sigma1, sigma2, iteration):
    buffer1 = np.asarray(im.copy())
    buffer2 = np.asarray(im.copy())

    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter
    buffer1 = ndimage.gaussian_filter(buffer1, sigma1)
    buffer2 = ndimage.gaussian_filter(buffer2, sigma2)

    Image.fromarray(buffer1).save(f"I_1{iteration}.jpg")
    Image.fromarray(buffer2).save(f"I_2{iteration}.jpg")

    buffer3 = buffer2 - buffer1

    Image.fromarray(buffer3).save(f"G_{iteration}.jpg")

    return Image.fromarray(buffer2)

im = ImageOps.grayscale(Image.open('input.jpg'))
im = im.resize((im.width // 2, im.height // 2))

im = pyramid(im, sqrt(2), 2, 1)
im = im.resize((int(im.width / 1.5), int(im.height / 1.5)), Image.BILINEAR)

pyramid(im, sqrt(2), 2, 2)

