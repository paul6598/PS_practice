def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    curr = -30001
    for route in routes:
      if curr < route[0]:
        answer += 1
        curr = route[1]
    return answer