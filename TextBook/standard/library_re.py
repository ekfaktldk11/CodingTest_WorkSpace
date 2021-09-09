import re

''' re.search(target, string) '''

# print(re.search('a', 'ab')) # <re.Match object; span=(0, 1), match='a'>
# print(re.search('ab','ababababbbabababaabab')) # <re.Match object; span=(0, 2), match='ab'>
# k = re.search('ab','ababababbbabababaabab')
# print(k.span()) # (0, 2)
# print(k.span()[0]) # 0

''' re.findall(target, string) '''
# print(re.findall('\d', '숫자123이 이렇게56 있다8')) #['1', '2', '3', '5', '6', '8']
# print(re.findall('\d+', '숫자123이 이렇게56 있다8')) #['123', '56', '8']
# print(re.findall('\w', '숫자123이 이렇게56 있다8')) #['숫', '자', '1', '2', '3', '이', '이', '렇', '게', '5', '6', '있', '다', '8']
# print(re.findall('\w+', '숫자123이 이렇게56 있다8')) #['숫자123이', '이렇게56', '있다8']
# print(re.findall('aaa', 'aaaaa')) #['aaa']
# print(re.findall('aaa', 'aaaaaa')) #['aaa', 'aaa']

''' re.split(target, string, max_split_num) '''
# print(re.split('a', 'abaabca')) #['', 'b', '', 'bc', '']
# print(re.split('a', 'abaabca', 2)) #['', 'b', 'abca'] #지정한 수 만큼 쪼개고 그 수가 도달하면 쪼개지 않음

''' re.sub(target, repl, string) '''
str = 'aabaa'
str = re.sub('aa',"",str)
print(str) # 'b'