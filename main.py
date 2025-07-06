import math

def find_factors(n):
    """Finds the factors of a number."""
    factors = []
    if n <= 0:
        return factors
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


def main():
    """Main function to run the TUI app."""
    print("===== GradeMaths TUI =====")
    num1, num2 = get_numbers()

    while True:
        print(f"\nNumbers are: {num1}, {num2}")
        print("\nWhat would you like to do?")
        print("1. Find factors of both numbers")
        print("2. Find LCM of the numbers")
        print("3. Find HCF of the numbers")
        print("4. Find product of the numbers")
        print("5. Enter two new numbers")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(f"The factors of {num1} are: {find_factors(num1)}")
            print(f"The factors of {num2} are: {find_factors(num2)}")
        elif choice == '2':
            print(f"The LCM of {num1} and {num2} is: {find_lcm(num1, num2)}")
        elif choice == '3':
            print(f"The HCF of {num1} and {num2} is: {find_hcf(num1, num2)}")
        elif choice == '4':
            print(f"The product of {num1} and {num2} is: {find_product(num1, num2)}")
        elif choice == '5':
            num1, num2 = get_numbers()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()