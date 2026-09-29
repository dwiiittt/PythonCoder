#### QUESTION 1 ####
#Empty bucket
bucket = []

bucket.append("Apple")
bucket.append("Banana")
bucket.append("Milk")
bucket.append("Bread")
bucket.append("Eggs")

#Show items inside bucket
print(bucket)


#### QUESTION 2 ####
# Ask the user to input their age
age = int(input("Enter your age: "))

# Classify the member based on age range
if age < 18:
    print("You belong to the Teenager category.")
elif age >= 18 and age <= 30:
    print("You belong to the Young Adult category.")
else:
    print("You belong to the Adult category.")


#### QUESTION 3 ####
def calculate_triangle_area(base, height):
    # Calculate the area of the triangle using the base and height
    area = (base * height) / 2
    return area

def main():
    # Print program header
    print("Triangle Area Calculation Program")
    print("--------------------------------")

    # Prompt the user to enter the base and height of the triangle
    base = float(input("Enter the length of the base: "))
    height = float(input("Enter the height: "))

    # Call the calculate_triangle_area() function to calculate the area
    area = calculate_triangle_area(base, height)

    # Print the result
    print("The area of the triangle is", area)

# Call Function
main()