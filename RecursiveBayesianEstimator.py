import math
import random
import sys

from Animate import Animate
from matplotlib import pyplot as plt


class RecursiveBayesianEstimator(Animate):

	def _pmf(self, x, mu):
		# return the probability mass function for x and mu
		return math.exp(-0.5*(((x - mu)/self._sigma)**2)) / (self._sigma * math.sqrt(2 * math.pi))

	def _recursive_bayesian_estimator(self):
		# get noisy measurement
		meas = self._T + random.gauss(0, self._sigma)
		self._measured = self._measured[1:]
		self._measured.append(meas)
		# local variables
		norm = 0
		estimate = -1
		tmp = -1
		# recursive Bayesian estimation
		self._Pr = list(self._Po)
		for n in range(self._M):
			self._Po[n] = self._Pr[n] * self._pmf(meas, n)
			norm += self._Po[n]
			if self._Po[n] > tmp:
				tmp = self._Po[n]
				estimate = n
		for n in range(self._M):
			self._Po[n] = self._Po[n] / norm
		# update result with estimate
		self._result = self._result[1:]
		self._result.append(estimate)
		return estimate

	def _setup_params(self):
		self._font_size = 15
		self._sigma = 10	# standard deviation of noise
		self._N = 100 		# number of samples
		self._M = 100		# number of discrete temperature levels
		self._T = self._M / 2	# temperature

	def _create_data(self):
		self._Pr = [1.0 / self._M for _ in range(self._M)]	# prior
		self._Po = list(self._Pr)			# posterior
		self._X = [n for n in range(self._N)]
		self._measured = [0 for _ in range(self._N)]
		self._result = [0 for _ in range(self._N)]
