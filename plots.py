# coding: utf-8
__author__ = 'air'

from pylab import *

threshold = [0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1.0]
precision = [0.12, 0.14, 0.17, 0.22, 0.33, 0.45, 0.65, 0.78, 0.83, 0.84]
recall =    [0.99, 0.99, 0.99, 0.99, 0.94, 0.86, 0.79, 0.68, 0.65, 0.57]
f1score =   [0.21, 0.24, 0.29, 0.36, 0.49, 0.59, 0.71, 0.73, 0.73, 0.68]
# figure()
# plot(threshold,precision, 'r',  threshold,recall, 'b', threshold,f1score, 'g')
# xlabel('threshold')
# legend ((u'precision', u'recall', u'f1-score'), loc=4)
# show()



# threshold = [0,    5,    10,   15,   20,   25,   30,   35,   40,   45]
# precision = [0.17, 0.22, 0.25, 0.30, 0.36, 0.44, 0.46, 0.62, 0.49, 0.50]
# recall =    [0.97, 0.93, 0.83, 0.75, 0.65, 0.55, 0.33, 0.28, 0.05, 0.00]
# f1score =   [0.29, 0.36, 0.39, 0.43, 0.47, 0.49, 0.39, 0.39, 0.09, 0.01]
# figure()
plot(threshold,precision, 'r--',  threshold,recall, 'b', threshold,f1score, 'g-.')
xlabel('threshold')
legend ((u'precision', u'recall', u'f1-score'))
show()