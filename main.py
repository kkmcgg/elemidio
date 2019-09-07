import mido

baseURL = "http://skuld.bmsc.washington.edu/scatter/data/"
suffix = '.dat'

ELEMENT = 'K'
col=1

URL = baseURL+ELEMENT+suffix

print(URL)

import urllib2
response = urllib2.urlopen(URL)
#data = response.read().strip()#.split(' ')

import numpy as np
#from io import StringIO   
data = response.read()
data=data.split()
data=np.array(data, dtype=float)
data = data.reshape(data.size/3,3).T
a=data[col]
a-=a.min()
a/=a.max()
a*=2
a-=1

#mirror array
b = np.zeros((a.size*2))
b[0:a.size]=a
b[a.size:]=a[::-1]
a=b

print a
from matplotlib import pyplot as plt 

plt.plot(a)
plt.axis('off')
plt.show()

import scipy.io.wavfile as wv
outFile = ELEMENT+str(col)+'.wav'

duration = 5.0
sps = 44100
approxLength = sps*duration
length = int(approxLength/a.size)*a.size

outData = np.zeros((length))
for i in range (0,length,a.size):
    outData[i:i+a.size]=a
wv.write(outFile, 44100, outData)