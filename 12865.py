#12865 평범한 배낭, 20210818
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0]*(k+1) #무게별 가치의 최대치를 저장하는 리스트 arr
for w, v in items : 
    if w > k : continue
    #arr의 최상단 k부터 시작해 w까지 하나씩 내려오면서 arr 업데이트
    for i in range(k, w-1, -1) : 
        #arr의 인덱스가 큰 쪽이 밸류도 더 크다는 사실이 보장되어있으므로 기존의 arr[i]와 v + arr[i-w]를 비교해주고 업데이트한다. 
        if arr[i] < v + arr[i-w] : 
            arr[i] = v + arr[i-w]
print(arr[-1])
#33052kb, 2580ms