# coding: utf-8
__author__ = 'air'

from gensim.models import Word2Vec
from os.path import exists

file_name_model = 'model_w2v.bin'


def load_gensim():
    if exists(file_name_model):
        w2v = Word2Vec.load(file_name_model)
    else:
        with open('hotels.txt') as f:
            sentences = f.read().split('\n')
            sentences = [s.split() for s in sentences]
        w2v = Word2Vec(sentences=sentences)
        w2v.save(file_name_model)

    return w2v


def test_model():
    w2v = load_gensim()
    while True:
        user_input = raw_input('Введите слово (или exit):')
        if user_input == 'exit':
            break
        for w, prob in w2v.most_similar(positive=[user_input]):
            print '%s\t-\t%s' % (w, prob)


if __name__ == '__main__':
    test_model()

