from typing import List

def read_integers() -> List[int]:
    li = []
    li_str = list(input().split(","))
    for num_str in li_str:
        li.append(int(num_str))
    return li

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
