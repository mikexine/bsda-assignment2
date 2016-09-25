#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import random


stopwords = set(STOPWORDS)


def grey_color_func(word, font_size, position, orientation,
                    random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(10, 20)


def create_wordcloud(text, mask, target_file):
    mask = np.array(Image.open(mask))
    wc = WordCloud(background_color="white", max_words=2000,
                   mask=mask, stopwords=stopwords, width=2000,
                   height=2000, scale=3)
    wc.generate(text)
    wc.recolor(color_func=grey_color_func, random_state=3)
    wc.to_file(target_file)
    return True
