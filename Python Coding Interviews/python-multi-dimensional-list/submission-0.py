from typing import List
import math

def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list = [0] * len(nested_arr)
    for i in range(len(nested_arr)):
        max_list[i] = nested_arr[i][0]
        for j in range(1, len(nested_arr[i])):
            max_list[i] = max(max_list[i], nested_arr[i][j])
    return max_list






# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
