from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import requests
import sys




def color_1(img, delta):
    print('Введите значения r,g,b (0-255) через enter')
    r1 = int(input())
    g1 = int(input())
    b1 = int(input())
    im = Image.open(img)
    pix = im.load()
    im1 = im.copy()
    pix1 = im1.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            pix[i, j] = r1, g1, b1
    im.save('color.jpeg')


def color_2(img):
    im = Image.open(img)
    pix = im.load()
    x, y = im.size
    r_new, g_new, b_new = pix[x / 2, y / 2]
    print(r_new, g_new, b_new)


print("Для генерации цвета по заданным параметрам r,g,b введите 1")
print("Для определения параметров r,g,b цвета по ссылке введите 2")
flag = int(input())

if flag == 1:
    color_1('temporary.jpg', 10)
if flag == 2:
    print(
        'Введите ссылку на картинку в формате .jpg (Для точного опредеения картинка должна состоять из одинаковых пикселей(быть монотонной))')
    url = input()
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        sys.exit(1)

    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        sys.exit(1)
    img.save('temporary.jpg', 'jpeg')
    enhancer = ImageEnhance.Contrast(img)
    factor = 1
    im_output = enhancer.enhance(factor)
    im_output.save('temporary.jpg', 'jpeg')
    color_2('temporary.jpg')


