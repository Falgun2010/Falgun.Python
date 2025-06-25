# 1. find the length of a 1D array without len()


size = int(input("Enter array size :"))

arr = []

print("Enter array Element :")

#loop

print(arr)

for i in range(size):
    val = int(input(f"a[{i}] ="))
    arr.append(val)


#count length manually

# print(len(arr))

# length = 0

# for _ in arr:
#     length += 1
# print(length)


length = 0

for _ in arr:
    length += 1
print(length)




# 2. Find teh average of a 1D array.

size = int(input("Enter size of array:"))

arr = []

print("Enter array Element:")

for i in range(size):
    val = int(input(f"a[{i}] ="))
    arr.append(val)


#calculate the average

total = 0
length = 0

for val in arr:
  total += val
  length += 1

average = total/length

print("average of an array : " , average )
