N = int(input())

first = input()
second = input()
sim = 0

for i in range(N):
  if first[i] == second[i] and first[i] != ("."):
    sim += 1
    
print(sim)
