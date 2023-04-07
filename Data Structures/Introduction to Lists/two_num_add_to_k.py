#Problem Statement
#In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

def find_sum_brute(lst, k):
    # Write your code here
    for x in range(0,len(lst)):
        for y in range(x+1,len(lst)):
            if(lst[x]+lst[y]==k):
                return [lst[x],lst[y]]

print(find_sum_brute([1,21,3,14,5,60,7,6],81))


def find_sum(lst, k):
    # Write your code here
    dic = {}
    for num in lst:
        diff = k - num
        dic[num] = diff
        if(diff in dic):
            return [diff,num]

print(find_sum([1,21,3,14,5,60,7,6],81))