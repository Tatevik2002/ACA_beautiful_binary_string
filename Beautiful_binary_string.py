our_string = input()
sum = 0
i = 0
size = int(input())
while i < size - 4:
    if our_string[i] == "0":
        if our_string[i+1:i+3] == "10":
            if our_string[i+3] == "1":
                sum += 1
                i += 4
            else:
                sum += 1
                i += 3
        else:
            i += 1
    else: 
        i += 1
if our_string[size -3 : ] == "010":
    sum += 1
print(sum)
