Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x1 = float(input("Enter x1: "))
... y1 = float(input("Enter y1: "))
... x2 = float(input("Enter x2: "))
... y2 = float(input("Enter y2: "))
... 
... slope = (y2 - y1) / (x2 - x1)
... 
... print("The slope of the line passing through the points ({}, {}) and ({}, {}) is: {:.2f}".format(x1, y1, x2, y2, slope))
