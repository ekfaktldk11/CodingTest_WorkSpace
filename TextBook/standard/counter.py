from collections import Counter

Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

from itertools import combinations
#from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            candidates = combinations(sorted(order), c)
            temp += candidates
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
            # counter에 있는 모든 item들에 대해 하나씩 살펴보기를 f 로 할 때 counter[f] 가 counter.values() 들 중 가장 큰 값과 일치하는 counter f에 대해 answer 이라는 배열에 해당 f 에 있는 문자열을 join한 배열을 더함

    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))