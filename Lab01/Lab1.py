# -*- coding: utf-8 -*-

import datetime
import csv
from math import log

# Addind service DATETIME Vars
now = datetime.datetime.now()
epoch = datetime(1970, 1, 1)



tittle = []
date = []
score_index = []
rank = []


#We translate timestamp to epoch seconds
def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

#We calculate score, based on upvotes and downvotes
def score(ups, downs):
    return ups - downs

def hot(ups, downs, date):
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)


def main():
    with open('HW.csv', 'rt', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            tittle.append(row[0])
            date.append(epoch_seconds(row[1]))
            score_index.append(score(row[2], row[3]))
            rank.append(hot(row[2], row[3],row[1]))

    sorted = [x for _,x in sorted(zip(rank,tittle))]
    for row in sorted:
        print(row)

if __name__ == '__main__':
    main()




