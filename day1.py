print("wandel")
print(1+2)

name= input("enter your name:")
print("hello! "+name)

pi= 3.14
print(pi)

# f-strings

user_input = input("is it raining outside ? anwer true or false")
is_raining = user_input.lower() == 'true'
print(f"is it raining?{is_raining}")
print(f"datatype of is_raining:{type(is_raining)}")
print(type(is_raining))

sentence="fuk sam"
times = int(input("Enter how many times you want to print"))
print(sentence*times)

# floor division

print(4//3)
print(4%3)
print(3+3)
print(3-3)
print(3*3)

val = 2
print(val)
val = int(input("enter a integer:"))
print(val)

# BODMAS
print(10+3*2-8/4)
print(4**2+5/2*3)
print((8+4)*3/2)
print(16/4+2**3-6)
print(10-3*(4+2)/5)

str1 = 'samatha weds '
str2= 'wandel rand'
print(str1+str2)

name= input("Enter your name:")
greet = input("Enter greeting:")

print(greet+"!"+name)

word = "luv u sam "
print(word*3)

word = input("Enter word")
times = int(input("Enter no. of times"))
print(word*times)

sentence = "samntha luv u"
print(len(sentence))

input = input("enter sentencee")
print(len(input),input[-1])

str1 = "wandel"
str2= "rand"
print(str1+str2)
print(len(str1),len(str2))

word1= input("enter word 1")
word2= input("enter word 2")
print(word1+" "+word2)

word = "samantha"
print((word+' ')*3)

# pattern
for i in range(6):
    print("*"*i)

