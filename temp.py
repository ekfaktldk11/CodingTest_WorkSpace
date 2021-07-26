# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))

# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위하 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += (x - mid)
    # 떡의 양이 부족한 경우 (search left part)
    if total == m:
        print(mid)
    # 떡의 양이 충분한 경우 (search right part)
    elif total < m:
        end = mid - 1
    else:
        result = mid # !!! 최대한 덜 잘랐을 때가 정답이므로, result 를 계속 기록
        start = mid + 1

# 정답 출력
print(result)