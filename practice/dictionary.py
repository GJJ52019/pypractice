#examples of dictionaries and thier basic uses in python

#convert three digit month names to full names ex: jan to january

#dictionaries use {} tuples use () arrays use []
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