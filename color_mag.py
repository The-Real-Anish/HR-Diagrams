from traceback import print_tb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Luminosity of the Sun in Watts(W)
sum_lum = 3.84*10e23

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

accurate_catalog = catalog.query('`F275W mag` > -99.99 and `F336W mag` > -99.99 and `Membership Probability [-1.0: not available]` > 90')
accurate_mag = accurate_catalog['F275W mag']
accurate_mag_diff = accurate_catalog['F275W mag'] - accurate_catalog['F336W mag']
#F275_mag = catalog['F275W mag']
#F336_mag = catalog['F336W mag']
#F275_mag = F275_mag[F275_mag > -99.99]
#F336_mag = F336_mag[F336_mag > -99.99]
#mag_diff = F275_mag - F336_mag
#for star in F275_mag:
#    mag_diff
#print(accurate_catalog)
#print(accurate_mag)
#print(accurate_mag_diff)
#print(catalog['F275W mag'])
#print(catalog['F336W mag'])
#print(mag_diff)
CMD = plt.subplot()
CMD.scatter(accurate_mag_diff, accurate_mag, s = 0.01, color = 'white', label = 'CMD')
CMD.invert_yaxis()

background = plt.gca()
background.set_facecolor('black')
CMD.set_aspect(1.0/CMD.get_data_ratio(), adjustable='box')
CMD.set_title("Color-Mag Diagram, NGC-2808")
plt.show()
#magnitudes = avg