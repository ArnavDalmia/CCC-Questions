line = input()
p = 0
n = 0

for i in range(len(line)-2):
    if line[i:i+3] == ":-)":
        p += 1
    if line[i:i+3] == ":-(":
        n += 1
        
if (p == 0 and n == 0):
    print("none")
elif p > n:
    print("happy")
elif p < n:
    print("sad")
elif p == n:
    print("unsure")
