# Swami is a highly talented faculty :P who taught a fantastic course called Deep Learning to N number of 4th year students. In his class he had wide varieties of students each with different mentality towards life. Based on some analysis he found that each student has level of mentality in terms of either positivity or negativity in their minds M = [m1,m2,m3…mN]. Swami believes in a marvellous theory about student gangs. He believes that the energy a gang is the product of the students’ mentalities in the gang. Now Swami ji is wondering that how many different possible student gangs X are there with negative mentalities. The students of a gang should be adjacent to each other from the M. If M = [-1, 2, -2] then X = 4. Because gangs with negative mentalities are [-1], [-2], [-1, 2] and [2, -2]. If M = [5, -4, -3, 2, -5], then X = 8.

# Input Format

# 3 -1 2 -2

# Constraints

# NA

# Output Format

# 4

# Sample Input 0

# 3
# -1 2 -2
# Sample Output 0

# 4
# Explanation 0

# 1s line is the N 2nd line is the array

#solution:





k  = int(input())
w = list(map(int,input().split()))
count = 1
count1 = 0
for i in range(len(w)):
  if(w[i]>0):
    w[i] = 1
  else:
    w[i] = -1
  if(i>0):
    w[i]*=w[i-1]
  if(w[i] ==1):
    count +=1
  else:
    count1 +=1
count2 = count * count1
print(count2)
  
