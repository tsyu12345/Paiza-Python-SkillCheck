from __future__ import annotations
from typing import Final as const


def str_decomposer(string: str) -> list[str]:
    return [char for char in string]

def decryption(chr: str, cipher: list[str]) -> str:
    """
    入力文字1文字を復号する
    """
    #復号の基準となる文字列
    decryption_key: const[str] = 'abcdefghijklmnopqrstuvwxyz'

    chr_index: int = cipher.index(chr)
    return decryption_key[chr_index]

def decodeing_str(count: int, cipher: list[str], encoded_str: str) -> str:
    """
    暗号化された文字列を復号する
    """
    decoded_str: str = ''
    for chr in encoded_str:
        for i in range(count):
            d_tmp = decryption(chr, cipher)
            chr = d_tmp
        decoded_str += chr
    return decoded_str

def main():
    inputs = input().split(' ')
    n: const[int] = int(inputs[0])
    T: const[str] = inputs[1]
    S: const[str] = input()

    cipher: list[str] = str_decomposer(T)
    target_str: list[str] = S.split(' ')
    encode_results: list[str] = []

    for word in target_str:
        encode_results.append(decodeing_str(n, cipher, word))
    
    print(' '.join(encode_results))


if __name__ == "__main__":
    main()