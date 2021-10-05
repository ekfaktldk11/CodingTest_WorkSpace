'''
- 잃어버린 괄호
- https://www.acmicpc.net/problem/1541
'''

# 내 풀이 (힌트 얻고 해결 ㅠ)
str1 = input().split('-') # - 기준으로 괄호를 씌움
total = 0
first_item = str1[0].split('+') # 첫번째 값은 무조건 + , 첫번째 값에 뒤 따라오는 숫자들도 다 더해줘야함
for num in first_item: total += int(num)
for i in range(1, len(str1)): # 나머지 들은 괄호를 기준으로 빼줌
    li = str1[i].split('+')
    for num in li: total -= int(num)

print(total)

'''
# 결론
- '+' , '-' 로만 구성된 식은 '-' 기준으로 괄호를 묶고, '-'에서 다음 '-'가 나올 때 까지 해당 숫자들을 더해주고 빼주면 최소값을 구할 수 있다는 접근이 중요
'''