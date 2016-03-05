from RecursiveBayesianEstimation import RecursiveBayesianEstimation


def main():
	print '[ recursive bayesian estimation ]'

	# parameters
	T = 50	# actual temperature reading
	params = [T]

	# display header text
	print ("Made by: Shraman Biswas"
			"\nDate: Dec 2015"
			"\nDescription:"
			"\nEstimates actual temperature value from noisy sensor measurements"
			"\nUses recursive Bayesian estimation"
			"\n\nBayes theorem:"
			"\n\t         P(H) x P(D|H)"
			"\n\tP(H|D) = -------------"
			"\n\t             P(D)"
			"\n\twhere,"
			"\n\t\tP(H) -> prior"
			"\n\t\tP(D|H) -> likelihood"
			"\n\t\tP(D) -> normalizing term"
			"\n\t\tP(H|D) -> posterior")

	# display temperature
	print '\nActual temperature:\t%d degrees C' % T

	# start recursive bayesian estimation
	rbe = RecursiveBayesianEstimation(params)


if __name__ == '__main__':
	main()
