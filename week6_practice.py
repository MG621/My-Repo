from random import randint

# Name: Mario A. Garza

# Create and print out a new list that only contains the integers from the given list below.

randList = [45, 2, 'true', True, 0, '100', 4, 2.01, 3.33, 86, False]

### Write here ##

newList = [x for x in randList if type(x) == int]
print(newList)

#--------------------------------------------------------------------------------------------------------

# Given a list of random integers below, go through the list and place all even integers in one list
# and all odd integers in another. Print both lists once done.

randInts = []
for i in range(100):
    randInts.append(randint(0,999))

### Write here ###

evenNum = [x for x in randInts if x % 2 == 0]
oddNum = [x for x in randInts if x % 2 == 1]
print("Even Numbers")
print(evenNum)
print("Odd Numbers")
print(oddNum)

#--------------------------------------------------------------------------------------------------------

# Find the largest and smallest number from the following three lists. 
# Optional: print which list they came from as well as its index location.

nums1 = [-29, -81, 86, 45, 58, 187, 659, -11, 114, 3]
nums2 = [128, -100, 409, -110, 179, -102, 671, 95, 3, 86]
nums3 = [-118, 104, -13, 11, 320, 202, -32, 608, 372, -750]

### Write here ###
indexLarge = 0
indexSmall = 0
smallest = nums1[0]
largest = nums1[0]
for x in nums1:
    if x < smallest:
        smallest = x
        indexSmall = nums1.index(smallest)
for x in nums1:
    if x > largest:
        largest = x
        indexLarge = nums1.index(largest)
print("List 1")
print(f"Smallest number: {smallest}")
print(f"The index is: {indexSmall}")
print(f"Largest number: {largest}")
print(f"The index is: {indexLarge}")

smallest = nums2[0]
largest = nums2[0]
indexLarge = 0
indexSmall = 0
for x in nums2:
    if x < smallest:
        smallest = x
        indexSmall = nums2.index(smallest)
for x in nums2:
    if x > largest:
        largest = x
        indexLarge = nums2.index(largest)
print("List 2")
print(f"Smallest number: {smallest}")
print(f"The index is: {indexSmall}")
print(f"Largest number: {largest}")
print(f"The index is: {indexLarge}")

smallest = nums3[0]
largest = nums3[0]
indexLarge = 0
indexSmall = 0
for x in nums3:
    if x < smallest:
        smallest = x
        indexSmall = nums3.index(smallest)
for x in nums3:
    if x > largest:
        largest = x
        indexLarge = nums3.index(largest)
print("List 3")
print(f"Smallest number: {smallest}")
print(f"The index is: {indexSmall}")
print(f"Largest number: {largest}")
print(f"The index is: {indexLarge}")

