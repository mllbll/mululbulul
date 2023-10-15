from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt
import requests
import sys
import glob

# url = 'ссылка на фото'
url='Papa_smurf.jpg'

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
factor = 0.8
im_output = enhancer.enhance(factor)
im_output.save('temporary.jpg', 'jpeg')


def shrek(img, delta):
    im = Image.open(img)
    pix = im.load()
    im1 = im.copy()
    pix1 = im1.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            pix[i, j] = r, g, b
            pix1[i, j] = b, g, r
    for i in range(x - delta):
        for j in range(y):
            r, g, b = pix[i + delta, j]
            r1, g1, b1 = pix1[i, j]
            pix[i + delta, j] = r1, g, b
    im.save('shrek.jpeg')


shrek('temporary.jpg', 10)