# Lab_7_Module.py

def Sum(number1, number2):
    Sum = number1 + number2
    return Sum


def Subtract(number1, number2):
    Difference = number1 - number2
    return Difference


def Multiply(number1, number2):
    Product = number1 * number2
    return Product


def IntDivision(number1, number2):
    Int_Division = number1//number2
    return Int_Division


def FloatDivision(number1, number2):
    Float_Division = number1/number2
    return Float_Division


def Square(number):
    Square = number*number
    return Square


def SquareRoot(number):
    SquareRoot = number**0.5
    return SquareRoot


def SquareArea(length):
    Area = length*length
    return Area


def RectangleArea(length, width):
    Area = length * width
    return Area


def CircleArea(radius):
    pi = 3.1415
    Area = pi*((radius)**2)
    return Area


def Right_Scalene_TriangeArea(base, height):
    Area = 0.5*(base*height)
    return Area

def EquilateralTriangleArea(side1, side2, side3):
    side = side1 = side2 = side3
    Area = ((3**0.5)/(4))*(side)
    return Area

def SphereSurfaceArea(radius):
    pi = 3.1415
    SurfaceArea = (4*pi)*(radius**2) 
    return SurfaceArea


def ShpereVolume(radius):
    pi = 3.1415
    Volume = ((4/3)*pi)*(radius**3) 
    return Volume


def CuboidSurfaceArea(length, width, height):
    SurfaceArea = 2*(length*width + width*height + height*length)
    return SurfaceArea


def CuboidVolume(length, width, height):
    Volume = length*width*height
    return Volume


def Tuple2List(*Tuple):
    List = list(Tuple)
    return List
    

def TupleEvenCounter(Tuple):
    counter = 0
    for i in range(len(Tuple)):
        if(Tuple[i]%2 == 0):
            counter = counter + 1
        else:
            continue
    return counter


def TupleGreaterThan20(Tuple):
    List = []
    for i in range(len(Tuple)):
        if(Tuple[i]>20):
            List.append(Tuple[i])
        else:
            continue
    return List
                   
                   
                   