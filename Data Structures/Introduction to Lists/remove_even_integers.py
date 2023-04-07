#Problem Statement:  
#Implement a function that removes all the even elements from a given list. Name it remove_even(lst).


def remove_even(lst):
    return [x for x in lst if x%2==1]

print(remove_even([1,2,4,5,10,6,3]))
