#modules basics 
# create a file that python files can call on to use
# use import then call this files name to use the functions and variables in this file
# this module contains a rolling dice function
#find more to import at docs.python.org/3/py-modindex.html
#offical ones are built in just need import found in external libraries in the lib folder
#more to be found on thrid party sites as well
# us pip install to install other python modules

import random

#needs to be passed a int for the number of sides a the requested dice has
def roll_die(num):
    return random.randint(1,num) # uses random then gets number between 1 and passed variable

#example of calling in another python file this file must be findable 
# import modules
# print(modules.roll_die)