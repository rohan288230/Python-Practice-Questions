# Q39. Duplicate values
# numbers = [10, 20, 10, 30, 20, 40, 10]
# Har number kitni baar appear hua, find karo.
# 10 → 3
# 20 → 2
# 30 → 1
# 40 → 1
# Isme nested loop useful ho sakta hai.
numbers = [10, 20, 10, 30, 20, 40, 10]
for num in numbers:
    count = 0
    for value in numbers:
        if value == num:
            count+=1
    print(num,"-",count)