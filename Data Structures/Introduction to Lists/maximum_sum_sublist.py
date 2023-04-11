def find_max_sum_sublist(lst): 
  # Anytime you encounter a negative curSum, just reset and start the cursum from that point
  # Kadene's algorithm, at each iteration check for the currentMax
  curSum = lst[0]
  maxSub = lst[0]
  for i in range(len(lst)):
    if(curSum<0):
      curSum = lst[i]
    else:
      curSum += lst[i]
    maxSub = max(curSum,maxSub)

  return maxSub

print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))