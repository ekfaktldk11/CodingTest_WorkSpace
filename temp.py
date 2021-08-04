# n, m = map(int, input().split())
#
# INF = int(1e9)
#
# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
# graph = [[INF] * (n + 1) for i in range(n + 1)]
#
# # (빼먹은 부분) 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0
#
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1 # (빼먹은 부분)
#
# x, k = map(int, input().split())
#
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         for c in range(1, n + 1):
#             graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])
#
# ans = graph[1][k] + graph[k][x]
# if ans >= INF: print(-1)
# else: print(ans)

# ----------------------------------
