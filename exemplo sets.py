A = set()
A.add(1)
A.add(2)
A.add(3)
A.add(4)

B = set()
B.add(2)
B.add(3)
B.add(5)
B.add(6)

print(A | B)#Ou A.union(B) 'união de A com B'
print(A.difference(B))#Ou A - B 'diferença de A pra B'
print(A.intersection(B))#Ou A & B 'Elementos que tem A e B
(B.update(A))#Atualiza o conjunto B com o conjunto A
print(B)
