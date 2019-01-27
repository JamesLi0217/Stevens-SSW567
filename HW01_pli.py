'''
@Title: Testing triangle classification
@Author: PuzhuoLi  CWID:10439435
@Date: 2019-01-25 23:54:31
'''


import math


def classify_triangle(a, b, c):
    '''
    equilateral triangles have all three sides with the same length
    isosceles triangles have two sides with the same length
    scalene triangles have three sides with different lengths
    right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
    '''

    lines = [a, b, c]
    lines.sort()
    if  type(a) not in (float,int) or type(b) not in (float,int) or type(c) not in (float,int):
        raise TypeError("Only enter number")
        
    elif a<=0 or b<=0 or c<=0:
        raise ValueError("length > 0")
        
    else:
        a, b, c = lines[0], lines[1], lines[2]
    # the sum of any two length > the third
    
    if a+b > c:
        if c**2 == a**2+b**2 and a == b:
            m1 = "It is a isoscele triangle and a right triangle as well!"
            print(m1)
            return m1
        elif c**2 == a**2+b**2 and a != b:
            m2 = "It is a right triangle!"
            print(m2)
            return m2
        elif a == b == c:
            m3 = "It is an equilateral triangle but not a right triangle!"
            print(m3)
            return m3
        elif a == b or b == c:
            m4 = "It is a isoscele triangle but not a right triangle!"
            print(m4)
            return m4
        else:
            m5 = "It is a scalene triangle and not a right triangle!"
            print(m5)
            return m5
    else:
        m6 = "Please double check the enter, it is not a triangle"
        print(m6)
        return m6


def main():
    lines = []
    # enter 3 number as length of triangle
    while len(lines) < 3:
        # check valid enter
        try:
            x = float(input("Please enter a number: "))
        except:
            m7 = "Please double check the enter"
            print(m7)
        else:
            lines.append(x)

    a, b, c = lines[0], lines[1], lines[2]

    classify_triangle(a, b, c)


if __name__ == "__main__":
    main()
