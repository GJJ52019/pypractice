#objects file using the class made in alienClass.py
#calls on the Alien class

# use from to call file then import the class to use
from alienClass import Alien

#creates a new object within the class must have all the variables
alien1 = Alien("LionDuck", 6 , "omnivore", True)

print(alien1.is_a_threat)