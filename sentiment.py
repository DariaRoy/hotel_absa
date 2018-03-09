# coding: utf-8
__author__ = 'air'

from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

from parse_dict import parse_dict

# good, bad - закачать из файла
good = ['хороший', 'чистый', 'просторный', 'удобный', 'замечательный']
bad = ['старый', 'грязный', 'плохой', 'хамский', 'ужасный']

def sentiment(pair, w2v):
    word1_good = -1
    word1_bad = -1
    word2_good = -1
    word2_bad = -1
    # вместо этого цикла - обучить KNN. train(good + bad)
    # после этого сделать
    for i in range(len(good)):
        try:
            word1_good = max(word1_good, w2v.similarity(pair[0].encode('utf-8'),  good[i]))
        except:
            pass

    for i in range(len(bad)):
        try:
            word1_bad = max(word1_bad, w2v.similarity(pair[0].encode('utf-8'),  bad[i]))
        except:
            pass

    for i in range(len(good)):
        try:
            word2_good = max(word2_good, w2v.similarity(pair[1].encode('utf-8'),  good[i]))
        except:
            pass

    for i in range(len(bad)):
        try:
            word2_bad = max(word2_bad, w2v.similarity(pair[1].encode('utf-8'),  bad[i]))
        except:
            pass

    mid_good = max(word1_good, word2_good)
    mid_bad = max(word1_bad, word2_bad)
    return 1 if mid_good > mid_bad else -1


def sentiment_rul(pair, k, word_norm, ys):
    if k-1 == 0:
        k = 1
    else:
        k = 0
    word = pair[k]
    if word in word_norm:
        k = word_norm.index(word)
        return ys[k]


def sentiment_svm(pair, k, w2v):
    if k-1 == 0:
        k = 1
    else:
        k = 0
    clf = create_classifier()
    word = pair[k].encode('utf-8')
    try:
        return clf.predict(w2v[word])
    except:
        return [1]

def create_classifier():
    _, words, mark, ys_1 = parse_dict()

    #clf = KNeighborsClassifier(n_neighbors=3)
    clf = LinearSVC(C=1.0)
    # clf = NuSVC(kernel='linear', probability=True, random_state=1)
    clf.fit(words, ys_1)
    return clf

def get_category(words, w2v):
    need = []
    for i in range(len(words)):
        try:
            #print(words[i])
            k = []
            k.append(w2v.similarity(words[i].encode('utf-8'), 'отель'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'номер'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'сервис'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'территория'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'питание'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'расположение'))
            k.append(w2v.similarity(words[i].encode('utf-8'), 'цена'))
            my_max = k.index(max(k))
            need.append(my_max)
            #print(words[i], my_max)
        except:
            print(words[i])
            need.append(4)
    return need


def count_sentiment(W_test, list_pair_1, list1, w2v, z, word_norm, ys):
    sent_1 = []
    aspects_1 = []
    aspects_1_id = []
    z_1 = []
    for i in range(len(list_pair_1)):
        #n = sentiment_svm(list1[i], list_pair_1[i][2], w2v)
        n = sentiment_rul(list1[i], list_pair_1[i][2],word_norm,ys)
        sent_1.append(n)
        aspects_1.append(list1[i][list_pair_1[i][2]-1])
        aspects_1_id.append(i)

    #print aspects_1
    for word in W_test:
        if word in aspects_1:
            k = aspects_1.index(word)
            aspects_1[k] = ''
            if (sent_1[k] == 1):
                z_1.append(1)
            else:
                z_1.append(-1)
        else:
            z_1.append(0)

    l_z = []
    l_z_1 = []
    for i in range(len(z)):
        if z_1[i] and z[i]:
            l_z.append(z[i])
            l_z_1.append(z_1[i])

    print('      sentiment      ')
    print classification_report(l_z, l_z_1)



if __name__ == '__main__':
    clf = create_classifier()
    from train_gensim import load_gensim
    w2v = load_gensim()
    # print w2v.
    print clf.predict([w2v['вкусный'], w2v['отель'], w2v['хороший']])
    # print clf.predict_proba([w2v['вкусный'], w2v['отель'], w2v['хороший']])
    # print clf.predict_proba([w2v['дети']])