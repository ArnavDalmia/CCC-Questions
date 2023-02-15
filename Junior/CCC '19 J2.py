n = int(input())

for i in range(n):
  code = str(input())
  parts = code.split(" ")
  print(parts[1]* int(parts[0]))
