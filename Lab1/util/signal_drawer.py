from matplotlib import pyplot as plt


def plot_signals(type_code, x_values, y_values):
	plt.title(type_code)
	plt.xlabel("tact")
	plt.ylabel("value")
	plt.grid(True)

	plt.plot(x_values, y_values, drawstyle="steps-post", linewidth = 7)
	plt.show()