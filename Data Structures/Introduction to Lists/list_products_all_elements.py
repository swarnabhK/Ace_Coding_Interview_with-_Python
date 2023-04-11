def find_product(lst):
  # Write your code here
  product = []
  for i in range(len(lst)):
      prod = 1
      for j in range(len(lst)):
          if(i!=j):
              prod = prod*lst[j]
      product.append(prod)
  return product

print(find_product([1,2,3,4]))