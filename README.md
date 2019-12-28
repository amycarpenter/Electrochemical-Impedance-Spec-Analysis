# Electrochemical-Impedance-Spec-Analysis
## Introduction
These files were made to analyze the results of electrochemical impedance spectroscopy experiments in the frequency domain. The file fftGraphing.py graphs the data, and mainfreqs.py finds the peaks in the graphs. 
## Input file
The applied potential is represented by E and the output current by I. The input file is expected to be a .txt file with these five columns:<br>
| Time | Frequency | E_real | E_imag | I_real | I_imag |.<br>
The data has been manipulated to represent the potential and current as the sum of just sine terms with a phase angle. Thus, there is only one amplitude corresponding to each frequency for the current and potential. See the attached image (math_manipulation.png) for the math.
## fftGraphing.py
This script graphs the amplitudes of the potential versus the frequencies, followed by the amplitudes of the current versus the frequencies. 
## mainfreqs.py
This script finds the peaks in the graphs shown by fftGraphing.py. The user will enter a percentage for the "contribution criterion" (usually around 0.01 – 0.05). If the amplitude associated with a given frequency constitutes at least that percentage of the sum of all the amplitudes, it is considered a “main contributing frequency.” The output is a .csv file with columns:<br>
} Frequency | Amplitude of Potential | Amplitude of Current|.<br>
Only “main” frequencies are listed.
## Acknowledgments
These files were created as part of MATH 370 St: Applied and Industrial Mathematics at Lee University. Some useful papers that inspired this work were: 
1. D. A. Harrington, *Theory of electrochemical impedance surface reactions: second-harmonic and large-amplitude response*, Canadian Journal of Chemistry 75, (1997).
2. C.  Hernandez-Jaimes,  J.  Vazquez-Arenas,  J.  Vernon-Carter,  and  J.  Alvarez-Ramirez, *A nonlinear Cole-Cole model for large amplitude electrochemcial impedancespectroscopy*, Chemical Engineering Science137, (2015),1-8.
3. R.  L.  Sacci  and  D.  A.  Harrington, *Dynamic Electrochemical Impedance Spectroscopy*,  Department  of  Chemistry,  University  of  Victoria,  Victoria,  British Columbia V8W3V6, Canada.
