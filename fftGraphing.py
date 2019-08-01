# This program graphs the weights, A[f] and B[f], 
# for E(t) and I(t), respectively, where
# E(t) = Edc(t) + sum{f=1}A[f]sin(2pift+phi), and 
# I(t) = Idc(t) + sum{f=1}B[f]sin(2pift+phi).

import sys
from numpy import loadtxt,empty,arctan,sin,cos
import matplotlib.pyplot as plt

# Extracts the data from the input file
name = input('FFT filename prefix: ')
filename = str(name) + '.txt'
data = loadtxt(filename,skiprows=2)
freq = data[:,0]
E_real = data[:,1]
E_imag = data[:,2]
I_real = data[:,3]
I_imag = data[:,4]

# Creates an array to store the values of the weights
A = empty([len(freq),1],float)
B = empty([len(freq),1],float)

# The 'frequency' of 0 is just the sum of every point - we don't care about that here
# So I set the value of these weights to 0
A[0]=0
B[0]=0

# Finds the phase angles (phi) and calculates the weights for each frequency
for i in range(1,len(freq)-1):
	Iphi = arctan(I_real[i]/I_imag[i])
	B[i] = abs(I_imag[i]/cos(Iphi))  # could have equivalently used abs(I_real[i]/sin(phi))
	Ephi = arctan(E_real[i]/E_imag[i]) 
	A[i] = abs(E_imag[i]/cos(Ephi))
	
# Plots the weights for the potential vs frequency
plt.plot(freq,A,'r-',label=("Applied Potential (E)"))
plt.title("Fourier Transform of Potential in " + filename[0:10] + " Experiment")
plt.legend(loc="best")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Ai")
#plt.xlim(2800,3000) # If you want, you can specify the axis limits with plt.xaxis(starting_value,ending_value)
plt.show()

# Plots the weights for the current vs frequency
plt.plot(freq,B,'b-',label=("Current (I)"))
plt.title("Fourier Transform of Current in " +filename[0:10] + " Experiment")
plt.legend(loc="best")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Bi")
plt.show()