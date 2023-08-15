from __future__ import annotations
from typing import Final as const


def get_sea_map_data(row: int) -> list[list[int]]:
    data: list[list[int]] = []
    for _ in range(row):
        data.append(list(map(int, input().split(" "))))
    return data

def get_net_data(row: int) -> list[str]:
    data: list[str] = []
    for _ in range(row):
        data.append(input())
    return data


def get_amount(sea_map_data: list[list[int]], net_data: list[str], st: int, end: int) -> int:
    get_amount: int = 0
    for i in range(len(net_data)):
        for j in range(len(net_data[i])):
            if net_data[i][j] == "#":
                
    return get_amount

def cacl_max_catch_amount(sea_map_data: list[list[int]], net_data: list[str]) -> int:

    capture_amounts: list[int] = []
    get_amount = 0
    for i in range(len(sea_map_data)):
        for j in range(len(sea_map_data[i])):
            
            
            


def main():

    inputs = input().split(" ") 
    H: const[int] = int(inputs[0])
    W: const[int] = int(inputs[1])
    map_data = get_sea_map_data(H)
    inputs_2 = input().split(" ")
    R: const[int] = int(inputs_2[0])
    C: const[int] = int(inputs_2[1])
    net_data = get_net_data(R)




if __name__ == '__main__':
    main()