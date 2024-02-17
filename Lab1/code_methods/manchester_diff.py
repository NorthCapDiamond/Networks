from util.signal_drawer import *
from util.util import *

def manchester_diff(signals, C):
	print(*signals)
	x_values = []
	y_values = []

	print("T = t, t = 1/C =", str(1/C))
	print("f_h = 1/T = C =", str(C), "MHz")
	print("f_l = C/2 =", str(C/2), "MHz")

	i = 1

	while i < (len(signals)+1):
		x_values.append(i)
		i+=1/2


	l = 1
	r = 0

	if(signals[0] == 0):
		y_values.append(l)
		y_values.append(r)
	else:
		l, r = r, l
		y_values.append(l)
		y_values.append(r)

	for i in range(1, len(signals)):
		if(signals[i] == signals[i-1] == 1):
			l,r = r,l
			y_values.append(l)
			y_values.append(r)
		elif (signals[i] == 1 and signals[i-1] == 0):
			l,r = r,l
			y_values.append(l)
			y_values.append(r)
		else:
			y_values.append(l)
			y_values.append(r)


	same, diff = count_swaps_diffm(signals)
	print(same, diff)
	print("f_mid =", (same*C/2 + diff*C)/(len(signals)*2), "MHz")
	print("Middle of spectrum = (f_h + f_l)/2 =", (C/2 + C)/2, "MHz")
	print("Spectrum width = f_h - f_l =", (C/2), "MHz")
	print("bandwidth F: f_h - f_l =", (C/2), "MHz")

	plot_signals("Manchester Thomas", x_values, y_values)

def count_swaps_diffm(signals):
	same = 0
	differ = 2
	for i in range(len(signals)-1):
		if(signals[i] == signals[i+1] == 1):
			same+=2
		elif (signals[i] == 0 and signals[i+1] == 1):
			same+=2
		elif (signals[i] == 1 and signals[i+1] == 0):
			differ+=2
		elif (signals[i] == 0 and signals[i+1] == 0):
			differ+=2
		else:
			differ+=2

	return same, differ