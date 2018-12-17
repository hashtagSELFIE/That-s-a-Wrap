"""Project"""

import pygal
import pandas as pd
from ast import literal_eval

def open(dir_name):
    """openfile,last_data"""
    movie_type = {}
    filedata = pd.read_csv('completed_movie_database_for_PSIT.csv')
    top1 = filedata.loc[filedata['director'] == dir_name, ["title", "vote_average", "revenue"]]
    for i in range(len(top1.index)):
        currenttitle = top1.iloc[i]['title']
        if currenttitle in movie_type:
            movie_type[currenttitle] += top1.iloc[i]['vote_average']
        else:
            movie_type[currenttitle] = top1.iloc[i]['vote_average']
    print("Data Success!!")
    return movie_type


    # filedata.close()

def picture(subject):
    """Picture Pie"""
    newdict = open(subject)
    bar_chart = pygal.Bar()
    bar_chart.title = subject+"'s movies ratings."
	dictlist = []
	for key, value in newdict.iteritems():
        temp = [key,value]
        dictlist.append(temp)
    for i in newdict:
        bar_chart.add(i[0], i[1])
    bar_chart.render_to_file('%s_bar.svg' % subject)
    print("Done!!")

picture(input())
