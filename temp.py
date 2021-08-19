words = []
queries = []

for _ in range(6):
    temp = input()
    words.append(temp)

for _ in range(5):
    temp = input()
    queries.append(temp)


def solution(words, queries):
    listify = []
    answer = []

    for _ in range(100001):
        listify.append([])

    for word in words:
        listify[len(word)].append(word)

    for query in queries:

        count = 0
        tail = len(query)
        head = 0

        q_len = len(query)
        if query.find('?') == 0:
            head = query.rfind('?') + 1
        else:
            tail = query.find('?')

        q_str = query[head:tail]

        # q_str, q_len
        if head == 0:
            for word in listify[q_len]:
                if word.find(q_str) == 0: count += 1
        else:
            for word in listify[q_len]:
                if word.rfind(q_str) == (q_len - len(q_str)): count += 1
        answer.append(count)

    return answer


print(solution(words, queries))
