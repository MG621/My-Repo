# Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll 
# do this for the type of repayment where the loan principal is reduced by a constant amount 
# each month. The rest of the monthly payment goes toward interest repayment and it is gradually 
# reduced over the term of the loan. This means that the payment is different each month. Let’s 
# look at the formula:

# Dm = P / n + i * (P - P * (m - 1) / n)

# Where:
# Dm = mth differentiated payment
# P = loan principal
# i = nominal (monthly) interest rate. Usually, it is 1/12 of the annual interest rate and 
#     is a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01
# n = number of payments. This is usually the number of months in which repayments will be made.
# m = current repayment month.

 ### Objective ###
 # In this stage, you are going to implement the following features:

# 1) Calculation of differentiated payments. To do this, the user can run the program specifying interest, 
#    number of monthly payments, and loan principal.
# 2) Ability to calculate the same values as in the previous stage for annuity payment (principal, number 
#    of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line 
#    arguments, and one parameter will be unknown. This is the value the user wants to calculate.

### Output ###
# NOTE: The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

# Example 1: calculating differentiated payments

# type=diff principal=1000000 periods=10 interest=10

# Month 1: payment is 108334
# Month 2: payment is 107500
# Month 3: payment is 106667
# Month 4: payment is 105834
# Month 5: payment is 105000
# Month 6: payment is 104167
# Month 7: payment is 103334
# Month 8: payment is 102500
# Month 9: payment is 101667
# Month 10: payment is 100834

# Overpayment = 45837

# Example 2: calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest

# type=annuity principal=1000000 periods=60 interest=10

# Your annuity payment = 21248!
# Overpayment = 274880

# Example 3: calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%

# type=diff principal=500000 periods=8 interest=7.8

# Month 1: payment is 65750
# Month 2: payment is 65344
# Month 3: payment is 64938
# Month 4: payment is 64532
# Month 5: payment is 64125
# Month 6: payment is 63719
# Month 7: payment is 63313
# Month 8: payment is 62907

# Overpayment = 14628

# Example 4: calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest

# type=annuity payment=8722 periods=120 interest=5.6

# Your loan principal = 800018!
# Overpayment = 246622

# Example 5: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest

# type=annuity principal=500000 payment=23000 interest=7.8

# It will take 2 years to repay this loan!
# Overpayment = 52000

### Write here ###
from math import ceil
from math import floor
from math import log

print("What do you want to calculate?")
print("Type 'd' for differetiated monthly payment amount,")
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
    print(f"Overpayment ${round((mPayment*n)-P,2)}")
elif choice == 'a':
    P = int(input("Enter the loan principal: "))
    n = int(input("Enter the number of periods: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    sum = 0
    for m in range(1,n+1):
        A = P * i * pow(i + 1, n) / (pow(i + 1, n) - 1)
        sum += A
    print(f"Your monthly payment ${round(A,2)}!")
    print(f"Overpayment ${round(sum-P,2)}")
elif choice == 'd':
    P = int(input("Enter the loan principal: "))
    n = int(input("Enter the number of periods: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    sum = 0
    for m in range(1,n+1):
        Dm = P / n + i * (P - P * (m - 1) / n)
        sum += Dm
        print(f"For month #{m} payment is: ${round(Dm,2)}")
    print(f"Overpayment ${round(sum-P,2)}")
else:
    A = float(input("Enter the annuity payment: "))
    n = int(input("Enter the number of periods: "))
    i = float(input("Enter the loan interest: "))
    i = i/1200
    P = A / (i * pow(1 + i, n) / (pow(1 + i, n) - 1))
    print(f"Your loan principal: ${round(P,2)}!")
    print(f"Overpayment ${round((A*n)-P,2)}")