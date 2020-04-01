# Superman and Batman once went for having a fruit drink at Child Deer Shop. Until 10 PM, Superman and Batman had X and Y number of fruit drinks. The shop has very different way of serving the people after 10 PM. After 10 PM, for every call i they will get i number of drinks at a time. For example, during first call either Superman or Batman can have single shot of fruit drink. During second call either one of them can have 2 drinks and so on. Now both Superman and Batman has decided that they will leave the shop only after finishing equal number of fruit drinks. So now they need to figure out what is the minimum number of calls N to make the drinks equal. If X = 1, Y = 3 then N = 3. During first call we can add 1 drink to X then X=2. Add 2 drinks to Y then Y = 5. Add 3 drinks to X then X = 5. Now we made X and Y equal in N = 3 calls. If X = 30, Y = 20 then N = 4. During 4 calls add 1+2+3+4 to Y then Y = 30.

# Input Format

# 1 3

# Constraints

# NA

# Output Format

# 3




from math import sqrt,floor
lst = list(map(int,input().split()))
x = lst[0]
z=0
y  = lst[1]
a = max(x,y)
while(x!=y):
  i = 2*a- x-y
  q = (-1 + sqrt(8 * i + 1)) / 2
  # print(q, floor(q))
  if (q - floor(q) == 0) : 
            z = q;  
            x = y;
  a+=1
print(int(z))
