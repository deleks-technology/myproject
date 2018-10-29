#An Algorithm For a Lottery Ticket

#This is to Collect the User Name
guest = input("Please Enter your Name:")
print ("================================================================================================================")
print ("Hello", guest, "Welcome to Our Automated Lottery System, all you need to do is to supply 6 digits and try your luck")
print ("================================================================================================================")

#To Generate Random 6 digits and Assign it to an empty list called random_num
import random
random_num = []
for i in range (6):
    system_gen_no =random.randint(1,99)
    random_num.append(system_gen_no)

#Printing random_num to enable us test the equality conditional statement else, it's suppose to be hidden.    
print ("System Generate 6 digit",random_num)
print ("================================================================================================================")

#This code collects 6 digits from user and assign it to an empty list called user
user=[]
for i in range (6):
    x=int(input("Enter your first digit and press enter to input other Digits. \n"))
    user.insert(i,x)
    i+=1

#Printing user to compare with random_num else, it's suppose to be hidden also    
print ("Your 6 digits:",user)

print ("================================================================================================================")

#First Conditional Statement to test if random generated numbers are equal to the numbers supplied by users and print congratulatory message if it matches/equal
if random_num == user:
 print ("Hurray",guest,"! You won 1 Million Naira")

#Second Conditional Statement to print consolation message if the numbers entered by users is not equal to system generated numbers 
else:
    print ("Sorry", guest,"! You lost your chance of being a million naira richer, better luck next time")
