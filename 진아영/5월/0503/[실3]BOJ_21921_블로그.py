# 파이썬    58780 KB, 204 ms
# 파이파이 156496 KB, 180 ms
# 범위 보고 시간초과 날거같아서 호준오빠가 예전에 알려준 누적합으로 특정 범위 최댓값 구하기 생각나서 풀어봄

N, X = map(int, input().split())            # N일차, X일동안
todays = list(map(int, input().split()))    # N일동안 방문자 수
accum_todays = [0] * N                      # 새로운 누적합 배열
max_todays = 0
max_count = 0

if set(todays) == {0}:
    print('SAD')
    exit(0)

for i in range(N):
    accum_todays[i] = accum_todays[i-1] + todays[i]  # 새로운 누적합 계산

    # X일 누적합이 쌓였을 때부터
    if i >= X-1:
        if max_todays == accum_todays[i]-accum_todays[i-X]:    # X일동안 방문자수가 max랑 같으면 갯수 추가
            max_count += 1
        elif max_todays < accum_todays[i]-accum_todays[i-X]:   # 더 크면 갱신
            max_todays = accum_todays[i]-accum_todays[i-X]
            max_count = 1
    
print(max_todays)
print(max_count)


# -----근데 이건 왜 틀렸지? 맨 첨엔 누적합 배열 새로 안만들고 있던거 초기화해서 했는데 64에서 틀려서 위에 코드로 제출...------------
# -> 해결! 조건문 범위가 잘못돼서 고쳐서 맞았음, 시간이랑 용량은 위에 코드랑 비슷~

N, X = map(int, input().split())  # N일차, X일동안
todays = list(map(int, input().split()))  # N일동안 방문자 수
max_todays = 0
max_count = 0

# 최댓값 0일 경우에 sad하고 끝내기
if set(todays) == {0}:
    print('SAD')
    exit(0)

for i in range(N):
    # 누적합 구하기
    if i >= 1:
        todays[i] = todays[i-1] + todays[i]

    # X일 누적합이 쌓였을 때부터
    if i >= X-1:
        if i == X-1:                 # 첫번째 누적합 구할때는 그 값이 X일동안 방문자 수
            cur_sum = todays[i]
        else:                        # 아니면 그 값에서 X일 전의 누적합을 빼면 그게 X일동안 방문자 수
            cur_sum = todays[i] - todays[i-X]

        if max_todays == cur_sum:    # X일동안 방문자수가 max랑 같으면 갯수 추가
            max_count += 1
        elif max_todays < cur_sum:   # 더 크면 갱신
            max_todays = cur_sum
            max_count = 1

print(max_todays)
print(max_count)
