from __future__ import annotations
from typing import Final as const


def get_work_day_datas(size: int) -> list[list[int]]:

    datas: list[list[int]] = []

    for i in range(size):
        inputs: list[str] = input().split(" ")
        datas.append([int(inputs[0]), int(inputs[1])])

    return datas


def calc_continuous_work(datas: list[list[int]]) -> list[int]:

    continuous_counts: list[int] = []

    for i, data in enumerate(datas):
        continuous_count: int = 0
        st_day = data[0]
        end_day = data[1]
        for j in range(i+1, len(datas)):#どこまで連続しているか調査
            next_st_day = datas[j][0]
            next_end_day = datas[j][1]
            if next_st_day - end_day == 1 or next_st_day == end_day or next_end_day - end_day == 1:
                end_day = next_end_day
            else:
                break
        continuous_count = end_day - st_day + 1
        continuous_counts.append(continuous_count)
    
    return continuous_counts
            



    



def main() -> None:
    
    N: const[int] = int(input())
    datas: list[list[int]] = get_work_day_datas(N)
    continuous_counts: list[int] = calc_continuous_work(datas)
    print(max(continuous_counts))



if __name__ == "__main__":
    main()


