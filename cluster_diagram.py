from traceback import print_tb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def column_switch(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df

with open("NGC2808_catalog.txt", 'r') as cata:
    col_names = cata.readlines()[13:50]
    for i in range(len(col_names)):
        col_names[i] = col_names [i] [11:len(col_names[i]) - 1]
    #print(col_names)

catalog = pd.read_table("NGC2808_catalog.txt", header = None, names = col_names,  delim_whitespace = True,
                                               skipinitialspace = True, skiprows = 56)
catalog = column_switch(catalog, 'Identification no. of star', 'Iteration star was found in')

what_to_plot = catalog.query('`Membership Probability [-1.0: not available]` > 90')

position_x = 10000 - what_to_plot['Absc. of stellar position (ref. system (5000,5000))']
position_y = 10000 - what_to_plot['Ord. of stellar position (ref. system (5000,5000))']
what_to_plot['F275W mag'][what_to_plot['F275W mag'] > 12] = 12
least_mag = what_to_plot['F275W mag'].min()
greatest_mag = what_to_plot['F275W mag'].max()
norm = mpl.colors.Normalize(vmin = least_mag, vmax = greatest_mag)
#size = catalog['F275W mag'].dropna().apply(lambda mag: [12 - s if s <= 12 else 0 for s in mag])

cluster = plt.subplot()
cluster.scatter(position_x, position_y, s = norm(12 - what_to_plot['F275W mag'])*0.1, color = 'white')
cluster.set_title("NGC-2808 Cluster")
space = plt.gca()
space.set_facecolor('black')
plt.show()