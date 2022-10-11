# Object that can be stocked in a warehouse
# Define a class for clothing
    # Attributes
        # Department
        # Weight
        # Name
        # Material
        # Initialize def __init__(self):
            ## add attributes as input paramenters
            ## add default value for attributes
class Clothing():
    def __init__(self, department = 'misc', weight = 0, name = ' ', material = ' '):
        self.department = department
    # Print the department of the item
    def check(self):
        print(self.department)

# Declare a clothing object 



# Warehouse class
class Warehouse():
    def __init__(self):
        self.inventory = {}
# Add new items
    def add(self, item = None):
        # First case - department is not in inventory
        if item.department in self.inventory.keys():
            # Access inventory and add 1 pair of shoes
            self.inventory[item.department] += 1
        else:
            # Create new department in inventory with new item
            self.inventory[item.department] = 1
# Define a warehouse that will hold clothing items
# Inventory (per department)

# Ship items (remove)
### For inventory - a good choice might be a dictionary

myDictionary = {
    'shoes': 0,
    'pants': 3
}
print(myDictionary.keys())

myWareHouse = Warehouse()
# Create 2 clothing items
myHat = Clothing('hats')
myShoes = Clothing('shoes')
## One with department shoes, the other with another department
myWareHouse.add(myHat)
myWareHouse.add(myShoes)
print(myWareHouse.inventory)
