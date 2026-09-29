import math

# Function to calculate the area of a square
def calculate_square_area(side):
    area = side * side
    return area


# Function to calculate the perimeter of a square
def calculate_square_perimeter(side):
    perimeter = 4 * side
    return perimeter

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area


# Function to calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area


# Function to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def display_menu():
    while True:
        print("Menu:")
        print("1. Square")
        print("2. Triangle")
        print("3. Circle")
        print("0. Exit")
        choice = input("Enter your choice (0-3): ")

        if choice == "1":
            side = float(input("Enter the length of a side: "))
            square_area = calculate_square_area(side)
            square_perimeter = calculate_square_perimeter(side)
            print("Square area:", square_area)
            print("Square perimeter:", square_perimeter)

        elif choice == "2":
            base = float(input("Enter the length of the base: "))
            height = float(input("Enter the height: "))
            triangle_area = calculate_triangle_area(base, height)
            side1 = float(input("Enter the length of side 1: "))
            side2 = float(input("Enter the length of side 2: "))
            side3 = float(input("Enter the length of side 3: "))
            triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)
            print("Triangle area:", triangle_area)
            print("Triangle perimeter:", triangle_perimeter)

        elif choice == "3":
            radius = float(input("Enter the radius: "))
            circle_area = calculate_circle_area(radius)
            circle_circumference = calculate_circle_circumference(radius)
            print("Circle area:", circle_area)
            print("Circle circumference:", circle_circumference)

        elif choice == "0":
            print("Thank you for using this program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")


        print()  # Add an empty line to separate output

print("=== 2D Figure Calculators ===")
display_menu()