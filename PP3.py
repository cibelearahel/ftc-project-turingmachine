fita = []
x=[]
D = 1
E = -1
P= 0
b = 3

kbsote = 0


enter = {'inicial': 0, 'aceita': 1, 'rejeita': 2, 'delta': [(0,0,0,1,D),(0,0,1,0,D),(0,3,b,b,E),(3,1,0,0,P),(3,1,1,1,P)]}

num_pal = int(input())
fita = [int(a) for a in str(num_pal)]

for i in range(3):
    for k in range(3):
        if fita[k] == 0:
            fita[k] = 1
        else:
            fita[k] = 0

print(fita)

