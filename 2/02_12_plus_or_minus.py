# 음이 아닌 정수로 이루어짐
# 각 숫자들에 알맞은 기호를 사용해서(더하거나 빼거나) 특정한 숫자를 만드려고함. 방법 몇가지 인지 리턴
# -1, +1, +1, +1, +1
# +1, -1, +1, +1, +1
# +1, +1, -1, +1, +1
# +1, +1, +1, -1, +1
# +1, +1, +1, +1, -1
# 1. 재귀적으로 숫자 하나씩 빼서 이전 값에 더하거나 뺀다
# 2. 최종까지 갔을 때 target_number가 반환되면 +!, 아니면 0

# 모든 경우의 수를 구하는 방식을 알아놓자. 대표적인 문제다. 하나의 함수를 만들어놓고 하나는 +1, 하나는 -1 호출하는 형태.
# 그리고 외부(전역)에 기록할 수 있는 자료구조를 만들어놓고 기록한 값 베이스로 답으로 리턴

# 현재 답안은 재귀를 좀 잘 다룰 수 있을 때 return 값을 조정하여 바로 답을 출력.. 노력하자

numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_all_ways_by_doing_plus_or_minus(array, recursive_count, sum, target):
    if recursive_count == len(array):
        return 1 if sum == target else 0

    return (
        get_all_ways_by_doing_plus_or_minus(array, recursive_count + 1, sum + array[recursive_count], target) +
        get_all_ways_by_doing_plus_or_minus(array, recursive_count + 1, sum - array[recursive_count], target)
    )

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    return get_all_ways_by_doing_plus_or_minus(array, 0, 0, target)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!