# n = 5  # Number of rows

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("5", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 
# for i in range(0,5):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# n = 5

# for i in range(1,n+1):
#     # Print spaces
#     print(" " * (n - i), end="")

#     # Print ascending numbers
#     for k in range(1,i+1):
#         print(k, end="")

#     # Print descending numbers
#     for l in range(i-1,0,-1):
#         print(l, end="")

#     # Move to the next line
#     print()

# n = 5

# Upper half of the diamond
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for k in range(1, i * 2):
#         print(k, end="")
#     print()

# # Lower half of the diamond
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for k in range(1, i * 2):
#         print(k, end="")
#     print()

# l=["mani","deep"]
# print(l[1][-1])


# This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")

# def add(x,y):
#     return x+y
      
# def sub(x,y):
#     return x-y
      
# def mul(x,y):
#     return x*y
      
# def div(x,y):
#     return x/y

# print("Select operation")
# print("1.add")
# print("2.sub")
# print("3.mul")
# print("4.div")

# while True:
#     choice=input("Select any operation(1/2/3/4):")
#     if choice in('1','2','3','4'):
#         try:
#             n1=float(input('Enter first number:'))
#             n2=float(input('Enter Second number:'))
#         except ValueError:
#             print("Invalid input")
#         if choice == '1':
#             print(n1,"+",n2,"=",add(n1,n2))
#         elif choice == '2':
#             print(n1,"-",n2,"=",sub(n1,n2))
#         elif choice == '3':
#             print(n1,"*",n2,"=",mul(n1,n2))
#         elif choice == '4':
#             print(n1,"/",n2,"=",div(n1,n2))
#         else:
#             ("invalid input")

s="python"
print((s+' ')*4)      
 
# l=["refr","efrf","frrevre","ferevr","frfrfr"]
# print(l[2][-1])

# a=input('Enter number 1:')
# b=input('Enter number 2:')
# if(a>b):
#     print(a,"is maximum")
# else:
#     print(b,"is maximum")

# a,b=input().split()
# if a>b:
#     print(a,"is maximum")
# else:
#     print(b,"is maximum")

# a=input('Enter:')
# if a in 'aeiouAEIOU':
#     print(a,"is vowel")
# else:
#     print(a,"is not a vowel")


# name,age=input().split()
# ag=int(age)
# print(name,ag)

# i=0
# while i<=4:
#     print("python")
#     i+=1


# for n in range(1,20):
#     if n%2==0:
#         print(n,"i even")
#     else:
#         print(n,"is odd")
# a=1
# for i in range(2):
#     for j in range(3):
#         print(a,end="")
#     print()
#     a+=1

# same code
# for i in range(2):
# #     for j in range(3):
#         print(i,end="")
#     print()

# a=1
# for i in range(5):
#     for j in range(5):
#         print(a,end="")
#     print("\r")
#     a+=1

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end="")
#         if j==3:
#             break
#     if i==3:
#         break
#     print()

# for i in range(1,10):
#     if i==5:
#         print("continue")
#         continue
#     else:
#         print(i)

# a=int(input())
# b=int(input())
# g=max(a,b)
# while True:
#     if(g%a==0) and (g%b==0):
#         print(g)
#         break
#     g+=1


