

def get_user_input():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    return a, b

def calculate_sum(a, b):
    return a + b

if __name__ == "__main__":
    a, b = get_user_input()
    result = calculate_sum(a, b)
    print(f"The sum of {a} and {b} is {result}")