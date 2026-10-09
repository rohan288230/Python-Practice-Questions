# Q9. Write a function is_prime(n) that returns True if n is a prime number
# and False otherwise, using a LookupError.
# [ -Hint
# 1. We only check prime for 2 or numbers greater than 2. is the smallest
# prime number.
# 2
# 2. A number, , will always get divided by atleast one number in
# range [2, n-1].
# non-Prime n
# Eg - For number weʼll check in range (2, 8) & itʼll get divided by 3. So is
# non-prime & weʼll return false for it.
# 9 9
# For number weʼll check in range (2, 6) & it wonʼt get divided by any. So
# is prime & weʼll return true for it.
def is_prime(n):
    if n<2:
        return False
    for num in range(2,n-1):
        if n % num == 0:
            return False
    return True

num = int(input("Enter a number : "))
print("The number is prime : ",is_prime(num))