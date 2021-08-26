x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))

if x > y and y > z :
    print( "The list is this ;" + str(x) + "" + str(y) + "" + str(z))
if y > x and z > x :
    print ( "The list is this ;" + str(y) + "" + str(z) + "" + str(x))
if z > y and x > y :
    print ( "The list is this ;" + str(z) + "" + str(x) +  "" + str(y))
    
