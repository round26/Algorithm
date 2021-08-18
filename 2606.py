import sys

num_pc = int(sys.stdin.readline()) # 컴퓨터 개수 받기
link_num = int(sys.stdin.readline()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

input_list = [] # 컴퓨터 연결 관계 (이차원 배열)
infect_list = [1, ] # 감염된 컴퓨터 리스트

for ind in range(link_num):
    input_list.append(list(map(int, sys.stdin.readline().split())))
    # print(input_list) # to check the input_list
###############################################################################

input_list.sort() # 1과 연결된 게 제일 앞에 옴
# print('sorted input_list: ', input_list)

i = 0
while i < link_num:
    if input_list[i][0] in infect_list:
        infect_list.append(input_list[i][1])
    elif input_list[i][1] in infect_list:
        infect_list.append(input_list[i][0])
    i += 1

i = link_num-1
while i > 0:
    if input_list[i][0] in infect_list:
        infect_list.append(input_list[i][1])
    elif input_list[i][1] in infect_list:
        infect_list.append(input_list[i][0])
    i -= 1

infect_list = set(infect_list)
# print('final infect_set: ', infect_list)
result = len(infect_list)-1 # 1 제외

print(result)

'''
i = 0
temp_ind = 0
inf_ind = 0
while 1:
    while i < link_num:
        if input_list[i][0] == infect_list[inf_ind]:
            infect_list.append(input_list[i][1])
        elif input_list
    
    if len(infect_list) == inf_ind+1:
        i += 1
    else: inf_ind += 1
'''    