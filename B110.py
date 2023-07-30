from __future__ import annotations
from typing import Final as const

def get_pixcel_datas(row: int) -> list[list[int]]:
    datas: list[list[int]] = []
    for _ in range(row):
        datas.append(list(map(int, input().split(" "))))
    return datas


def px_decomposer(data: list[list[int]], H: int, W: int) -> list[list[list[int]]]:
    sprit_size: const[int] = 2 * H * 2 * W
    result: list[list[list[int]]] = []
    for i in range(s)


def get_high_solution_px(first_img: list[list[int]], second_img: list[list[int]]) -> list[list[int]]:

    result_img: list[list[int]] = []

    for i in range(len(first_img)):
        result_img.append([])
        for j in range(len(first_img[i])):
            result_img[i].append(max(first_img[i][j], second_img[i][j]))

def main():
    inputs = input().split(" ")
    H: const[int] = int(inputs[0])
    W: const[int] = int(inputs[1])
    first_img: const[list[list[int]]] = get_pixcel_datas(H)
    second_img: const[list[list[int]]] = get_pixcel_datas(H)






if __name__ == '__main__':
    main()