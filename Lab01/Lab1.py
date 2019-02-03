# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import csv
from math import log

# Addind service DATETIME Vars
now = datetime.now()
epoch = datetime(1970, 1, 1)

tittle = []
date = []
score_index = []
rank = []
sorted_news = []


# We translate timestamp to epoch seconds
def epoch_seconds(date):
    td = datetime.strptime(date, '%m/%d/%y %H:%M') - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


# We calculate score, based on upvotes and downvotes
def score(ups, downs):
    return int(ups) - int(downs)


def hot(ups, downs, date):
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)


def main():
    with open('HW.csv', 'rt', encoding='utf8') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=','))
        for element in spamreader[1:]:
            sorted_news.append([element[0], hot(element[2], element[3],element[1])])
            tittle.append(element[0])
            date.append(epoch_seconds(element[1]))
            score_index.append(score(element[2], element[3]))
            rank.append(hot(element[2], element[3], element[1]))
    # print (sorted_news)
    for row in sorted(sorted_news, key=lambda x: x[1], reverse=True):
        print(row[0])

if __name__ == '__main__':
    main()
