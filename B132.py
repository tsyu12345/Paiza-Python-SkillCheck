from __future__ import annotations
from typing import Final as const


def get_passing_times(size: int) -> list[int]:
    return [int(input()) for _ in range(size)]

def calc_blocking_times(passing_time_data: list[int], blocking_st_time: int) -> list[int]:
    
    blocking_time_data: list[int] = []
    
    for i, time in enumerate(passing_time_data):
        blok_time = time - (time - blocking_st_time)
        #次の通過と重なっているか調査
        if i < len(passing_time_data) - 1 and passing_time_data[i+1] <= time + blocking_st_time:
            blok_time += passing_time_data[i+1] - time
        blocking_time_data.append(blok_time)
    
    return blocking_time_data
            
def main():

    inputs = input().split(" ")
    N: const[int] = int(inputs[0])
    c: const[int] = int(inputs[1])
    t_i: const[list[int]] = get_passing_times(N)

    blocking_time_data: list[int] = calc_blocking_times(t_i, c)
    #print(blocking_time_data)

    print(max(blocking_time_data))



if __name__ == '__main__': 
    main()