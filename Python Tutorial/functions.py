# Function definition
def print_hello():
    print("Hello")

# Function definition with arguments
def print_var(x):
    print("x = ", x)

# Function with return value
def summer(a, b):
    return a + b

# Function with type hints
def add_two(a: int, b: int) -> int:
    return a + b

# Function calls
print_hello()
print_var(5)
result = summer(2, 3)
print("Sum = ", result)
print("Sum = ", add_two(2, 3))

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    """Returns volume of a cylinder given radius, height."""
    pi = 3.14159
    volume = pi * radius * radius * height
    return volume

# Main function
def main():
    print("This is the main function")

    six_pack_volume = cylinder_volume(2.5, 5) * 6
    print(f'Six pack volume: {six_pack_volume}')

if __name__ == "__main__":
    main()
