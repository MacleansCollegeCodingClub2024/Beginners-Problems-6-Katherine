def triangleTest(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b > c:
        return True 
    else:
        return False  
        
        
        
        
def greet_user():
    name = input("Please enter your name: ")

    time = int(input("Please enter the current time (0-23): "))

    if 0 <= time <= 12:
        print(f"Good morning, {name}!")
    elif 13 <= time <= 17:
        print(f"Good afternoon, {name}!")
    elif 18 <= time <= 23:
        print(f"Good evening, {name}!")
    else:
        print("Invalid time entered. Please enter a time between 0 and 23.")

greet_user()



def getEven(numbers):
    
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

numbers = list(map(int, input("Please enter a list of integers, separated by spaces: ").split()))

print(getEven(numbers))
