# 오름차순 정렬된 숫자 리스트
# 이진 탐색으로 특정 숫자 존재하는지 검색
# 1. 첫번째 인덱스와 마지막 인덱스의 절반 값을 찾고 해당 인덱스를 조회해서 타겟 숫자인지 검증한다.
# 2. 타겟이 조회한 숫자보다 크면 첫번째 인덱스를 타겟 인덱스로 바꾸고 작으면 마지막 인덱스를 타겟 인덱스로 변경
# 3. 1, 2번을 타겟이 나올때 까지 반복한다. 만약 첫번째 인덱스와 마지막 인덱스가 같아지면 종료

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:
        find_target_index = (first_index + last_index) // 2
        if array[find_target_index] == target:
            return True

        if target > array[find_target_index]:
            first_index = find_target_index + 1
        else:
            last_index = find_target_index - 1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)