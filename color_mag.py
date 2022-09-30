from traceback import print_tb
import numpy as np
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

#print(catalog.query('`F275W photometric RMS` < 99').sort_values(['F275W photometric RMS']))
mag_diff = catalog['F275W mag'] - catalog['F336W mag']
#print(catalog['F275W mag'])
#print(catalog['F336W mag'])
#print(mag_diff)
CMD = plt.subplot()
CMD.scatter(mag_diff, catalog['F275W mag'], s = 1, color = 'black', label = 'CMD')
CMD.invert_yaxis()
CMD.set_aspect(1.0/CMD.get_data_ratio(), adjustable='box')
CMD.set_title("Color-Mag Diagram, NGC2808")
plt.show()
#magnitudes = avg