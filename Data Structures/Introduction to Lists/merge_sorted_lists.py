#Problem Statement: 
#Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).


def merge_lists(lst1, lst2):
    # Write your code here
    res = []
    p1,p2= 0,0
    while(p1<len(lst1) and p2<len(lst2)):
        if(lst1[p1]<lst2[p2]):
            res.append(lst1[p1])
            p1 = p1+1
        else:
            res.append(lst2[p2])
            p2 = p2+1
    if(p2<len(lst2)):
        res.extend(lst2[p2:])
    if(p1<len(lst1)):
        res.extend(lst1[p1:])
    return res


print(merge_lists([1,3,4,5],[2,6,7,8]))
