t = int(input())

def do():
    money = int(input('Please write the total amount of money'))
    size = int(input("Please indicate the size of the cost"))
    cost = input("Please write costs of ice creams")
    cost= cost.split(' ')
    cost= list(cost)
    for i in range(size):
        rest_of_costs = (set(cost[i+1: size]))
        if str(money - int(cost[i])) in rest_of_costs:
            j = cost[i+1:size].index(str(money - int(cost[i])))+i+1
            list1= [j+1,i+1]
            list1.sort()
            return(list1)
        break

for _ in range(t): 
    print(do())


