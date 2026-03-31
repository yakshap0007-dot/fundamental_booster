print("hello sir, welcome ! please enter your detail in below \n")

name = str(input("enter your name :"))
age = int(input("enter your age :"))
height = float(input("enter your height :"))
favourite_number = int(input("enter your favourite nummber :"))

# operator = input("enter the operator ( - ):")
running_year = 2026
# age = int(input("enter the age:"))
your_birth_year = running_year - age
print(your_birth_year)

print("your birth year is approximately:",your_birth_year)

print("name:", name , ("type:",type(name), "memory address:",id(name)))
print("age:",age , ("type:",type(age), "memory address:",id(age)))
print("height:",height , ("type:",type(height), "memory address:",id(height)))
print("favourite_number:",favourite_number , ("type:",type(favourite_number), "memory address:",id(favourite_number)))

print("Thank you sir ! for your detail . ")
