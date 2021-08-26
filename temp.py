def solution(tickets):
    # [(1, 2), (1, 1)], [[1, 2], [1, 1]] 를 sort()든 sorted()든 사용하여 정렬하면 [(1, 1), (1, 2)], [[1, 1], [1, 2]] 로 정렬됨

    tickets.sort(reverse=True)  # 스택 형식을 사용하기 때문에 reverse=True
    routes = dict()  # routes = {}
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]  # 'port_name' : [dest1, dest2 ...]
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            ans.append(st.pop())  # 출발지 또는 경유지 목록에 없기에 도착지점일 수 밖에 없는 port_name을 미리 ans 배열에 넣음 or 더이상 port_name에 대한 dest가 존재하지 않을 경우
        else:
            st.append(routes[top].pop())  # 순서가 거꾸로 정렬된 dest 리스트를 뒤에서 부터 뽑아내어 순서에 맞게 -> 나중에 ans.append()로 해당 dest 가 추가 될때 다시 거꾸로 저장되어 밑의 ans.reverse()에서 순서에 맞게 정렬됨
    ans.reverse()
    return ans