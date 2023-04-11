def right_rotate(lst, k):
  # Write your code here
  # rotate the right elements to the end and the left elements to the beginning.
  # len(lst)-k denotes the starting point of the resulting list
  if(len(lst)==0):
      k=0
  else:
      k = k%len(lst)
  res = []
  for i in range(len(lst)-k,len(lst)):
      res.append(lst[i])
  for i in range(0,len(lst)-k):
      res.append(lst[i])
  return res

print(right_rotate([1, 2, 3, 4, 5], 2))
print(right_rotate(['right', 'rotate', 'python'], 4))