# include your other code here
import funcWarmUp
from anotherFunction import hi, bye, tenSqr
# import * means all functions
# write script (main function) here

# call our function
print(funcWarmUp.compare(5,9))
# call the "hi" function
hi()
bye()
# call the bye function from funcWarmUp
# because "import funcWarmUp", use dot notation
funcWarmUp.bye()

num = 9
#call here
print(tenSqr(num))