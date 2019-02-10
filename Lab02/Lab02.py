# -*- coding: utf-8 -*-

#You may also check it out on my github (https://github.com/alexeyshulzhenko/Recommendation-Engines-Course)
# to ensure, that this lab was done by me
from datetime import datetime, timedelta
import csv
import itertools, operator
import pandas as pd

raitings_list = []


def main():
    with open('data/movies.csv', 'rt', encoding='utf8') as csvfile:
        movies = list(csv.reader(csvfile, delimiter=','))
    with open('data/ratings.csv', 'rt', encoding='utf8') as csvfile:
        ratings = list(csv.reader(csvfile, delimiter=','))
    with open('data/links.csv', 'rt', encoding='utf8') as csvfile:
        links = list(csv.reader(csvfile, delimiter=','))
    with open('data/tags.csv', 'rt', encoding='utf8') as csvfile:
        tags = list(csv.reader(csvfile, delimiter=','))


    for element in ratings[1:]:
        raitings_list.append([element[1], float(element[2])])

    #borrowed idea here: https://stackoverflow.com/questions/44503016/how-to-use-python-list-to-group-elements-and-average-the-group-numbers

    df = pd.DataFrame(raitings_list, columns=["filmid", "raiting"], dtype=float).set_index("filmid")
    average_raiting = df.groupby(df.index).mean()

    # Calculating damped mean using k = 5


    sum_raiting = df.groupby(df.index).sum()
    count_raiting = df.groupby(df.index).count()

    sum_raiting['sum_rating_factor'] = sum_raiting["raiting"]+5*(df["raiting"].mean())

    count_raiting['count_rating_factor'] = count_raiting['raiting']+5
    print(count_raiting)

if __name__ == '__main__':
    main()

#
# Ratings_mean=Ratings.groupby([‘movieId’])[[‘rating’]].mean().rename(columns = {‘rating’: ‘Mean_rating’}).reset_index()
# # Calculating damped mean using alpha = 5
# ###############Ratings_sum=Ratings.groupby([‘movieId’])[[‘rating’]].sum().rename(columns = {‘rating’: ‘sum_rating’}).reset_index()
# Ratings_sum[‘sum_rating_factor’]=Ratings_sum[‘sum_rating’]+5*(Ratings[“rating”].mean())
# ###############Ratings_count=Ratings.groupby([‘movieId’])[[‘rating’]].count().rename(columns = {‘rating’: ‘count_rating’}).reset_index()
# ###############Ratings_count[‘count_rating_factor’]=Ratings_count[‘count_rating’]+5
# Ratings_damped=pd.merge(Ratings_sum,Ratings_count[[‘movieId’,’count_rating’,’count_rating_factor’]],on=[‘movieId’],how=’left’)
# Ratings_damped[‘damped_mean’]=Ratings_damped[‘sum_rating_factor’]/Ratings_damped[‘count_rating_factor’]
# Ratings_mean_dampmean=pd.merge(Ratings_mean[[‘movieId’,’Mean_rating’]],Ratings_damped[[‘movieId’,’damped_mean’]],on=[‘movieId’],how=’left’)
# # Sorting to get top rated movies
# Ratings_mean_dampmean = Ratings_mean_dampmean.sort([‘Mean_rating’], ascending=False)
