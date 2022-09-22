# Write a function that will determine if a number squared is greater than or less than the number multiplied by an 
# input value "mult"
# the function should return true (greater) or false
# Need to know: number, mult

def compare(mult, num):
    squared = num*num
    multiplied = mult*num
    if (squared > multiplied):
        return True
    else:
        return False
def bye():
    print("This is warm up's bye")
#num = int(input("Enter a number: "))
#mult = int(input("Enter the multiplier: "))