# i= 2
# while i<=10:
#     print(i)
#     i+=2

# n = int(input("entr a negative no"))

# while n>0:
#     i = int(input("entr a no"))
#     if i<0:
#         break

# i = 10
# while i>=1:
#     print(i)
#     i-=1


# guessing secret no
# n = int(input("entr a no"))
# while n!=7:
#     print("not correct")
#     n=int(input("enter a no"))
#     if n==7:
#         print("correct")
#         break

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


# factorial fo a no
'''
n= int(input("entre a no to cal fact:"))
def fact(n):
    if n<0:
        return "enter a positve"
    elif n==0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *=i
        return result
    
print(fact(n))
'''
# result = 0
# while True:
#    n = int(input("enter no"))
#    if n==0:
#         break
#    else:
#        result +=n
# print(result)

# for i in range(1,6):
#     print(i)

# n= int(input("no"))
# print(n*(n+1)/2)

# for i in range(0,19,2):
#     print(i)
    

# string = input(":")
# string = "hello world"
# print(string.lower())
# print(len(string))
# print(string.upper())
# string = "abv123"
# print(string.isalpha())
# print(string.isdigit())
# print(string.isalnum())

# string = input(":")
# print(string.strip())
# print(string.rstrip())

# string = "l-luv- python"
# print(string.split("-"))
# print(string.split(" "))
# print(string.replace("python","java"))

# string = "hello world"
# print(string.startswith("hello"))
# print(string.endswith("hello"))
# print(string.endswith("ld"))

# string = "banana"
# print(string.count("a"))
# print(string.count("an"))
# print(string.count("ban"))

# string= "hello world"
# print(string.find("llo"))
# print(string.find("llp"))

