
print("Welcome to the pattern generator and number Analyzer\n")
print("Selct an option:")
print("1. Right-angled triangle")
print("2. pyramid")
print("3. left-angled triangle")
print("4. Analyze a Range of Numbers")

choice = int(input("Enter your choice: "))


if choice in [1 ,2 ,3 ,4]:
   
   if choice == 1:
      row = int(input("Enter the number of rows for the pattern "))
      print("pattern: ")
      for i in range(1, row + 1):
        print("*" * i)

   elif choice == 2:
       row = int(input("Enter the number of rows for the pattern "))
       print("pattern: ")
       for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2*i  -1))

   elif choice == 3:
     row = int(input("Enter the number of rows for the pattern "))
     print("pattern: ")
     for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

   elif choice == 4:
      start=(int(input("Enter the start of range:")))    
      end=(int(input("Enter the end of range:")))  
      total=0
      for num in range(start , end +1):
          if num %2 == 0:
            print(f"Number {num} is Even") 

          else:
             print(f"Number {num} is Odd") 
          total += num
      print(f"Sum of all numbers from {start} to {end} is: {total}")

else:
   print("Sorry!, This option is not Availeble!!")      
    
               