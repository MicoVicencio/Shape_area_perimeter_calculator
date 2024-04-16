import math

# Define a class called SHAPE_CALCULATOR
class SHAPE_CALCULATOR:
    
    # Initialize the class with various shape parameters set to None initially
    def __init__(self,
                 square_side_length=None,  # Length of the square's side
                 rectangle_length=None,  # Length of the rectangle
                 rectangle_width=None,  # Width of the rectangle
                 circle_radius=None,  # Radius of the circle
                 circle_diameter=None,  # Diameter of the circle
                 triangle_base=None,  # Base length of the triangle
                 triangle_height=None,  # Height of the triangle
                 polygon_sides=None,  # Number of sides of the polygon
                 polygon_side_length=0.0,  # Length of each side of the polygon
                 polygon_n_sides=0,  # Number of sides for the polygon
                 polygon_apothem=None,  # Apothem of the polygon
                 square_area=None,  # Area of the square
                 square_perimeter=None,  # Perimeter of the square
                 triangle_area=None,  # Area of the triangle
                 triangle_perimeter=None,  # Perimeter of the triangle
                 rectangle_area=None,  # Area of the rectangle
                 rectangle_perimeter=None,  # Perimeter of the rectangle
                 polygon_area=None,  # Area of the polygon
                 polygon_perimeter=None,  # Perimeter of the polygon
                 circle_area=None,  # Area of the circle
                 circle_circumference=None  # Circumference of the circle
                 ):
        # Assign all the parameters to respective attributes of the class
        self.circle_circumference = circle_circumference
        self.circle_area = circle_area
        self.polygon_perimeter = polygon_perimeter
        self.polygon_area = polygon_area
        self.rectangle_perimeter = rectangle_perimeter
        self.rectangle_area = rectangle_area
        self.square_area = square_area
        self.square_perimeter = square_perimeter
        self.triangle_area = triangle_area
        self.triangle_perimeter = triangle_perimeter
        self.square_side_length = square_side_length
        self.rectangle_length = rectangle_length
        self.rectangle_width = rectangle_width
        self.circle_radius = circle_radius
        self.circle_diameter = circle_diameter
        self.triangle_base = triangle_base
        self.triangle_height = triangle_height
        self.polygon_sides = polygon_sides
        self.polygon_side_length = polygon_side_length
        self.polygon_n_sides = polygon_n_sides
        self.polygon_apothem = polygon_apothem
    
    # Method to calculate the area of a square
    def C_square_area(self):
        self.square_side_length = float(input("Enter the side Length of the Square:"))
        self.square_area = self.square_side_length ** 2
        print(f"The Area of the square is {self.square_area}.")
        print()
        
    # Method to calculate the perimeter of a square
    def C_square_perimeter(self):
        self.square_side_length = float(input("Enter the side Length of the Square:"))
        self.square_perimeter = 4 * self.square_side_length
        print(f"The Perimeter of the square is {self.square_perimeter}.")
        print()
        
    # Method to calculate the area of a rectangle
    def C_rectangle_area(self):
        self.rectangle_length = float(input("Enter the length of the Rectangle:"))
        self.rectangle_width = float(input("Enter the width of the Rectangle:"))
        self.rectangle_area = self.rectangle_length * self.rectangle_width
        print(f"The Area of the rectangle is {self.rectangle_area}.")
        print()
        
    # Method to calculate the perimeter of a rectangle
    def C_rectangle_perimeter(self):
        self.rectangle_length = float(input("Enter the length of the Rectangle:"))
        self.rectangle_width = float(input("Enter the width of the Rectangle:"))
        self.rectangle_perimeter = 2 * (self.rectangle_length + self.rectangle_width)
        print(f"The Perimeter of the Rectangle is {self.rectangle_perimeter}.")
        print()
        
    # Method to calculate the area of a circle
    def C_circle_area(self):
        self.circle_radius = float(input("Enter the Radius of the Circle:"))
        self.circle_area = math.pi * self.circle_radius ** 2
        print(f"The Area of the circle is {self.circle_area}.")
        print()
        
    # Method to calculate the circumference of a circle
    def C_circle_circumference(self):
        self.circle_radius = float(input("Enter the Radius of the Circle:"))
        self.circle_perimeter = 2 * math.pi * self.circle_radius
        print(f"The Perimeter of the Circle is {self.circle_perimeter}.")
        print()
        
    # Method to calculate the area of a triangle
    def C_triangle_area(self):
        self.triangle_base = float(input("Enter the base of the Triangle:"))
        self.triangle_height = float(input("Enter the Height of the Triangle:"))
        self.triangle_area = 0.5 * self.triangle_base * self.triangle_height
        print(f"The Area of the Triangle is {self.triangle_area}.")
        print()
        
    # Method to calculate the perimeter of a triangle
    def C_triangle_perimeter(self):
        sideA = float(input("Enter the Side A Length of the Triangle:"))
        sideB = float(input("Enter the Side B Length of the Triangle:"))
        sideC = float(input("Enter the Side C Length of the Triangle:"))
        self.triangle_perimeter = sideA + sideB + sideC
        print(f"The Perimeter of the Triangle is {self.triangle_perimeter}.")
        print()
        
    # Method to calculate the area of a polygon
    def C_polygon_area(self):
        self.C_polygon_perimeter()
        self.polygon_apothem = self.polygon_side_length * 0.5 * (3 ** 0.5)
        self.polygon_area = 0.5 * self.polygon_perimeter * self.polygon_apothem
        print(f"The Area of the Polygon is {self.polygon_area}.")
        print()
        
    # Method to calculate the perimeter of a polygon
    def C_polygon_perimeter(self):
        self.polygon_n_sides = int(input("Enter the Number of the sides of the polygon:"))
        self.polygon_side_length = float(input("Enter the length of the Side:"))
        self.polygon_perimeter = self.polygon_side_length * self.polygon_n_sides
        print(f"The Perimeter of the Polygon is {self.polygon_perimeter}.")
        print()
        return self.polygon_perimeter
    
    # Method to display the main shape choice menu
    def shape_choice_menu(self):
        while True:
            print("Welcome to Shape Calculator")
            print("Available Shapes that can be calculated:")
            print("1. Square")
            print("2. Circle")
            print("3. Rectangle")
            print("4. Polygon")
            print("5. Triangle")
            print("6. Exit")
            choice = input("Enter your choice 1-6:")
            if choice == '1':
                self.square_menu()
                break
            elif choice == '2':
                self.circle_menu()
                break
            elif choice == '3':
                self.rectangle_menu()
                break
            elif choice == '4':
                self.polygon_menu()
                break
            elif choice == '5':
                self.triangle_menu()
                break
            elif choice == '6':
                print("The program will now exit!")
                break
            else:
                print("Invalid Selection! Try Again.")
                print()
                
    # Method to display the square-specific menu
    def square_menu(self):
        while True:
            print("Square Calculator")
            print("This Calculator can calculate the Area and Perimeter of the Square")
            print("1. Area")
            print("2. Perimeter")
            print("3. Return to the Main Menu")
            choice = input("Enter your choice 1-3:")
            if choice == '1':
                self.C_square_area()
            elif choice == '2':
                self.C_square_perimeter()
            elif choice == '3':
                self.shape_choice_menu()
                break
            else:
                print("Invalid Choice! Try Again.")
                print()
            
    # Method to display the circle-specific menu
    def circle_menu(self):
        while True:
            print("Circle Calculator")
            print("This Calculator can calculate the Area and Perimeter of the Circle")
            print("1. Area")
            print("2. Circumference")
            print("3. Return to the Main Menu")
            choice = input("Enter your choice 1-3:")
            if choice == '1':
                self.C_circle_area()
            elif choice == '2':
                self.C_circle_circumference()
            elif choice == '3':
                self.shape_choice_menu()
                break
            else:
                print("Invalid Choice! Try Again.")
                print()
                
    # Method to display the triangle-specific menu
    def triangle_menu(self):
        while True:
            print("Triangle Calculator")
            print("This Calculator can calculate the Area and Perimeter of the Triangle")
            print("1. Area")
            print("2. Perimeter")
            print("3. Return to the Main Menu")
            choice = input("Enter your choice 1-3:")
            if choice == '1':
                self.C_triangle_area()
            elif choice == '2':
                self.C_triangle_perimeter()
            elif choice == '3':
                self.shape_choice_menu()
                break
            else:
                print("Invalid Choice! Try Again.")
                print()
                
    # Method to display the rectangle-specific menu
    def rectangle_menu(self):
        while True:
            print("Rectangle Calculator")
            print("This Calculator can calculate the Area and Perimeter of the Rectangle")
            print("1. Area")
            print("2. Perimeter")
            print("3. Return to the Main Menu")
            choice = input("Enter your choice 1-3:")
            if choice == '1':
                self.C_rectangle_area()
            elif choice == '2':
                self.C_rectangle_perimeter()
            elif choice == '3':
                self.shape_choice_menu()
                break
            else:
                print("Invalid Choice! Try Again.")
                print()
                
    # Method to display the polygon-specific menu
    def polygon_menu(self):
        while True:
            print("Polygon Calculator")
            print("This Calculator can calculate the Area and Perimeter of the Polygon")
            print("1. Area")
            print("2. Perimeter")
            print("3. Return to the Main Menu")
            choice = input("Enter your choice 1-3:")
            if choice == '1':
                self.C_polygon_area()
            elif choice == '2':
                self.C_polygon_perimeter()
            elif choice == '3':
                self.shape_choice_menu()
                break
            else:
                print("Invalid Choice! Try Again.")
                print()


# Create an instance of the SHAPE_CALCULATOR class
x = SHAPE_CALCULATOR()
# Call the shape choice menu to start the calculator
x.shape_choice_menu()
