"""Simple example of plotting I/O."""

import numpy
import pylab

def draw_line(outfile):
    """
    Draw a straight line and save plot to a file
    of any supported format (emf, eps, pdf, png,
    ps, raw, rgba, svg, svgz).

    Display the image file with any graphics
    display software that supports the given format.

    Examples
    --------
    >>> draw_line('myplot.eps')
    >>> draw_line('myplot.pdf')
    >>> draw_line('myplot.png')

    """
    x = numpy.arange(10)
    y = x

    pylab.plot(x,y)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.title('Straight line')
    pylab.draw()
    pylab.savefig(outfile)
