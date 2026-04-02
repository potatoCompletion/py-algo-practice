# 재귀적으로 풀어보자
# 1. 문자열 슬라이싱을 이용해 재귀적으로 호출
# 2. 맨앞, 맨뒤를 비교하고 이상없으면 자르고 재귀호출


input = "소주만병만주소"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1]) # 맨 앞, 맨 뒤 자르고 재귀호출


print(is_palindrome(input))