import math
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

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
            num1 = int(Prompt.ask("[bold cyan]Enter the first number[/bold cyan]"))
            num2 = int(Prompt.ask("[bold cyan]Enter the second number[/bold cyan]"))
            return num1, num2
        except ValueError:
            print("[bold red]Invalid input. Please enter integers only.[/bold red]")

def main():
    """Main function to run the TUI app."""
    console.print(Panel("[bold green]===== GradeMaths TUI =====[/bold green]", expand=False))
    num1, num2 = get_numbers()

    while True:
        console.print(Panel(f"[bold yellow]Numbers are: {num1}, {num2}[/bold yellow]", expand=False))
        
        menu = """
[bold]What would you like to do?[/bold]
1. Find factors of both numbers
2. Find LCM of the numbers
3. Find HCF of the numbers
4. Find product of the numbers
5. Enter two new numbers
6. Exit
        """
        console.print(Panel(menu, title="[bold blue]Menu[/bold blue]", expand=False))

        choice = Prompt.ask("[bold cyan]Enter your choice (1-6)[/bold cyan]")

        if choice == '1':
            console.print(Panel(f"The factors of {num1} are: {find_factors(num1)}\nThe factors of {num2} are: {find_factors(num2)}", title="[bold green]Factors[/bold green]"))
        elif choice == '2':
            console.print(Panel(f"The LCM of {num1} and {num2} is: {find_lcm(num1, num2)}", title="[bold green]LCM[/bold green]"))
        elif choice == '3':
            console.print(Panel(f"The HCF of {num1} and {num2} is: {find_hcf(num1, num2)}", title="[bold green]HCF[/bold green]"))
        elif choice == '4':
            console.print(Panel(f"The product of {num1} and {num2} is: {find_product(num1, num2)}", title="[bold green]Product[/bold green]"))
        elif choice == '5':
            num1, num2 = get_numbers()
        elif choice == '6':
            print("[bold yellow]Exiting...[/bold yellow]")
            break
        else:
            print("[bold red]Invalid choice. Please enter a number between 1 and 6.[/bold red]")

if __name__ == "__main__":
    main()