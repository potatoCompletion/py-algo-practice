# 먼저 반복문으로 풀어보자
# 1. 하나는 역순으로 하나는 정방향으로 한글자씩 옮겨가면서 비교, 다르면 그 즉시 False
# 2. 두개의 인덱스의 차이가 1이거나 같으면 종료

input = "abcba"

def is_palindrome(string):
    string = string.replace(" ", "")
    for i in range(len(string) - 1):
        forward_index = i
        reverse_index = len(string) - 1 - i
        forward_char = string[i]
        reverse_char = string[len(string) - 1 - i]

        if forward_char != reverse_char:
            return False

        if reverse_index - forward_index == 1 or forward_index == reverse_index:
            break

    return True



print(is_palindrome("우영우"))
print(is_palindrome("역삼역"))
print(is_palindrome("기러기"))
print(is_palindrome("토마토"))
print(is_palindrome("오디오"))
print(is_palindrome("아시아"))
print(is_palindrome("일요일"))
print(is_palindrome("소주만병만주소"))
print(is_palindrome("가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가"))
print(is_palindrome("이건실패해야정상"))