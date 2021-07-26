string = input("Please input the string")
k = int(input("Please input the number k"))


def power(string,k):
    if k>=0:
        return(string*k)
    else:
        ref = string[0:int(len(string)/-k)]
        if power(ref,-k) == string:
            return ref
        else:
            return("Undefined")

print(power(string,k))
