# -*- coding = utf-8 -*-
# @Time : 2021/2/9 9:55 下午
# @Author : 汪文涛
# @File : imageConverter.py
# @Software : PyCharm 

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import cv2


#  draw函数对图像进行处理
def draw(pic, draw_text):
    img = cv2.imread(pic)
    blank = Image.new("RGB", [img.shape[1], img.shape[0]], "white")
    drawObj = ImageDraw.Draw(blank)
    n = 10
    m = 10
    font_path = "simsun.ttf"
    font = ImageFont.truetype(font_path, size=m)
    for i in range(0, img.shape[0], n):
        for j in range(0, img.shape[1], n):
            drawObj.text([j, i], draw_text[int(j / n) % len(draw_text)],
                         fill=(img[i][j][2], img[i][j][1], img[i][j][0]),
                         font=font)

    return blank
