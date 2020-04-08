# Kapil Sharma goes to Vikendi for a Ghost Mission


# Kapil Sharma is a famous astrologer in the city of Vikendi. One day manager of famous apartment group called Kapil and told that their residents are threatened by ghosts in their homes. The manager wanted Kapil to visit the apartment to solve this issue. The apartment has N*N grid of single villas. Kapil found that some villas have negative energy in it. 1 represents that villa has negative energy and 0 represents that no negative energy is present in a villa. This binary grid is represented as G. Kapil finds that a villa at ijth position will have ghost if the villas from i to N (single row elements starting from ijith position) and i to N (single column elements starting from ijith position) have negativity in it. In this manner Kapil has to count the number of villas X which have negative villas in the right side of the row and downside of the column. For example, G = [[1, 1, 1], [1, 1, 0], [1, 0, 1]] X=2 as the homes are at positions (0, 0) and (2, 2) If G = [[0, 1, 1], [0, 1, 1], [0, 1, 1]] X = 6

# Input Format

# 3 1 1 1 1 1 0 1 0 1

# Constraints

# NA

# Output Format

# 2

# Sample Input 0

# 3
# 1 1 1
# 1 1 0
# 1 0 1
# Sample Output 0

# 2
# Explanation 0

# Line 1 is the N Rest of the lines are N*N matrix






N = int(input())

def check(data,i,j):
    for r in range(i,N):
        if(data[r][j]==0):
            return False
    for c in range(j,N):
        if(data[i][c]==0):
            return False
    return True

data = [0]*N
for i in range(N):
    data[i] = list(map(int,input().split()))
    
count = 0

for i in range(N):
    for j in range(N):
        if(data[i][j] and check(data,i,j)):
            count+=1

print(count)




# Snack Exchange at Bennett Lecture Hall

# In Bennett University lecture hall H, there are N*N seats. Each seat is occupied by different students. Each of these students are denoted using one of the four numbers 0,1,2 and 3. Number 1 is only one student who is a snacks supplier, Number 2 is only one student who wants the snacks from 1. Number 3 is given to multiple people who can just pass the snacks to anyone next to them who is also number 3. Number 0 is given to people who does not cooperate in the whole process and does not pass the snacks to anyone. Given a hall H with a single source student 1, single destination student 2, 3s and 0s at random locations, you have to count what is the minimum number of moves X needed to move from the 1 to 2. If H = [[0 , 3 , 2 ], [3 , 3 , 0], [1 , 3 , 0 ]]; X=4

# If H = [[3 , 3 , 1 , 0 ], [ 3 , 0 , 3 , 3 ], [ 2 , 3 , 0 , 3 ], [ 0 , 3 , 3 , 3 ]]; Then X=4

# Input Format

# 3 0 3 2 3 3 0 1 3 0

# Constraints

# NA

# Output Format

# 4

# Sample Input 0

# 3
# 0 3 2
# 3 3 0
# 1 3 0 
# Sample Output 0

# 4
# Explanation 0

# Line 1 is the N Rest of the lines are N*N matrix



N = int(input())
                
data,one,two = [0]*N,[],[]

for i in range(N):
    data[i] = list(map(int,input().split()))
    if(1 in data[i]):
        one = [i,data[i].index(1)]
    elif(2 in data[i]):
        two = [i,data[i].index(2)]
        
print(abs(one[0]-two[0])+abs(one[1]-two[1]))



