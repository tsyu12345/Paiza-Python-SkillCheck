from __future__ import annotations
from typing import Final as const


def get_sugar_degrees(row: int) -> list[list[int]]:

    datas = []
    for i in range(row):
        d = list(map(int, input().split(' ')))
        datas.append(d)
    return datas


def add_name(l: list[str], name: str, count: int) -> list[str]:
    """
    nameをcount回追加したリストを返す
    """
    for i in range(count):
        l.append(name)
    return l


def split_chocolate(row_data: list[int], first_inspector: str, second_inspector: str) -> list[str]:
    """
    1行分の、均等割りを計算し、分割結果を返す
    """
    result: list[str] = []
    current_suger_sum = 0
    for i, choco in enumerate(row_data):
        current_suger_sum += choco
        #currentの値と残りすべての値の差分を計算
        diff = abs(current_suger_sum - sum(row_data[i+1:]))
        if diff == 0: #均等に分割できた場合
            #読み込んでいるindexまでをfirst_inspector割り当て
            result = add_name(result, first_inspector, i+1)
            #残りをsecond_inspector割り当て
            result = add_name(result, second_inspector, len(row_data) - (i+1))
            break
        else:
            pass
    return result
    

def main() -> None:
    
    inputs: str = input().split(' ')
    H: const[int] = int(inputs[0])
    W: const[int] = int(inputs[1])
    datas: list[list[int]] = get_sugar_degrees(H)

    results: list[list[str]] = []
    #1行ずつ読み込み、均等割りを計算
    for row_data in datas:
        result = split_chocolate(row_data, 'A', 'B')
        results.append(result)
    
    #結果を出力
    #均等割りできていないやつがあるか調べる
    for result in results:
        if len(result) == 0:
            print('No')
            return
    print('Yes')
    for result in results:
        print(''.join(result))
    
            

if __name__ == "__main__":
    main()