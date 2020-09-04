# -*- coding: utf-8 -*-
"""
In each input list, every number repeats at least once, except for two.

Write a function that returns the two unique numbers.

Examples
returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]

Notes
Keep the same ordering in the output.

"""

def return_unique(lst):
    copy = lst
    output = []
    
    for i in lst:
        counter = 0
        
        for value in copy:
            if i == value:
                counter += 1
        
        if counter == 1:
            output.append(i)
            
    print(output)

return_unique([1, 9, 8, 8, 7, 6, 1, 6])
return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])