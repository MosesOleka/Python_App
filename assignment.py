name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0 or age > 18:
    print("Invalid age entered!")
else:
    print(name + ", you are " + str(age) + " years old.")
