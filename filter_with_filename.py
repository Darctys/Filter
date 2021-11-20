from PIL import Image
import numpy as np
from numpy import array


def get_grayscale(x, y):
    gray = 0
    for windows_x in range(x, min(x + width_img // width_moz, width_img)):
        for windows_y in range(y, min(y + height_img // height_moz, height_img)):
            R = img_arr[windows_x][windows_y][0]
            G = img_arr[windows_x][windows_y][1]
            B = img_arr[windows_x][windows_y][2]
            gray += (int(R) + int(G) + int(B)) / 3
    return int(gray // 100)


def make_chunk_grey_pictures(x, y, grayscale):
    for windows_X in range(x, min(x + width_img // width_moz, width_img)):
        for windows_Y in range(y, min(y + height_img // height_moz, height_img)):
            img_arr[windows_X][windows_Y] = [int(grayscale // 50 * grayscale_step) * grayscale_step * 50] * 3
    return img_arr


def make_grey_pictures():
    global img_arr
    x = 0
    while x < width_img - 1:
        y = 0
        while y < height_img - 1:
            grayscale = get_grayscale(x, y)
            img_arr = make_chunk_grey_pictures(x, y, grayscale)
            y = y + width_img // width_moz
        x = x + height_img // height_moz
    res = Image.fromarray(img_arr)
    res.save(result_file)



file = 'D:\\Хакатон\\Filter\\img2.jpg'
result_file = 'D:\\Хакатон\\Filter\\img1.jpg'
img_arr = array(Image.open(file))
width_img = len(img_arr)
height_img = len(img_arr[1])

width_moz = 10

height_moz = 10

grayscale_step = 1
make_grey_pictures()