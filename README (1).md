z                                                                       # 🧑‍💻 Python Personal Data Collector

This is a simple Python program that collects user input and displays
details like name, age, height, and favourite number along with their
data types and memory addresses.

------------------------------------------------------------------------

## 📌 Features

-   Takes user input:
    -   Name
    -   Age
    -   Height
    -   Favourite Number
-   Calculates birth year
-   Displays:
    -   Value
    -   Data Type
    -   Memory Address

------------------------------------------------------------------------

## 🧾 Code

``` python
name = str(input("enter your name: "))
age = int(input("enter your age: "))
height = float(input("enter your height: "))
favourite_number = int(input("enter your favourite number: "))

running_year = 2026

your_birth_year = running_year - age
print("your birth year is approximately:", your_birth_year)

print("name:", name, "(type:", type(name), "memory address:", id(name))
print("age:", age, "(type:", type(age), "memory address:", id(age))
print("height:", height, "(type:", type(height), "memory address:", id(height))
print("favourite_number:", favourite_number, "(type:", type(favourite_number), "memory address:", id(favourite_number))
```

------------------------------------------------------------------------

## 🚀 How to Run

``` bash
python project1.py
```

------------------------------------------------------------------------

## 👨‍💻 Author

Yaksha Patel
