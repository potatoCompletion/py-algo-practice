# - 장르별로 가장 많이 재생된 노래를 두 곡 씩만 뽑아야함
# - 장르별로 구분해서 가장 많이 플레이된 장르 순으로 내림차순 정렬
# - 해당 장르 중에서 play 순으로 내림차순 정렬 후 append
# - 만약 play 수가 같은 곡이 존재한다면 인덱스가 낮은 순서로 append
# 1. 딕셔너리 사용해서 장르별 총 플레이 수를 기록하자
# 2. 내림차순 정렬
# 3. for 순회하면서 해당 장르 찾고 리스트에 튜플로 각각 (play수, 인덱스) 삽입
# 4. 리스트 정렬하는데 play 수 desc, index asc 로 정렬 후 1, 2번의 인덱스를 result에 삽입

# (플레이수, 인덱스리스트)

def get_melon_best_album(genre_array, play_array):
    genre_dict = {}
    result = []

    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]

        if not genre_dict.get(genre):
            genre_dict[genre] = (play, [i])
        else:
            dict_list = genre_dict[genre][1]
            dict_list.append(i)
            genre_dict[genre] = (genre_dict[genre][0] + play, dict_list)

    prepare_array = sorted(genre_dict.values(), key=lambda x:x[0], reverse=True)

    # 장르는 정렬된 상태
    for element in prepare_array:
        indexes = element[1]
        target_play_list = []

        for index in indexes:
            target_play_list.append((play_array[index], index))

        target_play_list.sort(key=lambda x:(-x[0], x[1]))

        for i in range(min(2, len(target_play_list))):
            result.append(target_play_list[i][1])

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))