# Q34. Profit aur Loss transactions count karo
profits = [500,-5000,10000,-600,800,-900,-6000,15000]
profit_count = 0
loss_count = 0
for profit in profits:
    if profit > 0:
        profit_count += 1
    elif profit < 0:
        loss_count += 1
print("Profit Transactions : ", profit_count)
print("Loss Transactions : ", loss_count)
