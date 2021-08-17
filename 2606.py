#2606 바이러스, 20210816
import sys
#input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n)]

#그래프 완성하기
for i in range(int(input())) :
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0]*n #방문 여부 확인 리스트 visited
visited[0] = 1
to_visit = [0] #방문해야할 곳 리스트 to_visit
answer = 0

#to_visit의 원소를 하나씩 pop해보고 원소와 연결된 곳 중 아직 방문하지 않은 곳을 체크하는 방식으로 탐색한다.
while(to_visit) :
    num = to_visit.pop()
    for i in graph[num] :
        if not visited[i] :
            visited[i] = 1
            to_visit.append(i)
            answer += 1

print(answer)
#29200kb, 72ms