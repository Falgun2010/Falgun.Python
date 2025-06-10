print("Welcome to the Interactive Personal Date collector!")

NAME=str(input(" Enter your Name ="))
AGE=int(input(" Enter your Age ="))
HEIGHT=float(input(" Enter your Height ="))
FAVOURITENUMBER=int(input(" Enter your Favourite Numben ="))

print("Thank you! Here is the information We collected.") 

print(("NAME:") , NAME ,("(") , ("Type:") , type(NAME) ,("/") , ("Memory Address:") , id(NAME) , (")"))
print(("NAME:") , AGE ,("(") , ("Type:") , type(AGE) ,("/") , ("Memory Address:") , id(AGE) , (")"))
print(("NAME:") , HEIGHT ,("(") , ("Type:") , type(HEIGHT) ,("/") , ("Memory Address:") , id(HEIGHT) , (")"))
print(("NAME:") , FAVOURITENUMBER ,("(") , ("Type:") , type(FAVOURITENUMBER) ,("/") , ("Memory Address:") , id(FAVOURITENUMBER) , (")"))
