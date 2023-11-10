import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius * radius

# Get the radius of the circle from the user any number you want 
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = calculate_area(radius)

# Print the computed area
print("The area of the circle is:", area)