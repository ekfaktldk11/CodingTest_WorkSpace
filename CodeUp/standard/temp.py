str = input()
m = int(str[1])
n = ord(str[0]) - ord('a') + 1

count = 0
# case m_long
if(m + 2 <= 8):
    if (n + 1 <= 8): count += 1
    if (n - 1 > 0): count += 1
if(m - 2 > 0):
    if (n + 1 <= 8): count += 1
    if (n - 1 > 0): count += 1

# case n_long
if(n + 2 <= 8):
    if (m + 1 <= 8): count += 1
    if (m - 1 > 0): count += 1
if(n - 2 > 0):
    if (m + 1 <= 8): count += 1
    if (m - 1 > 0): count += 1


print(count)

# --------------------------------------------------------

