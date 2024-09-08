names=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',]
print("Sorry we can accomodate only two people for the party on 1st of January 2021")
while len(names)>2:
    print(f"Sorry {names.pop()} you are not invited to the party on 1st of January 2021")

print(f"{names[0]} and {names[1]} are invited to the party on 1st of January 2021")

del names[0]
del names[0]
print(names)

