import math

print("Helllo World!")
radius = int(input("Enter the radius of the circle. "))
area = math.pi*(radius**2)
print("The area of the circle is: " + str(area))

shadedlength = int(input("Enter the length of the shaded area. "))
shadedheight = int(input("Enter the height of the shaded area. "))
shadedarea = shadedlength*shadedheight
totalarea = shadedarea-area

if totalarea > 0:
    print("The total area is: " + str(totalarea))

if totalarea < 0:
    print("You have entered invalid units, and the circle's area is greater than the rectangles. You can't have a negative area.")
    
    
