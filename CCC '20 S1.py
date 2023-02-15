first = int(input())
all = []
for i in range(first):
    newInput = input()
    temp = (newInput.split())
    newList = []
    newList.append(int(temp[0]))
    newList.append(int(temp[1]))
    all.append(newList)
all.sort()
speeds = []
for i in range(len(all) - 1):
    speeds.append(abs((all[i+1][1] - all[i][1]) / (all[i+1][0] - all[i][0])))
print(max(speeds))