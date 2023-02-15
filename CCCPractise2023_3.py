first = int(input())

poss = []
for i in range(1000):
    poss.append(i+1)
poss.sort(reverse=True)

full = []
for i in range(first):
    full.append(int(input()))

correspondingToPoss = [] # 0,0,0 etc holds counts of each number in poss
for i in poss:
    correspondingToPoss.append(full.count(i))


number = max(correspondingToPoss)
if number > 1:
    indexOf = correspondingToPoss.index(number)
    RealNumber = poss[indexOf]
    correspondingToPoss[indexOf] = -123

    secondNumber = max(correspondingToPoss)
    indexOf = correspondingToPoss.index(secondNumber)
    RealNumberSec = poss[indexOf]
    print(abs(RealNumber - RealNumberSec))
else:
    print(abs(max(full) - min(full)))



