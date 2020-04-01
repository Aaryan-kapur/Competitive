# Hulk is a good young dude from Kasna village. He goes to Haldiram to buy N types of sweets for celebrating Diwali with his friends. Initially he bought sweets in kilos S = [s1, s2, s3…sN]. After paying bills he gets a call from his friends saying that he has to buy sweets in the following order. Every sweet Si has to be lesser or equal to next sweet Si+1. So he tells the Haldiram bhayya to make it in that way. Now bhayya can either add a kilo or remove a kilo of sweet from Si at a time. Now Hulk needs to tell Bhayya the minimum number of times T required to make the sweets in the specific order. For example S = [1, 2, 1, 4, 3] then T = 2. First we can add a kilo to 3rd sweet and subtract a kilo from 4th sweet to get [1, 2, 2, 3, 3]. If S = [1, 2, 2, 100] then T = 0.

# Input Format

# 5 1 2 1 4 3

# Constraints

# NA

# Output Format

# 2

# Sample Input 0

# 5
# 1 2 1 4 3
# Sample Output 0

# 2
# Explanation 0

# First line is the N Second line is the array





# k = input()
# ar = list(map(int,input().split()))
# n = len(ar) 
# min = min(ar) 
# max = max(ar)
# arr = [[ 0 for i in range(max + 1)]  for i in range(n)] 
# for j in range(min, max + 1):
#   arr[0][j] = abs(ar[0] - j)
# for i in range(1, n): 
#   minimum = 10**9
#   for j in range(min, max + 1): 
#     minimum = min(minimum, arr[i - 1][j]) 
#     arr[i][j] = minimum + abs(ar[i] - j)
#     val = 10**9
#     for j in range(min, max + 1): 
#       val = min(val, arr[n - 1][j]) 
# print(val)


n = int(input())
ar = list(map(int,input().split()))
smallest = min(ar) 
largest = max(ar) 
array = [[ 0 for i in range(largest + 1)]  
              for i in range(n)] 
for j in range(smallest, largest + 1): 
  array[0][j] = abs(ar[0] - j) 
for i in range(1, n): 
  minimum = 10**9
  for j in range(smallest, largest + 1): 
    minimum = min(minimum, array[i - 1][j]) 
    array[i][j] = minimum + abs(ar[i] - j) 
    result = 10**9
    for j in range(smallest, largest + 1): 
        result = min(result, array[n - 1][j]) 
  
print(result)  
