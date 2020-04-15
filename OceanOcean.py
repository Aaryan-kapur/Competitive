# Ex1 Ocean God has some plans for the fishes


# The Indian Ocean had N number of fishes each with a specific amount of gold with them G = [g1,g2,g3…gN]. Fishes usually spend these golds for buying cosmetics and snacks in the Ocean Mall. One day the Ocean God has drunk a bottle of juice and said “You know what…. Imma make them fishes very unique”. So, god decided to give any amount of gold to individual fishes in G so that no two fishes can have the same amount of gold. Now God is wondering what is the minimum amount of gold X that he/she has to spend to make the fishes unique in G. If G = [3, 2, 1, 2, 1, 7] then X = 6 as, the new Gold could be [3, 4, 1, 2, 5, 7]. If G = [1, 2, 2] then X = 1. I.e the G can be [1,2,3]

# Input Format

# 6 3 2 1 2 1 7

# Constraints

# NA

# Output Format

# 6

# Sample Input 0

# 6
# 3 2 1 2 1 7
# Sample Output 0

# 6


def minSum(arr, n): 
      
    sum = arr[0]; prev = arr[0] 
  
    for i in range(1, n): 
        if arr[i] <= prev: 
            prev = prev + 1
            sum = sum + prev
        else : 
            sum = sum + arr[i] 
            prev = arr[i]
    return sum
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum1= 0
for i in range(n):
  sum1 += arr[i]

print(minSum(arr,n)-sum1)

# Ocean Robbery gang is on another mission




# The great Ocean robber gang is planning on a new robber mission called “Ocean N” with N members in it. Members in the mission have ages A = [a1,a2,a3…aN]. Since the mission needed cooperation from members, they were already in the increasing order. Cooperation between any two neighbouring members is based on their absolute age difference. Due to some reason they have to relieve K number of members from the gang. But after the removal of the K members, the maximum age difference among the adjacent members in the A should become minimum. So they need to choose those K members in such a way that even the maximum age difference X among neighbours is minimum for the new gang with size N-K. If A = {3, 7, 8, 10, 14}, K = 2 then X = 2. After removing elements A[0] and A[4], the maximum difference between adjacent members is minimum. After removing 0th and 4th member, the remaining gang is [7, 8, 10] If A = [12, 16, 22, 31, 31, 38], K = 3 then X = 6. After removing indices 3,4 and 5 array becomes [12, 16, 22].

# Input Format

# 5 3 7 8 10 14 2

# Constraints

# NA

# Output Format

# 2

# Sample Input 0

# 5
# 3 7 8 10 14
# 2
# Sample Output 0

# 2

import sys 
  
INT_MAX = sys.maxsize; 
INT_MIN = -(sys.maxsize - 1);
def minimumAdjacentDifference(a, n, k) :
    minDiff = INT_MAX;
    for i in range(k + 1) :
        maxDiff = INT_MIN; 
        for j in range( n - k - 1) :  
            for p in range(i, i + j + 1) : 
                maxDiff = max(maxDiff, a[p + 1] - a[p]);
        minDiff = min(minDiff, maxDiff); 
    return minDiff; 
n = int(input()) 
a =list(map(int,input().split())) 
k = int(input()) 
print(minimumAdjacentDifference(a, n, k)); 
