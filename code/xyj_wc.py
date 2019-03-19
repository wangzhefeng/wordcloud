#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import jieba.analyse
from PIL import Image
import random

#===========================================================
#                        codeing
#===========================================================
# 打开文本 jieba分词
text = open("..\\data\\xyj.txt", encoding = "utf-8").read()
# text = ' '.join(jieba.cut(text))
# print(text[:100])

# 提取关键字和权重
freq = jieba.analyse.extract_tags(text, topK = 200, withWeight = True)
print(freq[:20])
freq = {i[0]: i[1] for i in freq}

# 自定义控制字体颜色...
def random_color(word, font_size, position, orientation, font_path, random_state):
	s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
	print(s)
	return s

# 背景图设置
# mask = np.array(Image.open("..\\background_img\\black_mask.png"))
mask = np.array(Image.open("..\\background_img\\color_mask.png"))

# 设置词云
font_path = "..\\font\\Hiragino.ttf"
# wc = WordCloud(font_path = font_path, 
# 			   mask = mask,
# 			   # color_func = random_color,
# 			   # width = 800, 
# 			   # height = 600, 
# 			   mode = "RGBA", 
# 			   background_color = None).generate(text)
wc = WordCloud(font_path = font_path, 
			   mask = mask,
			   mode = "RGBA",
			   background_color = None).generate_from_frequencies(freq)


# 词云重上色
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func = image_colors)

# 词云输出
plt.imshow(wc)
plt.axis("off")
plt.show()
# wc.to_file("..\\imgs\\xyj.png")
# wc.to_file("..\\imgs\\xyj_cut.png")
# wc.to_file("..\\imgs\\xyj_mask_black.png")
# wc.to_file("..\\imgs\\xyj_mask_color.png")
# wc.to_file("..\\imgs\\xyj_random_color.png")
wc.to_file("..\\imgs\\xyj_freq_color.png")