from RecursiveBayesianEstimator import RecursiveBayesianEstimator


def main():
	print '[ recursive bayesian estimator ]'

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

	T = 50
	print '\nActual temperature:\t%d degrees C' % T
	rbe = RecursiveBayesianEstimator()


if __name__ == '__main__':
	main()
