from util.signal_drawer import *
from util.util import *

def manchester_two(signals, C):
	print(*signals)
	x_values = []
	y_values = []

	i = 1

	while i < (len(signals)+1):
		x_values.append(i)
		i+=1/2

	for i in range(len(signals)):
		if(signals[i] == 0):
			y_values.append(0)
			y_values.append(1)
		else:
			y_values.append(1)
			y_values.append(0)



	print(*signals)
	print("T = t, t = 1/C =", str(1/C))
	print("f_h = 1/T = C =", str(C), "MHz")
	print("f_l = C/(2) =", str(C/(2)), "MHz")
	same, diff = count_swaps_m_two(signals)
	print(same, diff)
	print("f_mid =", (same*C/2 + diff*C)/(len(signals)*2), "MHz")
	print("Middle of spectrum = (f_h + f_l)/2 =", (C + C/2)/2, "MHz")
	print("Spectrum width = f_h - f_l =", C - C/2, "MHz")
	print("bandwidth F: f_h - f_l =", (C - C/2), "MHz")

	plot_signals("Manchester 2 (IEEE 802.3)", x_values, y_values)

def count_swaps_m_two(signals):
	same = 0
	differ = 2
	for i in range(len(signals) - 1):
		if(signals[i]!=signals[i+1]):
			same+=2
		else:
			differ+=2

	return same, differ