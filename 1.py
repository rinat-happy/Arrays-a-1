a=[]
sym=0
for i in range(5):
    j=input()
    a.append(j)
    try:
        j=int(j)
    except ValueError:
        x=False
    else:
        x=True
    if(x==True):
        if(j%10==8)and(j%3==0):
            sym=sym+1
print(sym)
