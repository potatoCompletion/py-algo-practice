# 무작위 숫자 리스트
# 무작위 숫자리스트는 그냥 순차탐색으로 찾는게 더 효율적이다
# 순차탐색: O(n)
# 정렬 + 이진탐색: O(n log n) + O(log n)

finding_target = 3
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_existing_target_number_binary_random(target, array):
    for num in array:
        if num == target:
            return True

    return False


result = is_existing_target_number_binary_random(finding_target, finding_numbers)
print(result)