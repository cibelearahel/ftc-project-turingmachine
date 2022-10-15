cod = {'inicial': 0, 'aceita': 1, 'rejeita': 2, 'delta': [(0,0,0,1,"D"),(0,0,1,0,"D"),(0,3,"b","b","E"),(3,1,0,0,"P"),(3,1,1,1,"P")]}

entrada = cod
delta = (entrada['delta'])
init = (entrada['inicial'])
accept = (entrada['aceita'])
reject = (entrada['rejeita'])

numero = int(input("int: "))
pal = []
kbsote = 0

for i in range(numero):
    pal.append(input())

for k in range(len(pal)):
    digi = list(pal[k])
    digi.append('b')
    
    for i in range(len(delta)):
        x = str(delta[i][0])
        y = str(delta[i][1])
        u = str(delta[i][2])
        v = str(delta[i][3])
        w = str(delta[i][4])        
        
        if digi[kbsote] == u and init == x:
            init = y
            digi[kbsote] = v

            if w == 'D':
                kbsote += 1
            else:
                kbsote -= 1

        while w != 'P':
            for l in range(len(delta)):
                u = str(delta[i][2])
                x = str(delta[i][0])
                
                if digi[kbsote] == u and init == x:
                    init = y
                    digi[kbsote] = v

                    if w == 'D':
                        kbsote += 1
                    else:
                        kbsote -= 1

    if x == accept:
        print(digi + "ACEITA")
    if x == reject:
        print(digi + "REJEITA")
