# Q32. Sales > 15000 kitni hain?
sales = [15000,2000,50000,22000,6000,7000,55000]
count = 0
for sale in sales:
    if sale > 15000:
        count += 1
print("Sales above 15000 : ", count)