
def friend(x):
    #Code
    friends = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            friends.append(x[i])
    print(friends)        
friend(list(input().split()))