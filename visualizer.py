__author__ = 'air'

from pywordcloud import pywordcloud

FONT_SIZE = 1


class Sentiment(object):
    def __init__(self, phrase, weight):
        self.phrase = phrase
        self.weight = weight

        self.color = 'green' if self.weight > 0 else 'red'

    def get_html(self, f, id):
        print >>f, "#tag%s:hover{color:black}" % id
        print >>f, "#tag%s{font-size: %sem; color: %s}" % (id, abs(self.weight) * FONT_SIZE, self.color)

    def get_html2(self, f, id):
        print >>f, '<a href=#><span class="word%s" id="tag%s">&nbsp;%s&nbsp;</span></a>' % (id, id, self.phrase.encode('utf-8'))


def visualize(sent_list, file_name):
    with open(file_name, 'w') as f:
        print >>f, """<html>
 <head>
  <meta charset="utf-8">
 </head>
 <style type="text/css">
 #box{font-family:'calibri';width:1000px;height:400px}
 #box a{text-decoration : none}"""
        for i, s in enumerate(sent_list):
            s.get_html(f, i)
        print >> f, """</style>
 <div id='box'>"""
        for i, s in enumerate(sent_list):
            s.get_html2(f, i)
        print >> f, """</div></html>"""


if __name__ == '__main__':
    visualize([Sentiment('hello dasha', 2), Sentiment('goodbye dasha', -1)], 'dasha.html')


if __name__ == '__main2__':
    text = open('hotels.txt').read()
    # print text.split('\n')[0]
    pywordcloud.create(
        text,
        outfile="output.html",
        uppercase=False,
        showfreq=False,
        frequency=50,
        removepunct=False,
        minfont=1.5,
        maxfont=6,
        hovercolor="green",
        showborder=False,
        fontfamily='calibri',
        width="1000px",
        height="400px",
        colorlist = ["red", "blue", "yellow", "green"]
    )
    result = open('output.html').read()
    with open('output.html', 'w') as f:
        print >>f, """<html>
 <head>
  <meta charset="utf-8">
 </head>"""
        print >>f, result
        print >>f, "</html>"
