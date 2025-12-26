print("Hello, Python!")

name = "Meghana"
age = 22
height = 5.4
is_student = True

print(name)
print(age)
name = input("Enter your name: ")
print("Welcome,", name)


name = input("Enter your name: ")
age = input("Enter your age: ")

print("My name is", name)
print("My age is", age)


num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(5):
    print("Hello")



for i in range(1, 6):
    print(i)

    i = 1

while i <= 5:
    print(i)
    i = i + 1

for i in range(1, 10):
    if i == 5:
        break
    print("break",i)


for i in range(1, 6):
    if i == 3:
        continue
    print("continue",i)

    
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

for i in range(6, 0, -1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()
    

    names = ["Bhavesh", "Amit", "Neha"]

print(names[0])  # Bhavesh
print(names[1])  # Amit
print(names[2])  # Neha
print(names[-1])  # Neha

marks = []
for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

print("All marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))

