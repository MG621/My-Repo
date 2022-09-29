# Blueprint for a house
class House:
    # Initialize objects
    def __init__(self, isqFt, inumRooms, inumBathrooms):
        self.numRooms = inumRooms
        self.sqFt = isqFt
        self.numBathrooms = inumBathrooms
    #define methods
    def unlock(self):
        print("The house is unlocked!")
    def addition(self):
        # This function should add a new room and 200 sqFt to the house
        self.numRooms += 1
        self.sqFt = self.sqFt + 200