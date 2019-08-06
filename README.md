# Electrochemical-Impedance-Spec-Analysis
## Introduction
These files were made to analyze the results of electrochemical impedance spectroscopy experiments in the frequency domain. The input file should be of the form 
The file fftGraphing.py graphs the data, and mainfreqs.py finds the peaks in the graphs. 
## Input file
The applied potential is represented by E and the output current by I. The input file is expected to be a .txt file of the with each column as follows: Frequency | E_real | E_imag | I_real | I_imag. The data has been manipulated to represent the potential and current as the sum of only sine terms. See the attached image for the math.
## fftGraphing.py
This script graphs the amplitudes of the potential versus the frequencies, followed by the amplitudes of the current. 
## mainfreqs.py
This script finds the peaks in the graphs shown by fftGraphing.py. In other words, it finds the frequencies
The user will enter a percentage (usually around 0.01 – 0.05). If the amplitude associated with a frequency constitutes at least that percentage of the sum of all the amplitudes, it is considered a “main contributing frequency.” The output is a .csv file with columns: Frequency | Amplitude of Potential | Amplitude of Current. Only “main” frequencies are listed.
## Acknowledgments
These files were created as part of MATH 370 St: Applied and Industrial Mathematics. Some useful papers that inspired this work were: 
1. D.A.  Harrington,Theory of electrochemical impedance surface reactions: second-harmonic and large-amplitude response, Canadian Journal of Chemistry75, (1997).
2. C.  Hernandez-Jaimes,  J.  Vazquez-Arenas,  J.  Vernon-Carter,  and  J.  Alvarez-Ramirez,A nonlinear Cole-Cole model for large amplitude electrochemcial impedancespectroscopy, Chemical Engineering Science137, (2015),1-8.
3. R.  L.  Sacci  and  D.  A.  Harrington,Dynamic Electrochemical Impedance Spec-troscopy,  Department  of  Chemistry,  University  of  Victoria,  Victoria,  British Columbia V8W3V6, Canada.
