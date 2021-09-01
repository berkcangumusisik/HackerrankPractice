# PROBLEM: https://www.hackerrank.com/challenges/py-set-add/problem

n= int(input())

names = set([])

for i in range(n):
    names.add(input())
print(len(names))