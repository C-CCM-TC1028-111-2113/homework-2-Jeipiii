x = int(input(("Dame un numer entero :")))       
y = int(input(("Dame un numer entero :")))
z = int(input(("Dame un numer entero :")))

    
if x > z and x > y:
    print("El numero más grande es: " + str(x))
if y > z and y > x:
    print("El numero más grande es: " + str(y))
if z > x and z > y:
    print("El numero más grande es: " + str(x))
