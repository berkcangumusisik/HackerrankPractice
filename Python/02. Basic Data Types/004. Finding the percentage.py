
# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem

def readScores(listOfStudents):
    line = list(input().split())
    avScore = sum(map(float, line[1:])) / 3
    name = line[0]
    listOfStudents[name] = avScore
    
n = int(input())
studentMarks = {}
for _ in range(n):
        readScores(studentMarks)
print('%.2f' % studentMarks[input()])
