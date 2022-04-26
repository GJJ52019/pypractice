# gets a name and says hello if its in the array

#___________Asingments__________________________________________________
knownNames = ["Pat","Nick","Gary","Marc","Amanda","Nikki","Hannah","Chris","Tyler","Pete"]

i=0

listSize = len(knownNames)

pOI = "stranger"
#____________________________________________________________________
#$$$$$$$$$$$$$$$$ TEST $$$$$$$$$$$$$$$$$$$$
print(knownNames)
print(pOI)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#+++++++++++++++++++ Start of Program +++++++++++++
print("Hello please input your name:")

inputName = input()

while i < listSize:
    if knownNames[i] == inputName:
        pOI = inputName
        break
    else: i+=1


print("Hello " + pOI)