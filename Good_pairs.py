list1 = input("Please input the list of numbers in the form of list")
list2 = []
for i in range(len(list1)):
    if list1[i] != ","  and  list1[i] != "[" and list1[i] != "]":
        list2.append(list1[i])
size = len(list2)
sum = 0
for i in range(size-1):
    for j in range(i+1,size):
        if list2[i] == list2[j]:
            sum += 1
print(sum)

            
