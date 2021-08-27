height =input("Please Input your height in meters\n")
height= float (height)

weight =float( input("Input your wieght in killograms\n"))
BMI = weight/ ( height **2)

print("The value for your BMI is : " + str(BMI) )


if BMI > 40:
    print ( " You are Very severly obese")
elif BMI >= 35:
    print( "  You are Severly obese")
elif BMI >=30:
    print ("You are Moderately obese")
elif BMI >= 25:
    print ("You are Overweight")
elif BMI >=18.25:
    print ("You are Normal")
elif BMI >= 16 :
    print ( "You are Underweight")
elif BMI >=15:
    print ("You are severely underweight")
elif BMI < 15:
    print ("You are Very severely underweight")
