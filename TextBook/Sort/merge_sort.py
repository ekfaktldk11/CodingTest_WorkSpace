# 병합(=합병) 정렬 - divide and conquer
def merge_sort(list): # divide
    if len(list) <= 1: return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right): # conquer
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
    return result

"""
 1. merge_sort() 로 리스트를 최소 단위로 divding
 2. merge() 로 왼쪽 오른쪽 각 리스트에서 작은 놈을 빼내서 넣음
 
 # 결론
 - 하나의 큰 문제를 여러개의 작은 문제로 나누어서 이 작은 문제들을
 풀면서 큰 문제를 해결하는 방법임
 - 왼쪽리스트 및 오른쪽리스트가 각각 정렬되어있다는 것을 보장해야만
 왼쪽 오른쪽의 첫 요소들을 비교하면서 합칠 수 있음!
 
 
 출처 : https://starblood.tistory.com/entry/merge-sort-in-Python-Python-%EC%9C%BC%EB%A1%9C-merge-sort-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
"""