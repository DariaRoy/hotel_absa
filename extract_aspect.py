# coding: utf-8
__author__ = 'air'

import parsing
import pickle
from train_gensim import load_gensim
import os.path as os_path
from sklearn.metrics import classification_report
from download import load_mark_word

def evaluate_task_new(W_test):

    train, _ = parsing.load_train_test()

    # достаем слова и метки слов
    W_train, y_train, _, _ = parsing.prepare_task1(train)

    w2v = load_gensim()
    # подсчитываем w2v расстояния либо загружаем из файла
    if os_path.exists('distances_train.bin'):
        with open('distances_train.bin') as f:
            X_train = pickle.load(f)
        with open('distances_test.bin') as f:
            X_test = pickle.load(f)
    else:
        # если они не предпосчитаны, то считаем и сохраняем

        X_train = [0 for _ in xrange(len(W_train))]
        X_test = [0 for _ in xrange(len(W_test))]

        for aspect_id in xrange(len(W_train)):
            if aspect_id % 100 == 0:
                print '%s/%s' % (aspect_id, len(W_train))

            if y_train[aspect_id] != 1:
                continue

            for word_id in xrange(len(W_train)):
                try:
                    # X_train[word_id] += w2v.similarity(W_train[aspect_id].encode('utf-8'),
                    #                                   W_train[word_id].encode('utf-8'))
                    X_train[word_id] = max(X_train[word_id], w2v.similarity(W_train[aspect_id].encode('utf-8'),
                                                       W_test[word_id].encode('utf-8')))
                except:
                    pass

            for word_id in xrange(len(W_test)):
                try:
                    # X_test[word_id] += w2v.similarity(W_train[aspect_id].encode('utf-8'),
                    #                                   W_test[word_id].encode('utf-8'))
                    X_test[word_id] = max(X_test[word_id], w2v.similarity(W_train[aspect_id].encode('utf-8'),
                                                       W_test[word_id].encode('utf-8')))
                except:
                    pass

        # with open('distances_train.bin', 'w') as f:
        #     pickle.dump(X_train, f)
        # with open('distances_test.bin', 'w') as f:
        #     pickle.dump(X_test, f)

    threshold = 0.75
    y_pred = [1 if x >= threshold else 0 for x in X_test]

    print(w2v.similarity('отеля', 'цена'))
    return y_pred

def evaluate_task1():
    """
    Выполнение задачи 1 и подсчет метрик
    :return: W_test - аспекты тестовой выборки,
     y_pred - метки для выборки,
     z - тональности,
     c - категории,
     y_test -реальные метки аспектов
    """
    train, test = parsing.load_train_test()

    # достаем слова и метки слов
    W_train, y_train, _, _ = parsing.prepare_task1(train)
    W_test, y_test, z, c = parsing.prepare_task1(test)

    w2v = load_gensim()
    # подсчитываем w2v расстояния либо загружаем из файла
    if os_path.exists('distances_train.bin'):
        with open('distances_train.bin') as f:
            X_train = pickle.load(f)
        with open('distances_test.bin') as f:
            X_test = pickle.load(f)
    else:
        # если они не предпосчитаны, то считаем и сохраняем

        X_train = [0 for _ in xrange(len(W_train))]
        X_test = [0 for _ in xrange(len(W_test))]

        for aspect_id in xrange(len(W_train)):
            if aspect_id % 100 == 0:
                print '%s/%s' % (aspect_id, len(W_train))

            if y_train[aspect_id] != 1:
                continue

            for word_id in xrange(len(W_train)):
                try:
                    # X_train[word_id] += w2v.similarity(W_train[aspect_id].encode('utf-8'),
                    #                                   W_train[word_id].encode('utf-8'))
                    X_train[word_id] = max(X_train[word_id], w2v.similarity(W_train[aspect_id].encode('utf-8'),
                                                       W_test[word_id].encode('utf-8')))
                except:
                    pass

            for word_id in xrange(len(W_test)):
                try:
                    # X_test[word_id] += w2v.similarity(W_train[aspect_id].encode('utf-8'),
                    #                                   W_test[word_id].encode('utf-8'))
                    X_test[word_id] = max(X_test[word_id], w2v.similarity(W_train[aspect_id].encode('utf-8'),
                                                       W_test[word_id].encode('utf-8')))
                except:
                    pass

        with open('distances_train.bin', 'w') as f:
            pickle.dump(X_train, f)
        with open('distances_test.bin', 'w') as f:
            pickle.dump(X_test, f)

    threshold = 0.75
    y_pred = [1 if x >= threshold else 0 for x in X_test]

    print(w2v.similarity('и', 'но'))
    print('извлечение')
    print classification_report(y_test, y_pred)
    return W_test, y_pred, z, c, y_test


def evaluate_task1_rules():
    """
    Выполнение задачи 1 и подсчет метрик для правил
    :return: None
    """
    train, test = parsing.load_train_test()

    # достаем слова и метки слов
    W_train, y_train, _, _ = parsing.prepare_task1(train)
    W_test, y_test, z, c = parsing.prepare_task1(test)

    mark_words = load_mark_word()
    y_pred = [0 for _ in xrange(len(W_test))]
    for i in xrange(0, len(W_test) - 1):
        if W_test[i] in mark_words:
            y_pred[i + 1] = 1
            y_pred[i - 1] = 1
            y_pred[i] = 0
        else:
            y_pred[i + 1] = 0

    print classification_report(y_test, y_pred)