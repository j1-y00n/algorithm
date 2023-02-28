def solution(numbers):
    result = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            result.append(numbers[i] + numbers[j])
    s = set(result)
    answer = sorted(s)

    return answer