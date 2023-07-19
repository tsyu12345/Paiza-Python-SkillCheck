from __future__ import annotations
from typing import Final as const


def get_area_datas(size: int) -> list[str]:
    datas = []
    for i in range(size):
        datas.append(input())
    return datas

def data_deconposer(datas: list[str]) -> list[list[str]]:
    return [list(data) for data in datas]


def cacl_rope_count(area_datas: list[list[str]], flower: str) -> int:
    
    count: int = 0
    for i, row in enumerate(area_datas):
        for j, cell in enumerate(row):
            if cell == flower: #花のあるマスに入ったら計算開始
                #４辺のマスに花が存在しているか確認し、必要なロープの数を計算する
                
                if i == 0 or area_datas[i-1][j] != flower: #上
                    count += 1
                if i == len(area_datas)-1 or area_datas[i+1][j] != flower: #下
                    count += 1
                if j == 0 or area_datas[i][j-1] != flower:
                    count += 1
                if j == len(row)-1 or area_datas[i][j+1] != flower:
                    count += 1
    return count
                
                



    
def main():

    inputs = input().split(' ')
    H: const[int] = int(inputs[0])
    W: const[int] = int(inputs[1])
    datas: list[str] = get_area_datas(H)
    area_datas: list[list[str]] = data_deconposer(datas)

    print(cacl_rope_count(area_datas, '#'))





if __name__ == '__main__':
    main()