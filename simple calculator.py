n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
print("press 1 for addition \npress 2 for subraction \npress 3 for multiplication \npress 4 for division")
choice=int(input("Enter your choice from 1-4: "))
if choice==1:
    print("The Addition of given two numbers is: ",n1+n2)
elif choice==2:
    print("The Subraction of given two numbers is: ",n1-n2)
elif choice==3:
    print("The Multiplication of given two numbers is: ",n1*n2)
elif choice==4:
    print("The Division of given two numbers is: ",n1/n2)
else:
    print("Invalid Input")
