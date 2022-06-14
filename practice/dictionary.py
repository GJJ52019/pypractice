#examples of dictionaries and thier basic uses in python

#convert three digit month names to full names ex: jan to january

#dictionaries use {}, tuples use (), arrays use [].
#Each entry has key: followed by its value (Key: value) for key vauled pairs

# can also use numbers instead of strings for keys.
# each key must be different
monthsConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#access with brackets
print(monthsConversions["Nov"])

#.get access
print(monthsConversions.get("Dec"))

#when not able to access something use default
print(monthsConversions.get("fun", "not a default value"))

#dictonaries can also be containted within list

mediaList = [
    {
    'movies': ['alien','aliens','alien3'],
    'games': ['AVP, 2000','AVP,2002','Isolation'],
    'tvShow' : None,
    'gamesAndMovies': True
    }, 
    { 
    'movies': ['Toy Story','Touy Story 2','Toy Story 3','Toy Story 4'],
    'games': ['Toy Story 2'],
    'tvShow' : ['Buzz lightYear'],
    'gamesAndMovies': True
}
]

#prints the third item in the movies key in the second list option
print(mediaList[1]['movies'][2])