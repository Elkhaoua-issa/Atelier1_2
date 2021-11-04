Liste=[47, 64, 69, 37, 76, 83, 95, 97] 
dic={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
lc=[]
tmp=[]
lc=dic.values()
for element1 in Liste:
    c=0
    for element2 in lc:
        if element1 == element2:
            tmp.append(element1)

print(tmp)
    
