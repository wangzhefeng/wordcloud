#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
WordCloud(font_path,
		  width,
		  height,
		  mask,
		  min_font_size,
		  )
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 打开文本
text = open("..\\data\\constitution.txt").read()

# 生成对象
wc = WordCloud().generate(text)

# 显示词云
plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("..\\imgs\\wordcloud.png")
