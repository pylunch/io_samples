# Routine for reading a FITS table into a data structure
import pyfits

class Ftable:
    """ Read in a fits file and return the result as a class with the
        following Attributes:
	   - h = FITS header
	   - d = FITS data
	   - columns = lower-case versions of the column names in the FITS table
	      - these are returned as numpy arrays
	Example: Find the mean of a column named 'flux' in table 'file.fits'
	  f = Ftable("file.fits")
	  print f.flux.mean()
    """    	

    def __init__(self, filename, ext=1):
	""" Creates a new Image object from a FITS file. Multi-extension
	files are supported. Attributes are populated from the header."""
	self.filename = filename+"["+`ext`+"]"
	self.f = pyfits.open(filename)
	self.h = self.f[ext].header
	self.d = self.f[ext].data
	self._changed = False
        self.setcolumns()

    def setcolumns(self):
        self.Columns = []
        if self.d.__dict__.has_key('_names'):
        	names = self.d._names
        else:	
        	names = self.d.names
        for cname in names:
            colname=cname.lower()
            self.Columns += [colname]
            if hasattr(self,colname):
                setattr(self,colname+'_',self.d.field(cname))
            else:
                setattr(self,colname,self.d.field(cname))

    def __getitem__(self,c):
        return self.__dict__[c]

    def __setitem__(self,c,value):
        self.__dict__[c] = value

    def __str__(self):
	longstring="\n "
	for k in self.__dict__:
	    if not k.startswith('_'): #Hide the hidden attributes
		longstring+= k +" : "+ str(self.__dict__[k])+ "\n"
	return longstring

