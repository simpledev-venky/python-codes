# sum of n numbers
"""
print(n*(n+1)/2)
"""

# leap year
'''
year = int(input("entr year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("not a leap year") 
'''

# vowel or not
'''
# c = input("enter charater")
# if c in "aeiouAEIOU":
#     print("VOWEL")
# else:
#     print("consonant")
'''

# lcm
'''
a= int(input("entr a no"))
b= int(input("entr a no"))
big = max(a,b)

while True:
    if big%a==0 and big%b==0:
       print("lcm:",big)
       break
    big+=1
'''

# factorial of num
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
print(fact(0))
print(fact(1))
'''

# even or not
'''
n =27
def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(n)
'''


# fibnocci numbers printing
"""
fib_series = [0,1]

def fib(n):
    if n<0:
        print("enter positive")
    elif n==1:
        return [0]
    elif n==2:
        return fib_series
    else:
        for i in range(2,n):
            next_num = fib_series[-1]+fib_series[-2]
            fib_series.append(next_num)
        return fib_series
n = int(input("enter a no of terms for fibnnoci"))
print(fib(n))
"""

# prime num or not
'''
n = int(input("enter a num"))
cnt = 0
for i in range(2,n):
    if n%i==0:
        cnt+=1
if cnt==0:
    print("prime")
else:
    print("not prime")
'''

# palindrome or not
'''
n = input("entre  sting: ")
string = n.lower()
rev_str = string[::-1]
if string==rev_str:
    print("palindrome")
else:
    print("not a palindrome")

'''

# sorting
'''
li = [1,3,12,11,4]
print(sorted(li))
'''

# ASCII Number
print(ord('A'))

# ASCII Character
print(chr(65))
