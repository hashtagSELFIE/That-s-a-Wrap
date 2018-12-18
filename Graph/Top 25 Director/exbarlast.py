"""Project"""

import pygal
import pandas as pd
from pygal.style import DarkStyle

def main():
    """Create graph"""
    movie_type = {}
    test = pd.read_csv('completed_movie_database_for_PSIT.csv')
    sample = {}
    already = []
    for x in range(len(test.index)):
        name = test.iloc[x]['director']
        networth = test.iloc[x]['revenue']
        if name not in already:
            sample[name] = networth
        else:
            sample[name] += networth
        print(sample.get(name))
    print("yay")
    sorted_d = sorted(sample.items(), key=lambda x: x[1], reverse=True)
    bar_chart = pygal.HorizontalBar(x_label_rotation=30, style=DarkStyle)
    bar_chart.title = "Top 25 director by revenue in all movies"
    counter = 0
    for a, b in sorted_d:
        if counter > 25:
            break
        bar_chart.add(a, b)
        counter += 1
    bar_chart.render_to_file('chart.svg')
    print("done")

main()
