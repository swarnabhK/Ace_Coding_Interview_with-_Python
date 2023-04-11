def find_minimum(arr):
  current_min = arr[0]
  min_idx = 0
  for idx,num in enumerate(arr):
      if(num<current_min):
          current_min = num
  return current_min

print(find_minimum([9,2,3,6]))
