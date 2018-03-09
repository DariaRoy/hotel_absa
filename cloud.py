# coding: utf-8
__author__ = 'air'

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
# text = open(path.join(d, 'hotels.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg


def visualize(last_pair, last_count, sent):

    text_to_visualize = []
    for i in range(len(last_pair)):
        phrase = last_pair[i][0].encode('utf-8') + '_' + last_pair[i][1].encode('utf-8')
        phrase = phrase.decode('utf-8')
        if sent[i][0] == 0:
            phrase = 'a' + phrase
        text_to_visualize.extend([phrase] * last_count[i])

    text_to_visualize = ' '.join(text_to_visualize)
    text = text_to_visualize

    alice_mask = imread(path.join(d, "mask.png"))

    STOPWORDS2 = ['не', 'в', 'то', 'что', 'бы', 'но', 'а', 'был', 'тут', 'на', 'это', 'по', 'все', 'мы', 'за', 'очень', 'для', 'было', 'так', 'как', 'из', 'есть']
    STOPWORDS2 = [w.decode('utf-8') for w in STOPWORDS2]
    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=STOPWORDS2, prefer_horizontal=1.0)
    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "alice.png"))

    # show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()