# coding: utf-8
__author__ = 'air'

import itertools

from train_gensim import load_gensim

def parse_dict():
    dict = {}
    word_positive = []
    word_negative = []
    y_positive = []
    y_negative = []
    with open('rus_dic.txt', 'r') as f:
        sentences = f.read().split('\n')
        sentences = [s.split() for s in sentences]

    for i in range(len(sentences)):
        word = sentences[i][2][6:].decode('utf-8')
        dict['word'] = word
        y = sentences[i][5][14:]

        if y == 'positive':
            word_positive.append(word)
            y_positive.append(1)
            dict['sent'] = 1

        if y == 'negative':
            word_negative.append(word)
            y_negative.append(0)
            dict['sent'] = 0

    word_norm = []
    words = []
    ys = []
    ys_1 = []
    w2v = load_gensim()

    for word in word_positive:
        w = word.encode('utf-8')
        word_norm.append(w.decode('utf-8'))
        if w in w2v:
            words.append(w2v[w])
            ys_1.append(1)
        ys.append(1)
    for word in word_negative:

        w = word.encode('utf-8')
        word_norm.append(w.decode('utf-8'))
        if w in w2v:
            words.append(w2v[w])
            ys_1.append(0)
        ys.append(0)

    return word_norm, words, ys, ys_1


if __name__ == '__main__':
    word_norm, words, ys, ys_1 = parse_dict()