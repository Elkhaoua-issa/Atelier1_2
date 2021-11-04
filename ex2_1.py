l1=[]
n = int(input("Entrez le nombre des element de tableau 1: "))
print("Entrez les elements de tableau:")
for i in range(0, n):
    ele = int(input(f"l1[{i}]: "))
    l1.append(ele)
l2=[]
n = int(input("Entrez le nombre des element de tableau 2: "))
print("Entrez les elements de tableau:")
for i in range(0, n):
    ele = int(input(f"l2[{i}]: "))
    l2.append(ele)
l3=[]
for i in range(0,len(l1)):
    if i%2!=0:
        l3.append(l1[i])
for i in range(0,len(l2)):
    if i%2==0 or i==0:
        l3.append(l2[i])

print(l3)

