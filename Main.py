# -*- coding = utf-8 -*-
# @Time : 2021/2/10 10:33 上午
# @Author : 汪文涛
# @File : Main.py
# @Software : PyCharm 

import os
from imageConverter.Draw import draw

dirIn = "untransformedImages/"  # 未处理照片的文件夹
dirOut = "transformedImages/"  # 处理过的照片的文件夹

picsNameList = os.listdir(dirIn)  # 将所有未处理的照片名封装成列表
if '.DS_Store' in picsNameList:  # Mac电脑的毛病
    picsNameList.remove('.DS_Store')

# 设置for循环，对每张照片处理
for picName in picsNameList:
    picPath = dirIn + picName
    transPic = draw(picPath, "我爱你")
    saveName = dirOut + 'trans_' + picName  # 设置保存处理完图像的路径
    transPic.save(saveName)
