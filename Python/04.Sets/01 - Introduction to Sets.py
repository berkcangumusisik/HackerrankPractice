#PROBLEM: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    s = set(arr)
    return sum(s) / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)