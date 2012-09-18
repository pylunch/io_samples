"""
Simple example of FITS I/O.

For PyFITS 3.1 or later.

http://packages.python.org/pyfits/appendix/header_transition.html

"""
import numpy
import pyfits
import pylab

def new_fits(outfile, **kwargs):
    """
    Write a multi-extension FITS from scratch.
    
    Extensions are in HST format::

        0. PRIMARY
        1. SCI
        2. ERR
        3. DQ

    Parameters
    ----------
    outfile : str
        Output FITS filename.

    **kwargs : keyword(s) for `pyfits.HDUList.writeto`

    Examples
    --------
    >>> new_fits('myimage.fits', clobber=True)
    
    """
    # Fake data
    sci_data = numpy.arange(10000, dtype='float').reshape(100,100)
    err_data = numpy.sqrt(sci_data)  # Poisson error
    dq_data  = numpy.zeros(sci_data.shape, dtype='int16')  # No bad pixel

    # Create individual extensions
    hdu_hdr = pyfits.PrimaryHDU()
    hdu_sci = pyfits.ImageHDU(sci_data)
    hdu_err = pyfits.ImageHDU(err_data)
    hdu_dq  = pyfits.ImageHDU(dq_data)

    # Modify headers
    
    hdu_hdr.header['FILENAME'] = outfile
    hdu_hdr.header['NEXTEND'] = 3
    
    hdu_sci.header['BUNIT'] = 'COUNTS'
    hdu_sci.header['EXTNAME'] = 'SCI'
    hdu_sci.header['EXTVER'] = 1

    hdu_err.header['BUNIT'] = 'COUNTS'
    hdu_err.header['EXTNAME'] = 'ERR'
    hdu_err.header['EXTVER'] = 1

    hdu_dq.header['BUNIT'] = 'UNITLESS'
    hdu_dq.header['EXTNAME'] = 'DQ'
    hdu_dq.header['EXTVER'] = 1

    # Create multi-extension FITS
    hduList = pyfits.HDUList([hdu_hdr])
    hduList.append(hdu_sci)
    hduList.append(hdu_err)
    hduList.append(hdu_dq)

    # Write to file
    hduList.writeto(outfile, **kwargs)

def view_fits(infile):
    """
    Assortments of ways to view FITS data.

    Examples
    --------
    >>> view_fits('myimage.fits')

    """
    pf = pyfits.open(infile)  # Read-only

    # Look at available extensions.
    # This is slightly different than IRAF catfits.
    pf.info()

    for ext in range(4):
        # Look at all the headers
        print
        print repr(pf[ext].header)
        print

        if ext == 0:
            continue

        # View all the data, except PRIMARY header
        fig = pylab.figure()
        ax = fig.add_subplot(111)
        cax = ax.imshow(pf[ext].data)
        ax.set_title('Ext {}'.format(ext))
        fig.colorbar(cax)

    # You can manipulate FITS data like any numpy array.
    # Python starts from 0, IRAF starts from 1.
    # Python indexing is [Y,X], IRAF is [X,Y].
    # Python index range is [inclusive:exclusive],IRAF is [inclusive:inclusive].
    print
    print 'Mean SCI at IRAF region X=10:55 Y=80]:', \
          pf['SCI',1].data[79,9:55].mean()
    print 'ERR at IRAF coord X=50 Y=10:', pf['ERR',1].data[9,49]
    print

    pf.close()

def modify_fits(infile):
    """
    Modify existing FITS data.

    Examples
    --------
    modify_fits('myimage.fits')

    """
    with pyfits.open(infile,mode='update') as pf:

        # Add/update a keyword
        pf['PRIMARY'].header['MY_KEYWD'] = 2.0

        # Add HISTORY
        pf['PRIMARY'].header['HISTORY'] = 'Multiplied SCI by 2.'

        # Modify SCI data
        pf['SCI',1].data *= 2.0

        # Recalculate ERR data
        pf['ERR',1].data = numpy.sqrt(pf['SCI',1].data)

    # Look at the modified contents using function above
    view_fits(infile)
