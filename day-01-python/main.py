print("Hello world")
name="Maher"
age=20
goal ="AI/ML Engineer"
print(name,goal)
name=input("Enter your name")
print(name,"iiiss")

age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote")
elif age==17:
    print("You are not eligible to vote but you can apply for voter ID")
else:
    print("You are not eligible to vote")

for i in range(0,11):
    print(i)

number=1
while number<=10:
    print(number)
    number+=1

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
numbers.append(25)
print(numbers)
for number in numbers:
    print("ami",number)

total=0
for number in numbers:
    total+=number
print("Total:",total)

student = {
    "name": "Maher",
    "age": 22,
    "goal": "AI/ML Engineer"
}
print(student["name"])
print(student["age"])
print(student["goal"])
def greet(name):
    print("Hello", name)

greet("Maher")

def add(a,b):
    return a+b
result=add(5,10)
print("Result:", result)
           Even or Odd Number Checker
number=int(input("Enter a number:"))
if number%2==0:
    print(number,"The number is even")
else:
    print(number,"The number is odd")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
    print(num1,"is the largest number")
elif num2>num1 and num2>num3:
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")
sum=0
for i in range(1,100):
    sum+=i
print(sum)
fact=1;
number=int(input("Enter a number:"))
for i in range(number,1,-1):
    fact*=i
print("Factorial of",number,"is",fact)

numbers=[12,7,8,15,20,33,42,51]
evn=0;
for number in numbers:
    if number%2==0:
        evn+=1
print("Total even numbers:",evn)
