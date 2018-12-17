"""project"""

import pygal
import pandas as pd
from ast import literal_eval

def open():
	"""openfile,last_data"""
	movie_type = {}
	filedata = pd.DataFrame(r '\Users\Mickey\Documents\completed_movie_database_for_PSIT.csv')
	top1 = filedata.loc[filedata['director'] == 'James Cameron', ["genres"]]
	for i in range(len(top1.index)):
		for j in literal_eval(top1.iloc[i]['genres']):
			if j['name'] in movie_type:
				movie_type['name'] += 1
			else:
				movie_type['name'] = 1
	return(movie_type)


	# filedata.close()

def calculate():
	"""calculate Donut"""
	name = input()
	

def picture():
	"""picture Donut"""
	pie_chart = pygal.Pie()
	pie_chart.title = 'Director (in %)'
	pie_chart.add('Action', 19.5)
	pie_chart.add('Adventure', 36.6)
	pie_chart.add('War', 36.3)
	pie_chart.add('Drama', 4.5)
	pie_chart.add('Science', 2.3)
	pie_chart.add('Family', 2.3)
	pie_chart.add('Thriller', 2.3)
	pie_chart.add('Crime', 2.3)
	pie_chart.add('Documentaries', 2.3)
	pie_chart.add('Animation ', 2.3)
	pie_chart.add('Comedy ', 36.6)
	pie_chart.add('Erotic', 36.3)
	pie_chart.add('Fantasy', 4.5)
	pie_chart.add('Musicals', 2.3)
	pie_chart.add('Romance ', 2.3)
	pie_chart.add('Western ', 2.3)
	pie_chart.render_to_file('pie-chart.svg')

# picture()
print(open())