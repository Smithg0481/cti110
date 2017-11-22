# ask the user for the dimension of the kitchen
width = float(input("kitchen width? (in ft) "))
length = float(input("kitchen length? (in ft) "))



# calculate the square feet (area)
sqFootage = width * length

# print the square footage
print ("the kitchen is", sqFootage, "sqft.")

#print the square footage
print ("the kitchen is", sqFootage, "sqft.")


# calculate the total price for the tile
costPerSqFt = 0.89
totalCost = sqFootage * costPerSqFt

print("total tile cost is $", format(totalCost,'.2f'))
