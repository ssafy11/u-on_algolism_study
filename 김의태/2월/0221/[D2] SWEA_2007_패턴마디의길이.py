# 42,480 kb 101 ms
# idea : 체크할 길이를 점점 넓혀가주고, 해당 길이만큼 구간 이동해서 체크.
t = int(input())
for k in range(0, t):
    string = input()
    for i in range(1, 11): #최대 마디는 10마디이니까 그냥 무식하게 슬라이싱
        if string[:i] == string[i:2*i]: #두배 간격으로 같으면 정답
            print(f'#{k+1} {i}')
            break
