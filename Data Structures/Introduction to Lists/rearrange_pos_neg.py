def rearrange_brute(lst):
    # Write your code here
    res = []
    for num in lst:
        if(num<0):
            res.append(num)
    for num in lst:
        if(num>=0):
            res.append(num)
    return res

def rearrange(lst):
    #keep a pointer for the current leftmost_positive_element
    # swap that element when you encounter a negative element
    PositiveEle = 0
    for curr in range(len(lst)):
        if(lst[curr]<0):
            if(curr!=PositiveEle):
                lst[curr],lst[PositiveEle] = lst[PositiveEle],lst[curr]
            PositiveEle+=1
    return lst

print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
