"""
Program Name: Integer Range Table and Statistics
Author: Phuong Nguyen  
Purpose: This program generates a formatted table of integers in a specified range, 
         computes their squares and cubes, determines their parity and divisibility by 3, 
         and provides summary statistics.
"""

def main():
    try:
        # Input and validation
        start = int(input("Enter the start (lower bound): "))
        stop = int(input("Enter the stop (upper bound): "))
        step = int(input("Enter the step (positive step): "))

        if start >= stop:
            print("Error: start must be less than stop.")
            return
        if step <= 0:
            print("Error: step must be a positive integer.")
            return
    except ValueError:
        print("Error: please enter integers only.")
        return

    # Initialize statistics
    total_count = 0
    total_sum = 0
    even_count = 0
    odd_count = 0
    divisible_by_3_count = 0
    numbers = []
    
    # Header for the table
    print(f"{'n':>6}{'n^2':>12}{'n^3':>12}{'Parity':>6}{'Div3':>6}")
    print("-" * 42)

    # Generate table and calculate statistics
    for n in range(start, stop + 1, step):
        n_squared = n ** 2
        n_cubed = n ** 3
        parity = "even" if n % 2 == 0 else "odd"
        divisible_by_3 = "yes" if n % 3 == 0 else "no"

        # Print the row
        print(f"{n:6d}{n_squared:12d}{n_cubed:12d} {parity:<4} {divisible_by_3:<3}")

        # Update statistics
        total_count += 1
        total_sum += n
        numbers.append(n)
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if n % 3 == 0:
            divisible_by_3_count += 1

    # Summary statistics
    min_value = min(numbers)
    max_value = max(numbers)
    mean_value = total_sum / total_count

    print("\nSummary Statistics:")
    print(f"Total count: {total_count}")
    print(f"Min: {min_value}, Max: {max_value}")
    print(f"Sum: {total_sum}")
    print(f"Mean: {mean_value:.2f}")
    print(f"Evens: {even_count}, Odds: {odd_count}, Divisible by 3: {divisible_by_3_count}")

if __name__ == "__main__":
    main()