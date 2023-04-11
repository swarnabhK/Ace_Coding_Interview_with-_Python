def find_first_unique(lst):
  unique = 0
  for i in range(len(lst)):
      for j in range(len(lst)):
          if(i==j):
              continue
          elif(i!=j):
              if(lst[i]==lst[j]):
                  unique = 1
                  break
          unique = 0
      if(unique==0):
          return lst[i]
  return -1

print(find_first_unique([9, 2, 3, 2, 6, 6]))
print(find_first_unique([4, 5, 1, 2, 0, 4]))
