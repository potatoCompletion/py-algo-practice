# 1. 문장 루프 돌면서 해당 알파벳 나올때마다 map에 추가
# 2. map 루프 돌면서 앞에서부터 max alphabet 찾기

def find_max_occurred_alphabet(sentence):
    alphanet_occurrence_array = [0] * 26
    for ch in sentence:
        if ch.isalpha():
            alphanet_occurrence_array[ord(ch) - ord('a')] += 1

    max_ascii = 0
    max_occurrence = 0;
    for i in range(len(alphanet_occurrence_array)):
        if alphanet_occurrence_array[i] > max_occurrence:
            max_occurrence = alphanet_occurrence_array[i]
            max_ascii = i

    return chr(max_ascii + ord('a'))



result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))