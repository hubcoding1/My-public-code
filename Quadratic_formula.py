from os import system
from time import sleep
from math import sqrt
system('cls')

while True:
    print('What do you want to calculate with the quadratic formula?')
    I1 = input("discriminant (D), intersection(s) with x-axis (I), x-top (X), top (T), discriminant and intersection x-axis (DI) or quit (Q): ").upper()
    #discriminant
    if I1 == "D":
        A = (input('Give the value of A: '))
        B = (input('Give the value of B: '))
        C = (input('Give the value of C: '))
        try:
            A = float(A)
            B = float(B)
            C = float(C)
        except ValueError:
            print('invalid input')
            continue
        Discr = (B**2) - (4*A*C)
        if Discr == 0:
            print('D =',Discr,'and the formula has 1 intersection with the x-axis')
        elif Discr > 0:
            print('D =',Discr,'and the formula has 2 intersections with the x-axis')
        else:
            print('D =',Discr,'and the graph has no intersection with the x-axis')
    #intersection x-axis
    elif I1 == "I":
        A = (input('Give the value of A: '))
        B = (input('Give the value of B: '))
        C = (input('Give the value of C: '))
        try:
            A = float(A)
            B = float(B)
            C = float(C)
        except ValueError:
            print('invalid input')
            continue
        Discr = (B**2) - (4*A*C)
        if Discr < 0:
            print('this formula has no intersections with the x-axis')
        else:
            Sn1= (-B+ sqrt(Discr))/(2*A)
            Sn2= (-B- sqrt(Discr))/(2*A)
            if Discr == 0:
                print('The intersection with the x-axis is',Sn1)
            else:
                print('The intersections with the x-axis are x =',Sn1,'and x =',Sn2)
    #discriminant and intersection
    elif I1 == 'DI':
        A = (input('Give the value of A: '))
        B = (input('Give the value of B: '))
        C = (input('Give the value of C: '))
        try:
            A = float(A)
            B = float(B)
            C = float(C)
        except ValueError:
            print('invalid input')
            continue
        Discr = (B**2) - (4*A*C)
        if Discr < 0:
            print('D =',Discr,'And this formula has no intersections with the x-axis')
        else:
            Sn1= (-B+ sqrt(Discr))/(2*A)
            Sn2= (-B- sqrt(Discr))/(2*A)
            if Discr == 0:
                print('D =',Discr,'and the intersection with the x-axis is at x=',Sn1)
            else:
                print('D =',Discr,'and the intersections with the x-axis are x =',Sn1,'and x =',Sn2)
    #x-top
    elif I1 == 'X':
        A = (input('Give the value of A: '))
        B = (input('Give the value of B: '))
        try:
            A = float(A)
            B = float(B)
        except ValueError:
            print('invalid input')
            continue
        x_top = (-B)/(2*A)
        print('x-top =', x_top)
    #top
    elif I1 == 'T':
        A = (input('Give the value of A: '))
        B = (input('Give the value of B: '))
        C = (input('Give the value of C: '))
        try:
            A = float(A)
            B = float(B)
            C = float(C)
        except ValueError:
            print('invalid input')
            continue
        (x_top) = (-B)/(2*A)
        y_top = A*x_top**2 + B*x_top + C
        print('The top is (',x_top,',',y_top,')')
    #porgram quit
    elif I1 == "Q":
        print('The program stopped')
        sleep(1.4)
        break
    #typo's
    else:
        print('It looks like you made a typo, try again')
        continue
    