# coding: utf-8
__author__ = 'air'

# import selenium.webdriver as driver
# import random
# import logging
# import time
#
# logging.basicConfig(format='%(asctime)-15s %(message)s',level=logging.INFO)
#
# browser = driver.PhantomJS()
#
# random.seed = 13
CYR_SMALL = set(u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def parse(review):
    review = review.lower()
    new_review = ''

    for c in review:
        if c in CYR_SMALL or c == ' ' or c == '\t':
            new_review += c

    new_review = ' '.join(new_review.split())
    return new_review

#
# def main():
#     out_file = open('hotels.txt', 'a')
#     N = 30000
#
#     timeout = 2
#
#     for i in range(N):
#         if i % 100 == 0:
#             logging.info('Parsed: %s/%s' % (i, N))
#
#         rand_id = random.randint(1000, 1200000)
#         browser.get('http://www.tophotels.ru/main/viewrate/?id=%s' % rand_id)
#
#         try:
#             review = browser.find_element_by_class_name('hotel-review-text').text
#             review = ' '.join(review.split('\n'))
#             review = parse(review)
#             print >>out_file, parse(review).encode('utf-8')
#             out_file.flush()
#             timeout = 2
#         except Exception as ex:
#             time.sleep(timeout)
#             timeout *= 2
#             logging.error('http://www.tophotels.ru/main/viewrate/?id=%s' % rand_id)
#             logging.error(ex)
#             continue
#
#     out_file.close()


def load_mark_word():
    mark_word = set()
    with open('mark_word.txt', 'r') as f:
        for i in f:
            word, val = i.split()
            mark_word.add(word.decode('utf-8').lower())
    return mark_word


if __name__ == '__main__':
    main()