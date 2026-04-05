# 출석하지 않은 학생의 이름을 반환
# 해시 테이블을 이용해서 풀어보자(파이썬의 딕셔너리)
# 1. 현재 학생들을 dict에 저장
# 2, 모든 학생 배열을 순회하면서 dict에 있는지 확인

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}

    for present_student in present_array:
        dict[present_student] = True

    for student in all_array:
        if dict.get(student):
           continue
        else:
            return student

    return -1


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))