import numpy as np
from catalog2tess_px.catalogs.HyperLedaCsv import HyperLedaCsv

c1 = HyperLedaCsv('/Users/faus/python/catalog2tess_px/HyperLEDA/s01/hyperleda_s01_cam1.txt',
                 ignore_image_buffer=True)

c2 = HyperLedaCsv('/Users/faus/python/catalog2tess_px/HyperLEDA/s21/hyperleda_s21_cam1.txt',
                 ignore_image_buffer=True)


m1 = (np.isnan(c1.vmag)) |  (np.isnan(c1.modz))
print(len(c1.vmag[m1]))
print(np.c_[ c1.objname[~m1], c1.vmag[~m1], c1.moddist[~m1], c1.modz[~m1]])

m2 = (np.isnan(c2.vmag)) |  (np.isnan(c2.modz))
print(len(c2.vmag[m2]))


d1 = 10**(0.2*c1.modz[~m1])*10/1.e6
print(len(d1))
d2 = 10**(0.2*c2.modz[~m2])*10/1.e6
print(len(d2))

with open('Galaxy-Data.txt','w') as fout:
    fout.write('#{:29s}{:>15s}{:>15s}\n'.format('Object','Vmag','Distance_Mpc'))
    for ii in range(len(c1.vmag[~m1])):
        fout.write('{:30s}{:>15.4f}{:>15.4e}\n'.format(c1.objname[~m1][ii],
                                                     c1.vmag[~m1][ii],
                                                     d1[ii] ))
    for ii in range(len(c2.vmag[~m2])):
        fout.write('{:30s}{:>15.4f}{:>15.4e}\n'.format(c2.objname[~m2][ii],
                                                     c2.vmag[~m2][ii],
                                                     d2[ii] ))
