# 2차원 리스트를 90도 회전한(시계방향) 결과를 반환하는 함수

# 관련 문제 : https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

