
##VERY BRUTE AND VERY NAIVE
def find_max(lst):
    maximum = lst[0]
    max_idx = 0
    for idx,num in enumerate(lst):
        if(num>maximum):
            maximum = num
            max_idx = idx
    return max_idx,maximum

def find_min(lst):
    minimum = lst[0]
    min_idx = 0
    for idx,num in enumerate(lst):
        if(num<minimum):
            minimum = num
            min_idx = idx
    return min_idx,minimum

def max_min_brute(lst):
    res = []
    while(1):
        if(len(lst)!=0):
            idx,max_val = find_max(lst)
            res.append(max_val)
            lst.pop(idx)
        else:
            return res
        if(len(lst)!=0):
            idx,min_val = find_min(lst)
            res.append(min_val)
            lst.pop(idx)
        else:
            return res
    return res

#Brute Force solution test cases
print("Test cases for brute force solution: ")
print(max_min_brute([1, 2, 3, 4, 5, 6, 7]))
print(max_min_brute([1, 2, 3, 4, 5]))
print(max_min_brute([]))
print(max_min_brute([1, 1, 1, 1, 1]))
print(max_min_brute([-10, -1, 1, 1, 1, 1]))

#OPTIMAL SOLUTION: Since the elements in list are sorted.
# We can use two pointers technique


def max_min(lst):
    res = []
    left_pointer = 0
    right_pointer = len(lst)-1
    while(left_pointer<right_pointer):
        res.append(lst[right_pointer])
        res.append(lst[left_pointer])
        left_pointer+=1
        right_pointer-=1
    if(left_pointer==right_pointer):
        res.append(lst[left_pointer])
    return res

#Optimal solution test cases
print("Test cases for optimal solution: ")
print(max_min([1, 2, 3, 4, 5, 6, 7]))
print(max_min([1, 2, 3, 4, 5]))
print(max_min([]))
print(max_min([1, 1, 1, 1, 1]))
print(max_min([-10, -1, 1, 1, 1, 1]))