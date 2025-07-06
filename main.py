import math

def find_factors(n):
    """Finds the factors of a number."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def find_lcm(a, b):
    """Finds the LCM of two numbers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def find_hcf(a, b):
    """Finds the HCF (GCD) of two numbers."""
    return math.gcd(a, b)

def find_product(a, b):
    """Finds the product of two numbers."""
    return a * b

def get_numbers():
    """Gets two numbers from the user."""
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter integers only.")

def get_single_number():
    """Gets a single number from the user."""
    while True:
        try:
            num = int(input("Enter the number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """Main function to run the TUI app."""
    while True:
        print("\n===== GradeMaths TUI =====")
        print("1. Find factors of a number")
        print("2. Find LCM of two numbers")
        print("3. Find HCF of two numbers")
        print("4. Find product of two numbers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num = get_single_number()
            print(f"The factors of {num} are: {find_factors(num)}")
        elif choice == '2':
            num1, num2 = get_numbers()
            print(f"The LCM of {num1} and {num2} is: {find_lcm(num1, num2)}")
        elif choice == '3':
            num1, num2 = get_numbers()
            print(f"The HCF of {num1} and {num2} is: {find_hcf(num1, num2)}")
        elif choice == '4':
            num1, num2 = get_numbers()
            print(f"The product of {num1} and {num2} is: {find_product(num1, num2)}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()