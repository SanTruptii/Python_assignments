# Function to print lower triangular pattern
def print_lower_triangular(n):
    # Loop through rows
    for i in range(1, n + 1):
        # Print '*' i times in each row
        print('*' * i)

# Function to print upper triangular pattern
def print_upper_triangular(n):
    # Loop through rows
    for i in range(n, 0, -1):
        # Print '*' i times in each row
        print('*' * i)

# Function to print pyramid pattern
def print_pyramid(n):
    # Loop through rows
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Main function to call the pattern functions
def main():
    # Number of rows
    n = 5
    
    # Print lower triangular pattern
    print("Lower Triangular Pattern:")
    print_lower_triangular(n)
    print()  

    # Print upper triangular pattern
    print("Upper Triangular Pattern:")
    print_upper_triangular(n)
    print() 

    # Print pyramid pattern
    print("Pyramid Pattern:")
    print_pyramid(n)

# Run the main function
if __name__ == "__main__":
    main()
