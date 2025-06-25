#CRUD in python


# C :- Create

# R :- Read

# U :- Update

# D :- Delete

#Example:

users = [
   {"id":1 , "name":"Alice" , "age": 25},
   {"id":2 , "name":"Melisha" , "age": 30},

]

while True:
    print("CRUD Operation in Python!!!!!!!!")
    print("1. create user")
    print("2. read user")
    print("3. update user")
    print("4. delete user")
    print("5. exit")

    choice = input("Enter your Choice(1-5) :")

    if choice == "1":
      
        try:
            user_id = int(input("Enter id : "))
            name = input("Enter name :")
            age = int(input("Enter age :"))
            users.append({"id": user_id , "name": name , "age": age})

            print("User Successfully Added!!")
        
        except:
            print("Invalid Input!!!")

    elif choice == "2":

        if not users:
            print("No User found.")
        
        else:
            print("User List:")
            for user in users:
                print(user)

    elif choice == "3":

        try:
            user_id = int(input("Enter Update user id :"))
            
            found = False 

            for user in users:

                if user["id"] == user_id:

                    field = input("Enter your field to update (name/ age) :").lower()

                    if field in user:

                        if field =="age":

                            user["age"] = int(input("Enter new age :"))
                        
                        else:
                            
                            user["name"] = int(input("Enter new ame :"))
                    
                        print("User update saccessfully!!!")
                    
                    else:
                        print("invalid field!!")

                    found = True

                    break

            if not found:

                print("user not found!!")

        except:

            print("invalid input!!")
        
    elif choice == "4":

        try:

            user_id = int(input("Enter ID to delet User : "))

            for user in users:

                new_users = []

                if user["id"] != user_id:

                    new_users.append(user)

                    user = new_users

                    print("user delete successfully!!!")

        except:

            print("invalid input!!!")

    elif choice == "5":

        print("Program exit successfuly!!") 

    else:

        print("Invalid Choice, Please Enter number of 1 to 5.")   

            




                