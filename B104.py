from __future__ import annotations
from typing import Final as const


def get_answer_datas(count: int) -> list[list[str]]:
    datas: list[list[str]] = []
    for _ in range(count):
        datas.append(input().split(" "))
    return datas


def conv_question_data_by_person(datas: list[list[str]], question_no: int) -> list[str]:
    """元データを列を指定の設問、行を解答者一覧に変更する"""
    question_data: list[str] = []
    for data in datas:
        question_data.append(data[question_no])
    return question_data


def calc_avg(datas: list[int]) -> int:
    """平均値を算出する"""
    #print(datas)
    return int(sum(datas) / len(datas)) if len(datas) > 0 else 0


def cleansing_data(datas: list[str]) -> list[int]:
    clean_datas = []
    for i in range(len(datas)):
        #0以上100以下の整数でないデータは除外
        if datas[i].isdecimal() and 0 <= int(datas[i]) <= 100:
            clean_datas.append(int(datas[i]))
            
    #print(datas)
    return clean_datas

def main():
    inputs = input().split(" ")
    N: const[int] = int(inputs[0])
    M: const[int] = int(inputs[1])
    datas: const[list[list[str]]] = get_answer_datas(N)

    result_avg: list[int] = []
    questions_result: list[list[str]] = []
    for i in range(M):
        questions_result.append(conv_question_data_by_person(datas, i))
    #print(questions_result)
    for question_result in questions_result:
        #print(question_result)
        result_avg.append(calc_avg(cleansing_data(question_result)))
    
    for avg in result_avg:
        print(avg)
    


if __name__ == "__main__":
    main()