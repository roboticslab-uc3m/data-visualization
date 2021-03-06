#!/usr/bin/python
import matplotlib.pyplot as plt 

#import matplotlib

#matplotlib.rcParams['ps.useafm'] = True
#matplotlib.rcParams['pdf.use14corefonts'] = True
#matplotlib.rcParams['text.usetex'] = True

font = {'family' : 'Helvetica',
        'size'   : 36}

plt.rc('font', **font)


plt.plotfile('example-percentage-painted-ideal.txt', delimiter=' ', cols=(0, 1),
                     names=('Time interval', 'Wall Painted (%)'), marker='s', label='Ideal', linewidth=7.0)

plt.plotfile('example-percentage-painted-demons.txt', delimiter=' ', cols=(0, 1), newfig=False, 
                     names=('Time interval', 'Wall Painted (%)'), marker='x', label='Demonstrations', linewidth=2.0)

#plt.plotfile('IET-Paint-Percentage.txt', delimiter=' ', cols=(0, 1), newfig=False,
#                     names=('Time interval', 'Wall Painted (%)'), marker='o', label='IET', linewidth=2.0)

#plt.plotfile('OET-Paint-Percentage.txt', delimiter=' ', cols=(0, 1), newfig=False,
#                     names=('Time interval', 'Wall Painted (%)'), marker='^', label='OET', linewidth=2.0)

plt.legend(loc=2)

plt.savefig('Gen-paint.pdf')

plt.show()
