# Let's compute all the parameters of the loan. There are at least two kinds of loan: those with 
# annuity payment and those with differentiated payment. In this stage, you are going to calculate 
# only the former. Annuity type of payment consists in paying a fixed sum of money at specified 
# intervals, for example, each month or each year. The annuity payment amount is precisely this fixed 
# sum of money that you need to pay at regular intervals.

# Let's assume that annuity payments are made monthly. Thus, we can use the following formula to 
# calculate the monthly payment:

# A = P * i * pow(1 + i, n) / (pow(1 + i, n) - 1)

# Where:
# A = annuity payment
# P = loan principal
# i = nominal (monthly) interest rate. Usually, it is 1/12 of the annual interest rate and 
#     is a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01
# n = number of payments. This is usually the number of months in which repayments will be made

# So far, in this stage you are interested in four values: the number of monthly payments required to repay 
# the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can 
# be calculated if others are known:

 # Loan principal: P = A / (i * pow(1 + i, n) / (pow(1 + i, n) - 1))

 # The number of payments: n = log(A / (A - i * P), i + 1)

 ### Objective ###
 # In this stage, you should add new behavior to the calculator:

# 1) First, you should ask the user which parameter they want to calculate. The calculator should be able to 
#    calculate the number of monthly payments, the monthly payment amount, and the loan principal.
# 2) Then, you need to ask them to input the remaining values.
# 3) Finally, compute and output the value that they wanted.
# Note that you have to ask the user to input parameters in a specific order which is provided below. Simply 
# skip the value the user wants to calculate:
#       1) The first is the loan principal (P in the formulas).
#       2) The second is the monthly payment (A in the formulas).
#       3) The next is the number of monthly payments (n in the formulas).
#       4) The last is the loan interest. The user inputs the interest rate as a percentage, for example, 
#           11.7. You should divide this value by 12 and 100 to use it as i in the formula.

# NOTE: Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" 
# (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

### Output ###
# NOTE: The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

# Example 1: calculating the number of monthly payments

# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# > n
# Enter the loan principal:
# > 1000000
# Enter the monthly payment:
# > 15000
# Enter the loan interest:
# > 10
# It will take 8 years and 2 months to repay this loan!

# Example 2: calculating the monthly payment (the annuity payment)
# NOTE: Use A = P * i * pow(i + 1, n) / (pow(i + 1, n) - 1)

# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# > a
# Enter the loan principal:
# > 1000000
# Enter the number of periods:
# > 60
# Enter the loan interest:
# > 10
# Your monthly payment = 21248!

# Example 3: calculating the loan principal

# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# > p
# Enter the annuity payment:
# > 8721.8
# Enter the number of periods:
# > 120
# Enter the loan interest:
# > 5.6
# Your loan principal = 800000!

### Write here ###
from math import ceil
from math import floor
from math import log

print("What do you want to calculate?")
print("Type 'n' for number of monthly payments,")
print("Type 'a' for annuity monthly payment amount,")
print("Type 'p' for loan principal: ")
choice = input(">> ")
if choice == 'n':
    P = int(input("Enter the loan principal: "))
    mPayment = int(input("Enter the monthly payment: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    n = ceil(log(mPayment / (mPayment - i * P), i + 1)) 
    years = floor(n/12)
    if years == 0:
        print(f"It will take {n} months to repay the loan!")
    else:
        print(f"It will take {years} years and {int(n - (years*12))} months to repay the loan!")
elif choice == 'a':
    P = int(input("Enter the loan principal: "))
    n = int(input("Enter the number of periods: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    A = P * i * pow(i + 1, n) / (pow(i + 1, n) - 1)
    print(f"Your monthly payment ${round(A,2)}!")
else:
    A = float(input("Enter the annuity payment: "))
    n = int(input("Enter the number of periods: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    P = A / (i * pow(1 + i, n) / (pow(1 + i, n) - 1))
    print(f"Your loan principal: ${round(P,2)}!")