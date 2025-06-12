#1.Print your Name 

#print("Hello , my name is falgun!!!")

#2. Ask name and Print
#name=input( " what is your name : " )
#print("Nice to meet you ," , name)

#3. sum of two numbber

#a = 20
#b= 11

#sum = a+b
#print('This sum is:' , sum)


#4. simpel calculator

#a = int(input("Enter firs number :"))
#b= int(input("Enter second number :"))

#print("addition:", a + b)
#print("sub:", a - b)
#print("multiplication:", a * b)
#print("division:", a / b)

                                                    
#5. sandwich make

#bread = input("chooose your bread (white/brown)")
#filling = input("chooose your filling (chees / jam / potato / banana )")

#print("Here you silly sandwich : 🥪")
#print("[" + bread + " bread " + filling + " rainbow silly sandwich 🌈 " + " ]")




#6.rock , paper and scissors game

import random

chocies = ["rock" , "paper" , "scissors"]
computer = random.choice(chocies)
player = input(" choose rock , paper and scissors : ")

if player == computer:
    print("😂, it's a tie!! ")
elif (player == "rock" and computer == "scissors") or \
    (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"): 
    print("🎉 You win...")
else:
    print("🎊 computer win....")
