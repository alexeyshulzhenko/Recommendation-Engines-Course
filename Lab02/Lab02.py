# -*- coding: utf-8 -*-

#You may also check it out on my github (https://github.com/alexeyshulzhenko/Recommendation-Engines-Course)
# to ensure, that this lab was done by me
from datetime import datetime, timedelta
import csv
from math import log



def main():
    with open('HW.csv', 'rt', encoding='utf8') as csvfile:
        films = list(csv.reader(csvfile, delimiter=','))


if __name__ == '__main__':
    main()
