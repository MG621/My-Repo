from classes import House

# STEP 2: DECLARATION

myHouse = House(isqFt = 5, inumRooms = 5, inumBathrooms = 4)

# STEP 3 ACCESS (use dot notation)

print(myHouse.numBathrooms)
print(myHouse.sqFt)
print(myHouse.numRooms)

# Change the sqFt of myHouse to something reasonable

myHouse.sqFt = 5000
print(f"The new square footage of my house is: {myHouse.sqFt}")

# Make another object

neighborsHouse = House(5,4,3)

neighborsHouse.sqFt = 999

print(f"The neighbor's house square footage is: {neighborsHouse.sqFt}")

# Run method from an object
neighborsHouse.unlock()

# Add a new room 3 times to my myHouse

for x in range(3):
    myHouse.addition()
print(f"My house now has {myHouse.numRooms} rooms and {myHouse.sqFt} square feet!")