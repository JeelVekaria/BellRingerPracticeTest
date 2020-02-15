# Triangle2.oy
# ICS201 Jeel Vekaria
# Feb 13, 2020

a1=int(input("Enter First Angle"))
a2=int(input("Enter Second Angle"))
a3=int(input("Enter First Angle"))
angle = a1+a2+a3
while angle == 180:
    if a1 == a2 == a3:
        print("Equilateral triangle")
    elif a1 == a2 or a1 == a3 or a2 == a3 or a3 == a2 or a2 == a1 or a3 == a1:
        print("Isosceles triangle")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Right Angle Triangle")
    break
if angle<180 or angle>180:
    print("Error")

