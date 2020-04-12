https://www.codechef.com/APRIL20B/problems/CARSELL

T = int(input())

for i in range(T):
    N,data,profit = int(input()),list(map(int,input().split())),0
    data.sort(reverse = True)
    
    for p in range(N):
        if(data[p]-p>0):
            profit+=data[p]-p
        else:
            break
    
    print(profit%1000000007)
