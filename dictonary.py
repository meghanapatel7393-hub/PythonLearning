student = {
    "name": "Bhavesh",
    "age": 22,
    "course": "Python"
}

print(student["name"])
print(student["age"])
# ✔ Best way (safe):
print(student.get("course"))

# 3️⃣ Modifying Dictionary
student["age"] = 23
student["city"] = "Ahmedabad"

# 4️⃣ Removing Data
student.pop("city")

# 5️⃣ Looping Through Dictionary
# Keys
for key in student:
    print(key)
# Values
for value in student.values():
    print(value)
# Key + Value
for key, value in student.items():
    print(key, ":", value)

# 📘 Real Example: Student Record
student = {}

student["name"] = input("Enter name: ")
student["roll"] = int(input("Enter roll: "))
student["marks"] = int(input("Enter marks: "))

if student["marks"] >= 40:
    student["result"] = "Pass"
else:
    student["result"] = "Fail"

print(student)

# print(student["phone"])  # Error

print(student.get("phone")) #None



