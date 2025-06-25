# #Part-1  Use of Built-in Function in Python

import random

# #import the random module to generaterandom number later.

print("<=== Part-1 Built-in Function on list ===>")

numbers =[4 ,2 ,7 ,9 ,5 ,6]

print("List =" , numbers)

# #len()

# # A list named number is defined with 5 integers.

# #len() return the number of list

print("Length of list = " , len(numbers))


# #max() and min() are used to find the largest and smallest number respectively.

print("Max number = " , max(numbers))
print("Min number =" , min(numbers))

#sum() adds all values un the list

print("Sum of List =" , sum(numbers))



# # Part-2 Negative Flot Number Operation

print("<=== Part-2 Operation in Negative Value")

num = float(input("Enter a Negative float Number :"))

#abs() return the positive version from the user

print("positive version from the user :" , abs(num))

# #pow() raises the positive value of the power

print("Power of Value :" , pow(num,10))

#round() round of the number to 2 digit after the decimal point

print("Random of Value :" , round(num))

# #Part:3  Random List and Its Values / Analysis

print("<=== Part:3 Round List and Its Values / Analysis ===>")

random_num = random.sample(range(1 , 100) , 5)
print(random_num)

# #using max() , and min() , sum() in random Value

print("Random List :" , random_num)

print("Random Number max count :" , max(random_num))
print("Random Number min count :" ,min(random_num))
print("Random Number sum count :" ,sum(random_num))


#part:4 sort and Reverse a list

print ("<=== Sort and Reverse a list ===>")

user_list = list(map(int , input("Enter Number seperated by space :").split()))
prin(user_list)


# sorted() the original user inputs

# reverse() return a reverse iterator , and list convert in back to a list

print("Sorted List Ascending" , sorted(user_list))

# print("Sorted List Descending" , sorted(user_list , reverse=True))

print("Reverse value of List : " , list(reversed(user_list)) )