chcker = input()
string  = input()

l = []

for i in range(len(string)):
    temp = (string[i:] + string[:i])
    l.append(temp)
    
ch = True
for i in range(len(l)):
    if l[i] in chcker:
        ch = False
        print("yes")
        break
    else:
        continue

if ch == True:
    print("no")
    