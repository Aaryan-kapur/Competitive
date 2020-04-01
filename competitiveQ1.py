# Arnold Schwarzenegger goes to doll shop to buy teddy bears for his wife. Silvester Stallone the shop keeper worked real hard and helped Arnold to choose N number of teddy bears each weighing W = [w1,w2,w3…wN]. Now Arnold decided that every doll should weigh at least greater than or equal to T. But Silvester does not like to help Arnold at all. So Silvester tells Arnold that every time he can take two smallest teddy and replace by a single teddy. That single teddy should weigh equal to LCM of the two smallest teddies. Arnold is wondering that what is the minimum number of iterations X required to make every teddy bear greater or equal to T. If it is impossible to get such teddy bear combination print -1. If N = 4, T = 3 , W=[1 4 5 5] then X = 1. Since LCM of 1 and 4 is 4 then (1,4) will be replaced by single teddy 4. Now W = [4,5,5]. If N = 5, T = 8 , W=[4,4,4,4,4] then X = -1. Because it is impossible to get such teddies.

# Input Format

# 4 1 4 5 5 3

# Constraints

# NA

# Output Format

# 1

# Sample Input 0

# 4
# 1 4 5 5
# 3
# Sample Output 0

# 1
# Explanation 0

# 1st line is N 2nd line is array 3rd line is T


#solution:


import heapq

def lcm(a,b):
  if a == 0:
    return (a*b) / b
  elif(b%a == 0):
    return(a*b)/a

    
n = int(input())
arr = (list(map(int,input().split())))
t = int(input())
heapq.heapify(arr)
ans = 0
bool = False
while(len(arr)!=1):
    v = heapq.heappop(arr)
    if(v>=t):
        bool = True
        break
    else:
        heapq.heappush(arr,v)
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    e = int(lcm(a,b))
    heapq.heappush(arr,e)
    ans+=1

if(bool):
    print(ans)
elif(len(arr)==1):
    if(arr[0]>=t):
        print(ans)
    else:
        print(-1)
