from __future__ import annotations
from typing import Final as const


def calc_manhattan_distance(p1: list[int], p2: list[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



def main():

    inputs = input().split(" ")
    N: const[int] = int(inputs[0])
    H: const[int] = int(inputs[1])
    W: const[int] = int(inputs[2])
    P: const[int] = int(inputs[3])
    Q: const[int] = int(inputs[4])

    p_q: list[list[int]] = []
    for i in range(N):
        p_q.append(list(map(int, input().split(" "))))

    #最も見やすい席の座標は[P, Q]
    target_seat: list[int] = [P, Q]

    result: list[list[list[int], int]] = []

    #縦の長さH, 横の長さWの座標を全て計算
    for x in range(W):
        for y in range(H):
            p = [y, x]
            if p in p_q:
                continue
            dist = calc_manhattan_distance(target_seat, p)
            result.append([p, dist])
    
    result.sort(key=lambda x: x[1])
    min_dist = result[0][1]
    print(result)

    for [point, dist] in result:
        if dist == min_dist:
            print(f'{point[0]} {point[1]}')
        else:
            continue
    


if __name__ == '__main__':
    main()


    