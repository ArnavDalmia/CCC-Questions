A_3 = (int(input())* 3)
A_2 = (int(input())* 2)
A_1 = int(input())
B_3 = (int(input())* 3)
B_2 = (int(input())* 2)
B_1 = int(input())

A_P = A_3 + A_2 + A_1
B_P = B_3 + B_2 + B_1

if A_P > B_P:
  print("A")
if A_P < B_P:
  print("B")
if A_P == B_P:
  print("T")
