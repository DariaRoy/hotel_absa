# coding: utf-8
__author__ = 'air'

import pair_pmi
from download import load_mark_word
from parse_dict import parse_dict

def pair_from_dict_chet(W_test, y_pred):
    mark_word = load_mark_word()
    k = 0
    pair = []

    for i in range(len(W_test)):
        if y_pred[i]:
            if i > 0:
                if W_test[i-1] in mark_word:
                    lis = []
                    lis.append(W_test[i-1])
                    lis.append(W_test[i])
                    lis.append(2)
                    pair.append(lis)
                    k += 1
            if i < len(W_test) - 1:
                if W_test[i+1] in mark_word:
                    lis = []
                    lis.append(W_test[i])
                    lis.append(W_test[i+1])
                    lis.append(1)
                    pair.append(lis)
                    k += 1
    return pair

def pair_from_dict_new(W_test, y_pred):
    mark_word, _, _ ,_= parse_dict()
    k = 0
    pair = []

    for i in range(len(W_test)):
        if y_pred[i]:
            if i > 0:
                if W_test[i-1] in mark_word:
                    lis = []
                    lis.append(W_test[i-1])
                    lis.append(W_test[i])
                    lis.append(2)
                    pair.append(lis)
                    k += 1
            if i < len(W_test) - 1:
                if W_test[i+1] in mark_word:
                    lis = []
                    lis.append(W_test[i])
                    lis.append(W_test[i+1])
                    lis.append(1)
                    pair.append(lis)
                    k += 1
    return pair

def pair_from_tomita(W_test, y_pred):
    pair = pair_pmi.pair_mi()
    ok_pair = []
    #print ' '.join(W_test)
    for i in range(min(50,len(pair))):
        k1 = W_test.index(pair[i][0])
        k2 = W_test.index(pair[i][1])
        lis = []
        lis.append(pair[i][0])
        lis.append(pair[i][1])
        if y_pred[k1]:
            lis.append(1)
            ok_pair.append(lis)
        if y_pred[k2]:
            lis.append(2)
            ok_pair.append(lis)
    return ok_pair
