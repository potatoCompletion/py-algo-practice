# 1. 0과 1로만 이루어진 문자열
# 2. 연속된 하나 이상의 숫자를 잡고 모두 뒤집기만 가능
# 3. 처음부터 하나씩 순회하면서 보다가 이전과 다른 문자가 나오면 기록, 그리고 이어서 순회하면서 또 다른문자가 나오면 기록
# 4. 순회하면서 0과 1을 각각 연속된 덩어리가 몇개 씩 있는지 카운트 (ex: 1001110 이면, 1은 2덩이, 0도 2덩이)
# 5. 더 적은 연속된 덩어리를 뒤집으면 되니까 답은 2 (더 적은 덩어리 숫자와 같음)

input = "11101101"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_list_count = 0
    one_list_count = 0
    prefer_character = '-' # 의미없음

    for c in string:
        if c != prefer_character:
            if c == '0':
                zero_list_count += 1
            if c == '1':
                one_list_count += 1

            prefer_character = c

    return min(zero_list_count, one_list_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)