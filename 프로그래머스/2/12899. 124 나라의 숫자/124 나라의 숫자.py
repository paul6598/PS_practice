def solution(n):
    sol = ""
    strs = ["1", "2", "4"]
    digit = 1
    k = 3
    n -= 1
    while n >= k:
        n -= k
        k *= 3
        digit += 1
    
    while n > 0:
        sol = strs[n%3] + sol
        n //= 3
    sol = "1"*(digit-len(sol))+sol
    return sol
        
