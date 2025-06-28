print("Welcome to Inventory List Analyzer! ")

items = []
categories = []

while True:

    item = input("\nEnter item name : ")
    category = input("Enter category : ")
    quantity = int(input("Enter quantity : "))

    items.append({
        "item": item,
        "category": category,
        "quantity": quantity,
    })
    
    many_items = input("\nDo you want to add more items? (y/n) :   ")

    if many_items  == 'y': 
        continue

    elif many_items == 'n':
        break

    else:
        print("\nInvalid choice!!!!")    
    

print("\n========== INVENTORY SUMMARY ==========\n")  

Total_items = len(items)
Total_quantity = sum(item['quantity'] for item in items)
Average_Quantity = Total_quantity/Total_items
most_stocked = max(items , key= lambda x: x['quantity'])
least_stocked = min(items , key= lambda x: x['quantity'])

print("\nTotal Different Items :" , Total_items)
print("\nTotal Quantity in stock :" , Total_quantity)
print("\nAverage Quantity per Itrm :" , Average_Quantity)
print(f"\nMost Stocked Item : , {most_stocked['item']} ({most_stocked['quantity']}units)")
print(f"\nLeast Stocked Item : , {least_stocked['item']} ({least_stocked['quantity']}units)")

print("\n-------------------------------------\n")

categories = sorted((set(item['category'] for item in items)))
print(f"unique categories are in inventory:  {set(categories)}")


print("\n-------------------------------------\n")

print("📦 Items Sorted by Quantity (High to Low):\n")

sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
for i, item in enumerate(items, start=1):
    print(f"{i}. {item['item']} - {item['quantity']} units")

print("\n-------------------------------------\n")

print("Categories in Alphabetical Order:\n")
for i, cat in enumerate(categories,start=1):
    print(f"{i}. {cat}")


print("\n============ END OF REPORT ============")