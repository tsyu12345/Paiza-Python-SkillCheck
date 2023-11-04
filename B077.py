from __future__ import annotations
from typing import Final as const



def get_purchase_durationTime(size: int) -> list[int]:
    result: list[int] = []
    for i in range(size):
        result.append(int(input()))
    return result

def get_total_time(t_i: list[int], persons: list[bool]) -> int:
    now_time: int = 0
    counter_status: list[bool] = [False] * len(t_i)
    print(persons)
    while False in persons:
        #print(counter_status)
        for person_no in range(len(persons)):
            #カウンターへの割り当て判定
            for counter_num, status in enumerate(counter_status):
                if status == False:
                    counter_status[counter_num] = True
                    break
                if now_time == t_i[counter_num]:
                    counter_status[counter_num] = False if counter_status[counter_num] == True else True
                    persons[person_no] = True
            if False not in counter_status:
                break
        now_time += 1
    return now_time



def main():
    inputs = input().split(" ")
    N: const[int] = int(inputs[0]) #カウンター数
    M: const[int] = int(inputs[1]) #待機中の人数
    t_i: const[list[int]] = get_purchase_durationTime(N)
    persons: list[bool] = [False] * M
    print(get_total_time(t_i, persons))
    
    




if __name__ == '__main__':
    main()