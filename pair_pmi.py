__author__ = 'air'
# coding: utf-8
import re
import collections
import numpy as np

def splitter(text):
    exp = re.compile(r',|\.|!|:|\?| |\(|\)|<|>|"|&|\n|\t', re.IGNORECASE)
    return [word for word in re.split(exp, text) if len(word) > 0]

def pair_mi():
    # /Users/air/PycharmProjects/hotels/out.txt
    # ../../Downloads/book_tomita.txt
    with open('/Users/air/PycharmProjects/hotels/out.txt') as f:
        words = splitter(f.read().decode('utf-8').lower())
        #words = [word for word in words if len(word)>2]

    #print ' '.join([i.encode('utf-8') for i in words])

    # counter for words from text
    cnt_words = collections.Counter()
    for w in words:
        cnt_words[w] += 1

    # read phrases
    with open('/Users/air/Downloads/dasha_tomita/pairs.txt') as f:
        text = f.read().decode('utf-8').lower().split('\n')
        phrases = []
        for i in xrange(0, len(text) - 1, 2):
            # print text[i]
            phrases.append((text[i].split(' ')[-1], text[i + 1].split(' ')[-1]))
    # print phrases
    # count phrases
    cnt = collections.Counter()
    for p in phrases:
        cnt[p] += 1

    # print top25 phrases for occurency
    # print('Number of occurencies')
    # for w, num in cnt.most_common(20):
    #     print w[0], w[1], num

    # count mutual information
    mi = []
    for p in list(set(phrases)):
        try:
            cur_mi = np.log(len(words) * cnt[p] * 1.0 / cnt_words[p[0]] / cnt_words[p[1]])
        except:
            continue
        mi.append((cur_mi, p[0], p[1]))


    mi = sorted(mi, key=lambda x: x[0], reverse=True)
    return [i[1:] for i in mi]



if __name__ == '__main__':
    main()
