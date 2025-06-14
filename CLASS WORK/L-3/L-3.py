#print() formatting using set and end

print("Apple" , "banana" , "Cherry" , sep=" ~ " , end="<--- end of list\n")

#formatted message for user input

Name = input("Enter your Name:")
Age = input("Enter your Age:")
Hobby = input("Enter your Hobby:")


print(" my name is " + Name + " and my age is " + Age + " and hobby is " + Hobby)

print(f"Hello , {Name}! At {Age} , enjoying {Hobby} sound fun! ")