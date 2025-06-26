# Extract All Numbers Divisible by 3

# arr = [ 4, 9, 1, 6, 3, 7, 12 ]

# div_by_3 = [num for num in arr if num % 3 == 0]
# print(div_by_3)


# Accept user input for the array

# arr_input = input("Enter Vallue Seperated by space : ")

# arr = list(map(int , arr_input.split()))

# print(arr)




#Array Program: Menu-driven array Operation

print("Array Operation Program")

print(f"{'='*25}")

arr =[]

#input array

array_input = input("Add Element by seperated space :")

arr = list(map(int , array_input.split()))

while True:

    print("\n-------- Menu --------")
    print("1. Display Array")
    print("2. Reverse Array")
    print("3. Sort Array by Ascending order")
    print("4. Sort Array by Descending order")
    print("5. Search by an Element")
    print("6. Remove an Element")
    print("7. Insert Element")
    print("8. Exit")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        print("Array :" , arr)

    elif choice == 2:
        print("Reverse Array :" , list(reversed(arr)))

    elif choice == 3:
        sorted_arr = sorted(arr)
        print("Sort by Ascending order :" , sorted_arr)

    elif choice == 4:
        sorted_arr = sorted(arr , reverse =True)
        print("Sort by Descending order :" , sorted_arr)

    elif choice == 5:
        val = int(input("Enter value to search :"))
        if val in arr:
            print(f"{val} found at index {arr.index(val)} ")
        else:
            print(f'{val} not found in array!!')

    elif choice == 6:
        val = int(input("Enter value to remove :"))
        if val in arr:
            arr.remove(val)
            print(f"{val} is remove from array. ")       
        else:
            print(f"{val} not found in array.")

    elif choice == 7:
        val = int(input("Enter value to insert :"))
        pos = int(input("Enter of insert element position :"))

        if 0<= pos <= len(arr):
            arr.insert(pos , val)
            print("Update array :" , arr) 
        else:
            print("Invalid position!!")

    elif choice == 8:
        print("Successfully Exit....🎉 , Thank you!!")    

    else:
        print("Invalid choice!! Please Enter right choice....!!!!!!!")   