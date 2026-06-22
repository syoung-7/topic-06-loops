# Topic 06 Collaborative Assignment
# Your Name: Steve Young  
# Date: 6-22-2026

# --- STARTER CODE ---
# This function takes a number and returns its square.
def square(n):
    return n * n

# This loop calls the function for numbers 1 through 5.
for i in range(1, 6):
    result = square(i)
    print(i, "squared is", result)

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Write a second function, change the range,
# change what the function does, or add a while loop
# that lets the user keep entering numbers until they type "quit".

def cube(n):
    return n * n * n

print("\nNow showing cubes:")

for i in range(1, 6):
    result = cube(i)
    print(i, "cubed is", result)

print("\nEnter numbers to cube (type 'quit' to stop):")

while True:
    user_input = input("Enter a number: ")

    if user_input == "quit":
        break

    num = int(user_input)
    print("Cube is:", cube(num))
