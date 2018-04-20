import matplotlib.pyplot as pyplot
import numpy as numpy

pyplot.plot([1, 2, 3, 4])
pyplot.ylabel('some numbers')
pyplot.show()

pyplot.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
pyplot.axis([0, 6, 0, 20])
pyplot.show()

intervals = numpy.arange(0., 5., 0.2)
pyplot.plot(intervals, intervals, 'r--', intervals, intervals **
            2, 'bs', intervals, intervals ** 3, 'g^')
pyplot.show()
