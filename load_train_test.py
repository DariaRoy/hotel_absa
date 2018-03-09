# coding: utf-8
__author__ = 'air'

import sentiment
import cloud
import extract_aspect
import extract_collocation
import parsing

from sklearn.metrics import classification_report

from train_gensim import load_gensim
from parse_dict import parse_dict
from collections import Counter


TRAIN_NUM = 30


def my_name():
    print('dasha')
    W_test = parsing.parse_new('text3.txt')
    y_pred = extract_aspect.evaluate_task_new(W_test)

    print(len(W_test), len(y_pred))
    aspects_word = []
    for i in range(len(y_pred)):
        if y_pred[i]:
            aspects_word.append(W_test[i])

    list_pair_1 = extract_collocation.pair_from_dict_new(W_test, y_pred)
    list_pair_2 = extract_collocation.pair_from_dict_chet(W_test, y_pred)
    #list_pair_3 = extract_collocation.pair_from_tomita(W_test, y_pred)

    pair = []

    list1 = [(i[0], i[1]) for i in list_pair_1]
    list2 = [(i[0], i[1]) for i in list_pair_2]
    #list3 = [(i[0], i[1]) for i in list_pair_3]

    w2v = load_gensim()

    pair = list1 + list2
    pair = Counter(pair)

    last_pair = []
    last_count = []
    last_number = []
    for key, value in pair.most_common(15):
        last_pair.append(key)
        last_count.append(value)

    k =0
    for key in last_pair:
        if key[0] in aspects_word:
            k = 1
        if key[1] in aspects_word:
            k = 2
        last_number.append(k)

    sent = []
    for i in range(len(last_pair)):
        n = sentiment.sentiment_svm(last_pair[i], last_number[i], w2v)
        sent.append(n)

    cloud.visualize(last_pair, last_count, sent)


if __name__ == '__main__':
    # print('dasha')
    my_name()
    exit(0)
    W_test, y_pred, z, c, y_test = extract_aspect.evaluate_task1()

    aspects_word = []
    for i in range(len(y_pred)):
        if y_test[i]:
            aspects_word.append(W_test[i])

    list_pair_1 = extract_collocation.pair_from_dict_new(W_test, y_pred)
    list_pair_2 = extract_collocation.pair_from_dict_chet(W_test, y_pred)
    list_pair_3 = extract_collocation.pair_from_tomita(W_test, y_pred)

    pair = []

    list1 = [(i[0], i[1]) for i in list_pair_1]
    list2 = [(i[0], i[1]) for i in list_pair_2]
    list3 = [(i[0], i[1]) for i in list_pair_3]

    word_norm, words, ys, _ = parse_dict()

    w2v = load_gensim()

    # определяем category
    my_c = sentiment.get_category(aspects_word, w2v)
    print classification_report(c, my_c)
    # for i in range(len(aspects_word)):
    #     if my_c[i] == 3 or c[i] == 3:
    #         print(aspects_word[i])
    #         print(my_c[i], c[i])
    #         print(" ")


    #определяем тональности
    sentiment.count_sentiment(W_test, list_pair_1, list1, w2v, z, word_norm,ys)



    pair = list1 + list2 + list3
    pair = Counter(pair)

    # for w, num in pair.most_common(20):
    #     print w[0], w[1], num


    last_pair = []
    last_count = []
    last_number = []
    for key, value in pair.most_common(15):
        last_pair.append(key)
        last_count.append(value)

    k =0
    for key in last_pair:
        if key[0] in aspects_word:
            k = 1
        if key[1] in aspects_word:
            k = 2
        last_number.append(k)

    sent = []
    for i in range(len(last_pair)):
        n = sentiment.sentiment_svm(last_pair[i], last_number[i], w2v)
        sent.append(n)

    cloud.visualize(last_pair, last_count, sent)
