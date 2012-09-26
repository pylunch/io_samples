# Utilities for formatting and printing one-dimensional numpy arrays.
# Saves having to loop through the arrays explicitly.
#
# H. Ferguson - revised 1/8/04
#
"""Utilities for formatting and printing one-dimensional numpy arrays.
Usage example:
  
>>> from numpy import *
>>> from numprint import *
>>> x = arange(5.)
>>> y = x*2.
>>> z = sqrt(x)
>>> l = format("%10.1f %10.2f",x,y)
>>> l.heading("%10s %10s" % ("x","2x"))
>>> print l
         x         2x
       0.0       0.00
       1.0       2.00
       2.0       4.00
       3.0       6.00
       4.0       8.00

>>> l.addcols("%10.3f",z)
>>> l.addheading(" %10s" % "sqrt(x)")
>>> print l
         x         2x    sqrt(x)
       0.0       0.00      0.000
       1.0       2.00      1.000
       2.0       4.00      1.414
       3.0       6.00      1.732
       4.0       8.00      2.000
"""

__version__ = '1.0'
__author__ = 'Henry C. Ferguson, STScI'


class format:
    """Format a numpy array for printing"""
    def __init__(self,fmt,*args):
        """Specify the print format for a set of columns.

           Arguments:
           fmt -- Standard format string
           args -- one-dimensional array to print. Must be the same length.
        """
        self.head=''
        self.lines = printcols(fmt,*args)
    def heading(self,heading):
        """Specify the heading for a set of columns.

           Arguments:
           heading -- String to use as the heading (e.g. column labels).
        """
        self.head = heading
    def addheading(self,heading):
        """Specify the heading for a set of columns.

           Arguments:
           addheading -- Add some more column labels to an existing heading
        """
        self.head += heading
    def addcols(self,fmt,*args,**keywords):
        """Add more columns to the output.

           Arguments:
           fmt -- Standard format string
           args -- one-dimensional array to print. Must be the same length.
           separator -- Keyword argument. specifies a field separator to use 
                between these new columns an the previous ones. Default is ' '.
        """
        newcols = printcols(fmt,*args)
        if keywords.has_key('separator'):
            separator = keywords['separator']
        else:
            separator = ' ' 
        for i in range(len(newcols)):
            self.lines[i] = self.lines[i]+separator+newcols[i]
    def __repr__(self):
        """Display the output (returns a string).""" 
        s = ''
        if len(self.head) > 0:
            s = self.head+'\n' 
        for i in range(len(self.lines)):
            s += self.lines[i]+'\n'
	return s[:-1]
    def writeto(self,file,append=0):
        """Print the output to a file.""" 
        if append:
            f = open(file,'a')
        else:
            f = open(file,'w')
        f.write(self.__repr__())
        f.close

def printcols(fmt,*args):
    n = len(args[0])
    ncols = len(args)
    newcols = []
    for i in range(n):
        l = []
        for ii in range(ncols):
            l = l + [args[ii][i]]
        ll = tuple(l)
        s = fmt % ll
        newcols += [s]     
    return(newcols)

if __name__ == "__main__":
    from numpy import *
    x = arange(5.)
    y = x*2.
    z = sqrt(x)
    l = format("%10.1f %10.2f",x,y)
    l.heading("%10s %10s" % ("x","2x"))
    print l
    l.addcols("%10.3f",z)
    l.addheading(" %10s" % "sqrt(x)")
    print l
