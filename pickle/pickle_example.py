import pickle
import numpy as np

#Example inspired from http://wiki.python.org/moin/UsingPickle
######################
#Creating a pickled file
######################
#Create a dictionary
animal_colors = {'lion': 'gold', 'cat': 'tabby', 'parrot': 'rainbow'}
#Open file to save pickled object to
#Make sure it is writable
ofile = open('animal_colors_dict.pkl', 'w')
#Save animal_colors dictionary to the open file
pickle.dump(animal_colors, ofile)
ofile.close()

######################
#Reading a pickled file
######################
#Open pickled file
ofile = open('animal_colors_dict.pkl', 'r')
#Load in dictionary from the pickled file
animal_colors = pickle.load(ofile)
print animal_colors
