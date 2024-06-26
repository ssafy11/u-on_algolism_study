# -------------- 딕셔너리 사용하라는 힌트 듣고 해보는 버전..
def solution(weights):
    weights.sort()
    jjack = {}
    answer = 0
    for i in weights:
        if i in jjack:
            answer += jjack[i]
            jjack[i] += 1
        else:
            jjack[i] = 1
        if i * 1 / 2 in jjack:
            answer += jjack[i * 1 / 2]
            
        if i * 2 in jjack:
            answer += jjack[i * 2]
            
        if i * 3 in jjack:
            answer += jjack[i * 3]
            
        if i * 4 in jjack:
            answer += jjack[i * 4]
            
        if i * 3 / 2 in jjack:
            answer += jjack[i * 3 / 2]
        
        if i * 4 / 3 in jjack:
            answer += jjack[i * 4 / 3]
            
        if i * 2 / 3 in jjack:
            answer += jjack[i * 2 / 3]
            
        if i * 3 / 4 in jjack:
            answer += jjack[i * 3 / 4]
            
            
    return answer

#-----------------조합 사용한 실패 버전 
# .. ㅠㅠ! 
from itertools import combinations
def solution(weights):
    weights.sort()
    seesaw = list(combinations(weights, 2))
    see = [1, 2, 3, 4, 3/2, 4/3]
    jjack = 0
    for i in range(len(seesaw)):
        val = seesaw[i][1] / seesaw[i][0]
        if val in see:
            jjack += 1
        
    return jjack
