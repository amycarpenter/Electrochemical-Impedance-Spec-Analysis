########################################################################
# This program outputs a file with the mainfreqs and their contributions
# to the potential and current.
# It take an fft file as input.
########################################################################

from numpy import loadtxt,arctan,empty,sin,cos

########################################################################
#  Functions
########################################################################

# This function calculates the mainfreqs and enters the contributions into a file
def mainfreqs(A,B,freq,contr_criterion,filename,header):

	# Creates a new csv file
	newfilename = 'Mainfreqs ' + filename[0:31] + ' ' + header + '.csv' # you can edit what the name of the file will be here
	working_file = open(newfilename,'wt')
	working_file.write('Frequency Contribution Analysis\n')
	working_file.write(filename + '\n')
	working_file.write('Contribution criterion: %5f\n' % contr_criterion)
	working_file.write('Frequency,' + header + '\n')
	
	totalA=0.0
	totalB=0.0
	for i in range(1,len(freq)):
		totalA+=abs(A[i])
		totalB+=abs(B[i])
	for i in range(1,len(freq)):
		contributionA=abs(A[i]/totalA) # finds the percentage of contribution
		contributionB=abs(B[i]/totalB)
		ismainfreqA = (contributionA > contr_criterion) # ismainfreq will be either True or False
		ismainfreqB = (contributionB > contr_criterion)
		if ismainfreqA or ismainfreqB:
			working_file.write('%3.2f,' % freq[i])
			if ismainfreqA:
				working_file.write('%6f%%,' % (contributionA*100))
			else:
				working_file.write(',')
			if ismainfreqB:
				working_file.write('%6f%%\n' % (contributionB*100))
			else:
				working_file.write('\n')
	working_file.close()
	

# This function calculates the phase angles and finds the weights, A and B, just like in fftGraphing.py
def findWeights(E_real,E_imag,I_real,I_imag):

	# Creates an array to store the values of the weights
	A = empty([len(freq),1],float)
	B = empty([len(freq),1],float)

	# The 'frequency' of 0 is just the sum of every point - we don't care about that here
	# So set the value of these weights to 0
	A[0]=0
	B[0]=0

	# Finds the phase angles (phi) and calculates the weights for each frequency
	for i in range(1,len(freq)-1):
		Iphi = arctan(I_real[i]/I_imag[i])
		B[i] = abs(I_imag[i]/cos(Iphi))  # could have equivalently used abs(I_real[i]/sin(phi))
		Ephi = arctan(E_real[i]/E_imag[i]) 
		A[i] = abs(E_imag[i]/cos(Ephi))
	return A,B

########################################################################

# Extracts the data from the input file
name = input('FFT filename prefix: ')
filename = str(name) + '.txt'
data = loadtxt(filename,skiprows=2)
freq = data[:,0]
E_real = data[:,1]
E_imag = data[:,2]
I_real = data[:,3]
I_imag = data[:,4]

contr_criterion = float(input('Contribution criterion: '))

A,B = findWeights(E_real,E_imag,I_real,I_imag)
mainfreqs(A,B,freq,contr_criterion,filename,'Potential,Current')

# If you want to look at the real and imaginary part separately, 
# execute these commands instead:
# mainfreqs(E_real,E_imag,freq,contr_criterion,filename,'E_real,E_imag')
# mainfreqs(I_real,I_imag,freq,contr_criterion,filename,'I_real,I_imag')