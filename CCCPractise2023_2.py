first = int(input())
second = list(map(int, input().split()))
third = list(map(int, input().split()))

totalList1 = []
totalList2 = []
listOfMatchingScores = []


for i in range(first):
    totalList1.append(sum(second[0:i+1]))
    totalList2.append(sum(third[0:i+1]))
    if totalList1[i] == totalList2[i]:
        listOfMatchingScores.append(i)

if len(listOfMatchingScores) == 0:
    print(0)
else:
    print(max(listOfMatchingScores) + 1)



