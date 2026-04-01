# 1. 반복되지 않는 문자
# 2. 알파벳 출현 빈도 수를 기록하고 값이 1인 문자를 기록 (값이 1이라면 반복일수가 없다)
# 3. string을 순차적으로 돌면서 먼저 나온 문자를 반환


def find_not_repeating_first_character(string):
    alphabet_occurence_array = [0] * 26
    for c in string:
        if c.isalpha():
            alphabet_occurence_array[ord(c) - ord('a')] += 1

    not_repeating_alphabet = []
    for index in range(len(alphabet_occurence_array)):
        if alphabet_occurence_array[index] == 1:
            not_repeating_alphabet.append(chr(index + ord('a')))

    if not not_repeating_alphabet:
        return "_"

    for c in string:
        if c in not_repeating_alphabet:
            return c

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))