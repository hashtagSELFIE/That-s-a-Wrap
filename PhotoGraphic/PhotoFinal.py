"""project"""

import pygal

def calculate():
	"""picture Donut"""



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

picture()
