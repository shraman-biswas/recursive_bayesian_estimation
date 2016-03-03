import sys

from matplotlib import animation as animation
from matplotlib import pyplot as plt


class Animate:

	def __init__(self):
		# setup
		self._setup_params()
		self._create_data()
		self._setup_plot()
		self._setup_axes()
		# start animation
		self._anim = animation.FuncAnimation(self._fig, self._animate, \
							init_func=self._init, \
							repeat=True, \
							interval=30, \
							blit=True)
		plt.show()

	def _init(self):
		# initialize animation
		self._line_actual.set_data(self._X, self._T)
		self._line_measured.set_data(self._X, 0)
		self._line_result.set_data(self._X, 0)
		self._line_posterior.set_data([n for n in range(self._M)], 0)
		return self._line_actual, self._line_measured, self._line_result, self._line_posterior,

	def _animate(self, frame_num):
		# calculate estimate at every frame
		estimate = self._recursive_bayesian_estimator()
		sys.stdout.write("\rEstimated temperature:\t%d degrees C " % \
								estimate)
		sys.stdout.flush()
		return self._update_plot()

	def _setup_plot(self):
		self._fig, (self._ax1, self._ax2) = plt.subplots(nrows=2, 
								ncols=1)
		plt.tight_layout(pad=3, w_pad=0, h_pad=3)
		self._fig.suptitle("Recursive Bayesian Estimator",
						fontsize=self._font_size)
		self._fig.canvas.set_window_title(
					"Recursive Bayesian Estimator")
		self._fig.set_size_inches(10, 10, forward=True)

	def _setup_axes(self):
		# setup top plot - temperature vs time
		self._ax1.axis([0, self._N, 0, self._M + 30])
		self._ax1.set_xlabel("time (ms)", fontsize=self._font_size)
		self._ax1.set_ylabel("temperature (degrees C)", \
						fontsize=self._font_size)
		self._ax1.set_title("temperature sensor reading", \
						fontsize=self._font_size)
		self._line_actual, = self._ax1.plot([], [], "g")
		self._line_measured, = self._ax1.plot([], [], "r")
		self._line_result, = self._ax1.plot([], [], "b")
		self._ax1.legend(["actual", "measured", "result"], \
						fontsize=self._font_size)
		# setup bottom plot
		self._ax2.axis([0, self._M, 0, 1])
		self._ax2.set_xlabel("temperature (degrees C)", \
						fontsize=self._font_size)
		self._ax2.set_ylabel("probability", fontsize=self._font_size)
		self._ax2.set_title("posterior probability distribution", \
						fontsize=self._font_size)
		self._line_posterior, = self._ax2.plot([], [], "b")

	def _update_plot(self):
		self._line_measured.set_ydata(self._measured)
		self._line_result.set_ydata(self._result)
		self._line_posterior.set_ydata(self._Po)
		return self._line_actual, self._line_measured, self._line_result, self._line_posterior,
