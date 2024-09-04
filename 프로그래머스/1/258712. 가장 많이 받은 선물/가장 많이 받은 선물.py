def solution(friends, gifts):
    n = len(friends)
    dic ={i:{j:0 for j in friends} for i in friends}
    gp = {i:0 for i in friends}
    
    for i in gifts:
        a,b = i.split()
        if b in dic[a]:
            dic[a][b] += 1
        else:
            dic[a][b] = 1
        gp[a] += 1
        gp[b] -= 1
        
    sol = {i:0 for i in friends}
    for i in friends:
        for j in friends:
            if i != j:
                if dic[i][j] > dic[j][i]:
                    sol[i] += 1
                elif dic[i][j] < dic[j][i]:
                    sol[j] += 1
                else:
                    if gp[i] > gp[j]:
                        sol[i] += 1
                    elif gp[j] > gp[i]:
                        sol[j] += 1

    answer = max(sol.values())//2
    return answer