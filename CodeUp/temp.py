# import sys
# maze = []
# for i in range(10):
#     maze.append(list(map(int, sys.stdin.readline().split)))

maze = []
for i in range(10):
    temp = input().split()
    for j in range(10):
        temp[i] = int(temp[i])
    maze.append(temp)

x, y = 1, 1
while (1):
    maze[x][y] = 9
    if (maze[x][y + 1] == 1):
        if (maze[x + 1][y]):
            break
        else:
            x = x + 1
    elif (maze[x][y + 1] == 2):
        break
    else:
        y = y + 1

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print()