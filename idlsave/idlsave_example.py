import idlsave
'''
Read in IDL save file
This file is a structure called fit with tagnames slopes, slope_err, wstart, 
and wend (there are more tagnames but we wont use them)
'''
#Read the entire structure into an object s
s = idlsave.read('G130M_c1291.00_tdsfit.sav')
#Pull out values (or arrays) belonging to the tagnames slopes, slope_err, wstart, and wend in the structure fit
#I've found that this yeilds a nested array ([[a, b, c]]) so I use the 0 index to get just the array ([a, b, c])
#The dot syntax should be familiar to IDL users. This is how you access data in a structure (structure.tagname)
slopes = s.fit.slopes[0]
slope_err = s.fit.slope_err[0]
wstart = s.fit.wstart[0]
wend = s.fit.wend[0]

print wstart
