from collections import deque

N = int(input())
K = int(input())

computer_list = [[] for i in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    computer_list[a].append(b)
    computer_list[b].append(a)

visited = [False]*(N+1)

q = deque()
q.append(1)
count = -1
while q:
    node = q.popleft()
    if visited[node] == False :
        visited[node] = True
        count +=1
        for i in computer_list[node]:
            q.append(i)
print(count)