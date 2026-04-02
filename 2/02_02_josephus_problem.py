# BOJ 1158
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수가 주어진다. 순서대로 k번째 사람을 제거한다. 원에서 사람들이 제거되는 순서를 요세푸스 순열
# 1 2 3 4 5 6 7 (3)  cur_index = 2
# 1 2 4 5 6 7   (6)  cur_index = 4
# 1 2 4 5 7     (2)  cur_index = 1
# 1 4 5 7       (7)  cur_index = 3

def josephus_problem(n, k):
    result_arr = [] # 정답 리스트
    people_arr = list(range(1, n + 1)) # 사람 리스트 생성
    cur_index = k - 1

    while people_arr:
        target = people_arr.pop(cur_index)
        result_arr.append(target)
        if len(people_arr) != 0:
            cur_index = cur_index + k - 1
            max_index = len(people_arr) - 1
            if cur_index > max_index:
                cur_index = cur_index % len(people_arr)

    print(result_arr)




n, k = map(int, input().split())
josephus_problem(n, k)