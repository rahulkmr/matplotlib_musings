import numpy as numpy
import matplotlib.pyplot as pyplot

def f(t):
    return numpy.exp(-t) * numpy.cos(2 * numpy.pi * t)


t1 = numpy.arange(0.0, 5.0, 0.1)
t2 = numpy.arange(0.0, 5.0, 0.02)

pyplot.figure(1)
pyplot.subplot(211)
pyplot.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

pyplot.subplot(212)
pyplot.plot(t2, numpy.cos(2 * numpy.pi * t2), 'r--')

pyplot.show()
