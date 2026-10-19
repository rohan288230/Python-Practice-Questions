# Q25. 1–20 print karo, lekin multiples of 3 skip karo
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
