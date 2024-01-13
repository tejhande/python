import os
clear = lambda: os.system('clear') #on Windows System

my_dict={}
def options():
    print("**********************************************************")
    print("**********Sawndarya Beauty Parlor And Cosmatics***********")
    print("**********************************************************")
    print("1.Add Product")
    print("2.Delete Product")
    print("3.Update Product Details")
    print("4.Display List of Products")
    print("5.Contact us")
    print("6.Exit")
    print("Choose Options:")
    ch=int(input())
    if(ch==1):
        add_item()
        i=input("Do You want to continue Press(Y/N):")
        if(i=='y' or i=='Y'):
            clear()
            options()
        else:
            clear()
            return
    elif(ch==2):
        delete_item()
        i=input("Do You want to continue Press(Y/N):")
        if(i=='y' or i=='Y'):
            clear()
            options()
        else:
            clear()
            return
    elif(ch==3):
        update_item()
        i=input("Do You want to continue Press(Y/N):")
        if(i=='y' or i=='Y'):
            clear()
            options()
        else:
            clear()
            return
    elif(ch==4):
        display_item()
        i=input("Do You want to continue Press(Y/N):")
        if(i=='y' or i=='Y'):
            clear()
            options()
        else:
            clear()
            return
    elif(ch==5):
        display_status()
        i=input("Do You want to continue Press(Y/N):")
        if(i=='y' or i=='Y'):
            clear()
            options()
        else:
            clear()
            return
    elif(ch==6):
        return 
    else:
        print("Please enter valid choice..")
        
def add_item():
    key=input("Enter Product ID:")
    value=input("Enter Name:")
    my_dict[key]=value
    print("Product Add Succesfully..")
            
def delete_item():
        if(len(my_dict)==0):
            print("Cant Do the Delete Operation..")
            print("Products Are Not Available")
        else:
            print(my_dict)
            key=input("Enter ID of Product you want to delete:")
            del my_dict[key]
            print("Product delete Succesfully..")
def display_item():
    print(my_dict)
def update_item():
    print(my_dict)
    key=input("Enter ID of Product you want to update Value:")
    value=input("Enter Name of Product:")
    my_dict[key]=value
    print("Product Update Succesfully..")
def display_status():
    print("**********************************************************")
    print("**********Sawndarya Beauty Parlor And Cosmatics***********")
    print("**********************************************************\n")
    print("Created By: Thorat Rohit\nThird Year Computer Department\nEnrollment No. : 1710510072")

options()