# -*- coding: utf-8 -*-

import datetime
import csv
from math import log

# Addind service DATETIME Vars

now = datetime.datetime.now()
epoch = datetime(1970, 1, 1)
tittle = []
date = []
upVotes = []
downVotes = []
rank = []

def main():
    with open('HW.csv', 'rt', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            tittle.append(row[0])
            date.append(epoch_seconds(row[1]))
            upVotes.append(row[2])
            downVotes.append(row[3])




if __name__ == '__main__':
    main()




#We
def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def score(ups, downs):
    return ups - downs

def hot(ups, downs, date):
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)

print(hot(10, 100, datetime(2000, 1, 1)))
print(hot(10, 1000, datetime(2000, 1, 1)))
