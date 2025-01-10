# Given DataList
DataList = [45, 28, -11, 0, 28, 10, -4, 45, 3, 19, -8, 7, 10, 3, 0, 28, 12, -6, -11, 10, 3]

# (a) Remove duplicates without creating a new list
i = 0
while i < len(DataList):
    if DataList.count(DataList[i]) > 1:
        DataList.remove(DataList[i])
    else:
        i += 1
print("Modified DataList (No duplicates):", DataList)

# (b) Identify the fifth smallest and second largest numbers
sorted_list = sorted(DataList)
fifth_smallest = sorted_list[4]
second_largest = sorted_list[-2]
print("Fifth Smallest:", fifth_smallest, ", Second Largest:", second_largest)

# (c) Rotate the list by 3 positions to the left
for _ in range(3):
    DataList.append(DataList.pop(0))
print("DataList after rotating 3 positions to the left:", DataList)

# (d) Divide the list into EvenList and OddList
EvenList = [num for num in DataList if num % 2 == 0]
OddList = [num for num in DataList if num % 2 != 0]
print("EvenList:", EvenList)
print("OddList:", OddList)

