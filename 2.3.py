import math 

side = int(input("Input number of sides: "))
len = int(input("Input the length of a side: "))

area = int((side * (len ** 2)) / (4 * math.tan(math.pi / side)))

print ("The area of the polygon is: ", area)