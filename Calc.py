import math, cmath, textwrap, warnings, random
import sympy as sp
from spellchecker import SpellChecker

spell = SpellChecker()

a = sp.symbols('a')
x = sp.symbols('x')
b = sp.symbols('b')
c = sp.symbols('c')
m = sp.symbols('m')

expr = a * x ** 2 + b * x + c
y = m * x + b

letters = []
count = 0
equals = "="

warnings.filterwarnings("ignore")
errors = (ValueError, TypeError, NameError, SyntaxError)

def Errors():
    print("Undefined")
def base(length, errors):
    width = input("Enter the width: ")
    hieght = input("Enter the height: ")
    
    try:
        base = float(width) * float(hieght) * float(length)
        print(base)
    except (errors):
        print('Undefind')
def Hexagon(x, length):
    try:
        math_stuff = 3 * math.sqrt(3) / 2
        area_2 = math_stuff * float(x) ** 2 * float(length)
        print(area_2)
    except (TypeError, NameError, ValueError):
        print('Undefined')
def cube_surface(errors):
    width = input("Enter the width: ")
    hieght = input("Enter the hieght: ")
            
    try:
        area = float(width) * float(hieght)
        surface_area = area * 6
        print(surface_area)
    except (errors):
        print('Undefined')

option_text = "Enter a operation or if you don't know what one is type help for a list of all operations in this program: "
list_text = "calc, pow, sqrt, distance, pythagorean theorem, area, temp converter, weight on earth, quadratic formula, slope-intercept, percentage, spellcheck and spelling corrections/word counter, volume, surface area, random number generator, simp algebra"
List_of_3D_shapes = "Cube, Rectangel, Sphere, Cylinder, Cone, Triangular prism, Octagonal prism, Trapezoidal prism"
list_of_shapes = "Circle, Rectangle, Triangle, Trapezoid, Ellipse, Regular Hexagon, Kite, Equilateral Triangle, Annulus, Circular Sector"
area_text = "Enter a shape if you dont know the name of one then type (list of shapes) for a list of shapes after this you will be sent back to choose a operator: "
circular_sector = "How many digrees of the sector are there?: "

