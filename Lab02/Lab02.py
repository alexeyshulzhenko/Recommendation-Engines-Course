# -*- coding: utf-8 -*-

#You may also check it out on my github (https://github.com/alexeyshulzhenko/Recommendation-Engines-Course)
# to ensure, that this lab was done by me
from datetime import datetime, timedelta
import csv
import itertools, operator
import pandas as pd

raitings_list = []
movie_list = []

def main():
    with open("data/movies.csv", "rt", encoding="utf8") as csvfile:
        movies = list(csv.reader(csvfile, delimiter=","))
    with open("data/ratings.csv", "rt", encoding="utf8") as csvfile:
        ratings = list(csv.reader(csvfile, delimiter=","))
    with open("data/links.csv", "rt", encoding="utf8") as csvfile:
        links = list(csv.reader(csvfile, delimiter=","))
    with open("data/tags.csv", "rt", encoding="utf8") as csvfile:
        tags = list(csv.reader(csvfile, delimiter=","))


    for element in ratings[1:]:
        raitings_list.append([element[1], float(element[2])])

    for element in movies[1:]:
        movie_list.append([element[1], element[2]])

    df_movies = pd.DataFrame(movie_list, columns=["filmid", "tittle"], dtype=float).set_index("filmid")
    #borrowed idea here: https://stackoverflow.com/questions/44503016/how-to-use-python-list-to-group-elements-and-average-the-group-numbers

    df = pd.DataFrame(raitings_list, columns=["filmid", "raiting"], dtype=float).set_index("filmid")
    average_raiting = df.groupby(df.index).mean().reset_index()

    # Calculating damped mean using k = 5

    df = pd.DataFrame(raitings_list, columns=["filmid", "raiting_s"], dtype=float).set_index("filmid")
    sum_raiting = df.groupby(df.index).sum().reset_index()

    df = pd.DataFrame(raitings_list, columns=["filmid", "raiting_c"], dtype=float).set_index("filmid")
    count_raiting = df.groupby(df.index).count().reset_index()

    sum_raiting["sum_rating_factor"] = sum_raiting["raiting_s"]+5*(df["raiting_c"].mean())

    count_raiting["count_rating_factor"] = count_raiting["raiting_c"]+5

    # print (count_raiting)
    # print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # print (sum_raiting)
    raitings_damped = pd.merge(sum_raiting,count_raiting[["filmid","raiting_c","count_rating_factor"]],on=["filmid"],how="left")

    raitings_damped["damped_mean"]=raitings_damped["sum_rating_factor"] / raitings_damped["count_rating_factor"]

    ratings_mean_dampmean=pd.merge(average_raiting[["filmid","raiting"]],raitings_damped[["filmid","damped_mean"]],on=["filmid"],how="left")

    print(ratings_mean_dampmean)
    print("############################################")




    ratings_mean_dampmean = ratings_mean_dampmean.sort_values(["raiting"], ascending=False).reset_index()

    ratings_mean_dampmean = ratings_mean_dampmean.reindex(columns=['filmid','raiting','damped_mean']).set_index("filmid")


    print(ratings_mean_dampmean[["raiting"]])
    films_sorted = pd.join(df_movies[["tittle"]],ratings_mean_dampmean[["raiting"]])
    print (films_sorted)


if __name__ == "__main__":
    main()

