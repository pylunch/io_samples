import pyfits

#Everything I know I learned from the pyfits users manual. I suggest looking at 
#examples in it

####################
#Reading in a fits binary table
####################

#Two ways to do this:
#1: open the file then get the table data
#2. use a conviencence function to get the table data
#Unless I have to modify the data, I always use option #2

#1 
#Open the file
ofile = pyfits.open('w7h1935dl_tds.fits') #If you want to edit this, use mode = 'update'
#Get the table data from the first extension into variable tbdata
tbdata = ofile[1].data

#2
#Get table data from the first extension into variable tbdata
tbdata = pyfits.getdata('w7h1935dl_tds.fits', 1)

#1 & 2 

#Get columns wavelength and time into separate variables
wl = tbdata['wavelength']  #index by column name
t = tbdata['time']

print t

###################
#Writing a fits binary table
###################

#This is a bit trickier since you have to make a table with column objects which you then write to a file

slope = tbdata['slope']

#Create wavelength and time column objects
#These are going to be 1D arrays (hence the indexing)
c1 = pyfits.Column(name = 'wavelength', format = 'D', array = wl[0])
c2 = pyfits.Column(name = 'time', format = 'D', array = slope[0][0])

#Create table HDU
tbhdu = pyfits.new_table([c1, c2])

tbhdu.writeto('table_example.fits')

