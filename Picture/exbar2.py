"""Project"""

import pygal
import pandas as pd
from ast import literal_eval

def open(dir_name):
    """openfile,last_data"""
    movie_type = {}
    filedata = pd.read_csv('completed_movie_database_for_PSIT.csv')
    top1 = filedata.loc[filedata['director'] == dir_name, ["vote_average", "revenue"]]
    for i in range(len(top1.index)):
        currenttitle = top1.iloc[i]['title']
        for j in top1.iloc[i]['vote_average']:
            if currenttitle in movie_type:
                movie_type[currenttitle] += j
            else:
                movie_type[currenttitle] = j
    print("Data Success!!")
    return movie_type


    # filedata.close()

def picture(subject):
    """Picture Pie"""
    newdict = open(subject)
    pie_chart = pygal.Bar()
    pie_chart.title = subject+"'s movie genres."
    lis = sorted(newdict.items(), key=lambda x: x[1], reverse=True)
    for i in lis:
        pie_chart.add(i[0], i[1])
    pie_chart.render_to_file('%s.svg' % subject)
    print("Done!!")

picture(input())
