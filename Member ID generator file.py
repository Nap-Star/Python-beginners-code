# SCRATCH 1
#Giving member id based on corridor colour, row and column
#Entering corridor
counter=True

while counter:
  corridor= input("Enter a corridor (red,blue,yellow,green)")
  if corridor=="red" or corridor=="blue" or corridor=="yellow"or corridor=="green":
    counter=False
    print("correct input")
  else:
    print("Incorrect input please try again")
    counter=True


#Entering row
counter=True

while counter:
  row=int(input("Enter a row (1-3)"))
  if 1<= row <= 3:
    counter=False
    print("correct input")
  else:
    print("Incorrect input please try again")
    counter=True

#Entering column

counter=True

while counter:
  column=int(input("Enter a column (1-12)"))
  if 1<= column <= 12:
    counter=False
    print("correct input")
  else:
    print("Incorrect input please try again")
    counter=True


print("Location is", str(row)+corridor+str(column))
print("Location is", corridor[0]+str(row**column))