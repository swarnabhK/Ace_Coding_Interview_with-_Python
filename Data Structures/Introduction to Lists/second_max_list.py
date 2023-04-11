import math
def find_second_maximum(lst):
  first_max,second_max = -math.inf,-math.inf
  for num in lst:
      if(num>first_max):
          first_max = num
  for i in range(len(lst)):
      if(lst[i]>second_max and lst[i]<first_max):
          second_max = lst[i]
  return second_max

print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([4, 2, 1, 5, 0]))