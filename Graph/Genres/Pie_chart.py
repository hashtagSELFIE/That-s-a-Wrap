"""Project"""

import pygal
import pandas as pd
from ast import literal_eval

def open(dir_name):
    """openfile,last_data"""
    movie_type = {}
    filedata = pd.read_csv('completed_movie_database_for_PSIT.csv')
    top1 = filedata.loc[filedata['director'] == dir_name, ["genres"]]
    for i in range(len(top1.index)):
        for j in literal_eval(top1.iloc[i]['genres']):
            if j['name'] in movie_type:
                movie_type[j["name"]] += 1
            else:
                movie_type[j['name']] = 1
    print("Data Success!!")
    return movie_type


    # filedata.close()

def picture(subject):
    """Picture Pie"""
    newdict = open(subject)
    pie_chart = pygal.Pie()
    pie_chart.title = subject+"'s movie genres."
    lis = sorted(newdict.items(), key=lambda x: x[1], reverse=True)
    for i in lis:
        pie_chart.add(i[0], i[1])
    pie_chart.render_to_file('%s.svg' % subject)
    print("Done!!")

picture(input())
