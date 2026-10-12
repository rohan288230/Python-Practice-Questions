# Q19. ATM Withdrawal
# User se:
# - Account balance
# - Withdrawal amount
# input lo.
# Rules:
# 1. Withdrawal amount balance se zyada hai → "Insufficient Balance"
# 2. Otherwise check karo withdrawal amount ₹500 ke multiple mein hai ya nahi.
# 3. Multiple hai → "Withdrawal Successful"
# 4. Nahi hai → "Amount must be multiple of 500"
# Isme nested if use karo.
account_balance = int(input("Enter your Account Balance : "))
withdrawal_balance = int(input("Enter Withdrawal Balance : "))
if account_balance < withdrawal_balance:
    print("Insufficient Balance")
else:
    if withdrawal_balance % 500 == 0 :
        print("Withdrawal Successful")
    else:
        print("Amount must be multiple of 500")