while True:
    print()
    operation = input(textwrap.fill(option_text, width=34))
    print()

    if operation.capitalize() == "Calc":
        try:
            print(eval(input('>>>>')))
        except (errors):
            Errors()

    elif operation.capitalize() == "Pow":
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        
        try:
            result = pow(float(num1), float(num2))
            print(result)
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Sqrt":
        num1 = input("Enter a number: ")
        
        try:
            result = cmath.sqrt(float(num1))
            print(result)
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Distance":
        first_x_value = input("Enter the first X value: ")
        second_x_value = input("Enter the second X value: ")
        
        try:
            result_one = float(first_x_value) - float(second_x_value)
            result_one_two = result_one ** 2
        except (errors):
            Errors()
        
        first_y_value = input("Enter the first Y value: ")
        second_y_value = input("Enter the second Y value: ")
        
        try:
            result_two = float(first_y_value) - float(second_y_value)
            result_two_two = result_two ** 2
            
            result = result_one_two + result_two_two
            print(result)
        except(errors):
            Errors()
            
    elif operation.capitalize() == "Pythagorean theorem":
        a = input("Enter side a: ")
        b = input("Enter side b:")
        
        try:
            c_squared = float(a) ** 2 + float(b) ** 2
            c = cmath.sqrt(c_squared)
            print(c)
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Area":
            shape = input(textwrap.fill(area_text, width=37))
            print()
            
            if shape.capitalize() == "Circle":
                radius = input("Enter the radius: ")
                
                try:
                    area = float(radius) ** 2 * math.pi
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Rectangle":
                length = 1
                
                base(length, errors)
                    
            elif shape.capitalize() == "Triangle":
                base = input("Enter the base: ")
                hieght = input("Enter the hieght: ")
                
                try:
                    num1 = float(base) * float(hieght)
                    area = num1 / 2
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Trapezoid":
                    length1 = input("Enter the length of the top line: ")
                    lenght2 = input("Enter the length of the bottom line: ")
                    
                    try:
                        length = float(length1) + float(length2)
                        num1 = length / 2
                    except (errors):
                        Errors()
                    
                    height = input("Enter the hieght: ")
                    
                    try:
                        area = num1 * height
                        print(area)
                    except (errors):
                        Errors()
                        
            elif shape.capitalize() == "Ellipse":
                min_radius = input("Enter the min radius: ")
                max_radius = input("Enter the max radius: ")
                    
                try:
                    num = float(min_radius) * float(max_radius)
                    area = num * math.pi
                        
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Kite":
                length = input("Enter the length: ")
                width = input("Enter the width: ")
                
                try:
                    area = float(length) * float(width) / 2
                    
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Annulus":
                a = input("Enter the outer radius: ")
                b = input("Enter the inner radius: ")
                
                try:
                    num = math.pi * float(a) ** 2
                    area = num - math.pi * float(b) ** 2
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Regular hexagon":
                x = input("Enter one side length: ")
                length = 0
                
                Hexagon(x, length)
                    
            elif shape.capitalize() == "Equilateral triangle":
                side = input("Enter the length of one of the sides: ")
                
                try:
                    num = math.sqrt(3)
                    num2 = num / 4
                    area = float(side) ** 2 * num2
                    
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "Circular sector":
                degrees = input(textwrap.fill(circular_sector, width=37))
                side_length = input("What is the side length?: ")
                
                try:
                    part1 = float(side_length) ** 2 * math.pi
                    part2 = float(degrees) / 360
                    area = part1 * part2
                    
                    print(area)
                except (errors):
                    Errors()
                    
            elif shape.capitalize() == "List of shapes":
                print(textwrap.fill(list_of_shapes, width=38))
                    
            else:
                Errors()
                
    elif operation.capitalize() == "Temp converter":
        temp = input("What would you like to convert? (farenheit, celsius, kelvin): ")
        
        if temp.capitalize() == "Farenheit to celsius":
            farenheit = input("Enter the temp in farenheit: ")
            
            try:
                num = int(farenheit) + 32
                celsius_temp = num * 9 / 5
                print(f"{round(celsius_temp)} C")
            except (errors):
                Errors()
                
        elif temp.capitalize() == "Celsius to farenheit":
            celcius = input("Enter the temp in farenheit: ")
            
            try:
                temp = 9 / 5 * int(celsius) + 32
                print(f"{round(temp)} C")
            except (errors):
                Errors()
                
        elif temp.capitalize() == "Celsius to kelvin":
            celcius = input("Enter the temp in celcius: ")
            
            try:
                temp = int(celsius) + 273.15
                print(f"{temp} K")
            except (errors):
                Errors()
                
        elif temp.capitalize() == "Farenheit to kelvin":
            farenheit = input("Enter the temp in farenheit: ")
            
            try:
                celsius = int(farenheit) - 32
                celsius_temp = celsius / 1.8
                kelvin_temp = celsius_temp + 273.15
                print(f"{round(kelvin_temp,2)} K")
            except (errors):
                Errors()
                
        elif temp.capitalize() == "Kelvin to celsius":
            kelvin_temp = input("Enter the temp in Kelvin: ")
            
            try:
                celcius_temp = float(kelvin_temp) - 273.15
                print(f"{round(celsius_temp)} C")
            except (errors):
                Errors()
                
        elif temp.capitalize() == "Kelvin to farenheit":
            kelvin_temp = input("Enter the temp in Kelvin: ")
            
            try:
                celcius_temp = float(kelvin_temp) - 273.15
                farenheit_temp = 9 / 5 * int(celsius_temp) + 32
                print(f"{farenheit_temp} F")
            except (errors):
                Errors()
                
    elif operation.capitalize() == "Weight on earth":
        mass_in_g = input("Enter the mass in grams: ")
        
        try:
            mass_in_kg = float(mass_in_g) / 1000
            gravity_on_earth = 9.8 * float(mass_in_g)
            result = gravity_on_earth * mass_in_kg
            print(f"{round(result,2)}N")
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Quadratic formula":
            a_sub = input("Enter a substitute for a, if you dont have one enter a: ")
            x_sub = input("Enter a substitute for x, if you dont have one enter x: ")
            b_sub = input("Enter a substitute for b, if you dont have one enter b: ")
            c_sub = input("Enter a substitute for c, if you dont have one enter c: ")
            
            try:
                print()
                sp.pprint(sp.solve(expr.subs({a:a_sub, x:x_sub, b:b_sub, c:c_sub}), dict=True))
            except (errors):
                Errors()
                
    elif operation.capitalize() == "Slope-interrcept":
        m_sub = input("Enter a substitute for m, if you dont have one enter m: ")
        x_sub = input("Enter a substitute for x, ig you dont have one enter x: ")
        b_sub = input("Enter a substitute for b, if you dont have one enter b: ")
        
        try:
            print()
            sp.pprint(sp.solve(y.subs({m:m_sub, x:x_sub, b:b_sub}), dict=True))
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Percentage":
        Is = input("Enter percent of_: ")
        of = input("Is _: ")
        
        try:
            percentage = float(of) / float(Is) * 100
            print(f"{round(percentage)}%")
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Spellcheck and spelling corrections":
        user_text = input("Enter a word or sentence to check the spelling: ")
        
        word = user_text.split()
        words = len(word)
        misspelled_words = spell.unknown(word)
            
        if not misspelled_words:
            print("Everything is spelt correctly!")
            print(f"And there are {words} words")
        else:
            for word in misspelled_words:
                print(f"{word} ---> {spell.correction(word)}")
                
    elif operation.capitalize() == "Volume":
        print("Here is a list of what shapes this operation can calculate the volume of")
        print()
        print(textwrap.fill(List_of_3D_shapes, width=41))
        print()
        shape = input("Enter a shape from the list: ")
        
        if shape.capitalize() == "Cube":
            print()
            length = input("Enter the length: ")
            
            base(length, errors)
            
        elif shape.capitalize() == "Rectangel":
            print()
            length = input("Enter the length: ")
            
            base(length, errors)
                
        elif shape.capitalize() == "Sphere":
            radius = input("Enter the radius: ")
            
            try:
                print()
                volume = 4 / 3 * math.pi * float(radius) ** 3
                print(volume)
            except (errors):
                Errors()
        
        elif shape.capitalize() == "Cylinder":
            radius = input("Enter the radius: ")
            hieght = input("Enter the hieght: ")
            
            try:
                area = math.pi * float(radius) ** 2
                volume = area * float(hieght)
                print(volume)
            except (errors):
                Errors()
                
        elif shape.capitalize() == "Pyramid":
            width = input("Enter the width: ")
            length = input("Enter the length: ")
            hieght = input("Enter the hieght: ")
            
            base(width, hieght, length)
            
        elif shape.capitalize() == "Cone":
            print()
            radius = input("Enter the radius: ")
            hieght = input("Enter the hieght: ")
            
            try:
                volume = 1 / 3 * math.pi * float(radius) ** 2 * float(hieght)
                print(volume)
            except (errors):
                Errors()
                
        elif shape.capitalize() == "Triangular prism":
            width = input("Enter the width: ")
            hieght = input("Enter the hieght: ")
            length = input("Enter the length: ")
            
            try:
                base = float(width) * float(hieght) / 2
                volume = base * float(length)
                print(volume)
            except (errors):
                Errors()
            
        elif shape.capitalize() == "Octagonal prism":
            x = input("Enter a side length: ")
            length = input("Enter the length of it: ")
            
            Hexagon(x, length)
            
        elif shape.capitalize() == "Trapezoidal prism":
            side_a = input("Enter the length of side a: ")
            side_b = input("Enter the length of side b: ")
            distance = input("Enter the disance betwen them: ")
            length = input("Enter the length: ")
            
            try:
                area = float(side_a) + float(side_b)
                area_2 = area / 2
                volume = area_2 * float(distance) * float(length)
                print(volume)
            except (errors):
                Errors()
            
        else:
            Errors()
            
    elif operation.capitalize() == "Surface area":
        print("This part of the program can only solve for:")
        print()
        print("Cube, Sphere, Cylinder")
        shape = input("Enter a shape: ")
        
        if shape.capitalize() == "Cube":
            cube_surface(errors)
            
        elif shape.capitalize() == "Sphere":
            radiuse = input("Enter the radiuse: ")
            
            try:
                surface_area = 4 * math.pi * float(radiuse) ** 2
                print(surface_area)
            except (errors):
                Errors()
                
        elif shape.capitalize() == "Cylinder":
            radius = input("Enter the radius of a side: ")
            hieght = input("Enter the hieght: ")
            
            try:
                part_1 = 2 * math.pi * float(radius) ** 2
                part_2 = 2 * math.pi * float(radius) * float(hieght)
                surface_area = part_1 + part_2
                
                print(surface_area)
            except (errors):
                Errors()
        
    elif operation.capitalize() == "Random number generator":
        min_num = input("Enter a min number: ")
        max_num = input("Enter a max number: ")
        
        try:
            for i in range(1):
                print(random.randint(int(min_num), int(max_num)), end=' ')
                print()
        except (errors):
            Errors()
            
    elif operation.capitalize() == "Simp algebra":
        print("This part of the program is not finished yet!")
        print("This part of the program can only solve eqations like:")
        print()
        print("1-89=x, 56+21=t and 97*31=v")
        text = input("Enter letters and numbers: ")
        
        letters = []
        count = 0
        nothing = ""
        equals = "="
        
        try:
            for digit in text:
                if digit.isalpha():
                    letters.append(digit)
                    count += digit.isalpha()
                
            while "=" in text:
                text = text.replace("=", "")
                break
                
            text = text.replace(digit, "")
            solved = eval(text)
            
            print(solved, equals, *letters)
        except (errors):
            Errors()
        
    elif operation.capitalize() == "Help":
        print(textwrap.fill(list_text, width=37))
            
    else:
        print(f"{operation} is invalid please try again")
        
