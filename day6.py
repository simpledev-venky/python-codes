# working with sets

set1 = {1,2,3,4}
set2 = {4,5,6}
# print(set1.symmetric_difference(set2))

print(3 in set1)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


li=[1,1,2,2,3]
new_set = set(li)
print(list(new_set))
print(tuple(new_set))

li2 = []
for i in new_set:
   li2.append(i)
print(li2)


set1 ={1,2,3}
set2 = {4,5,6}
print(len(set1))
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))


set1 = {1,2,3}

for i in set1:
    set1.remove(i)
print(set1)


def greet():
    return "hello,world"
print(greet())

def greet(name):
    return f"hello {name}! ,welcome"
print(greet("wandel"))

def add(a,b):
    return a+b
print(add(1,2))




def greet(name="wandel"):
    print(f'hello {name},good morning')
greet("samantha")
greet()


def sum(a,b,c,d):
    return a+b+c+d
print(sum(1,2,3,4))



def square(n):
    def multiply(i):
        return i*i
    return multiply(n)
print(square(25))


def square(n):
    return n*n
def square_and_double(n):
    i= square(n)
    return i*2
print(square_and_double(5))


def divide_and_remainder(a,b):
    return[a/b,a%b]
print(divide_and_remainder(2,2 ))




def add(a,b):
    return a+b
print(add(1,2))


def greet(age,name):
    return f"hello{name},you are {age} years old"
print(greet(name="wandel",age=33))

def multiply(a,b=2):
    return a*b
print(multiply(2))

cnt = 1
li = []
num = int(input("how many elemnets you wna to enter"))
for i in range(num):
    n = int(input("enrte a no"))
    li.append(n)
    cnt +=1
    if cnt==10:
        break
print(max(li))
print(min(li))
print(sum(li))


for i in range(1,11):
    if i%2==0:
        print(i)


li = [33,45,65,87,22]
li.sort() #this method doesn't return anything
print(li)
print(sorted(li)) #it return new list in asending order


sting = "i uv samntha"
print(len(sting))


n = -22
print(abs(n))
# returns the absolute value

li = [True,True,True,False]
print(all(li))
print(any(li))