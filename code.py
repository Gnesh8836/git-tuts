import random
import random

def generate_random_data(rows=10):
    """Generates a list of random numbers."""
    return [random.randint(1, 100) for _ in range(rows)]

def calculate_average(data):
    """Calculates and returns the average of the numbers."""
    return sum(data) / len(data) if data else 0

def main():
    print("Generating random numbers...")
    data = generate_random_data()
    print(f"Random Numbers: {data}")

    average = calculate_average(data)
    print(f"Average: {average}")

if __name__ == '__main__':
    main()

 # type: ignore