n=int(input('enter a number'))

for i in range(0,n):
    for j in range(0,i):
        print(' ',end=' ')
    for k in range(0,2*(n-i)):
        print('*',end=' ')
    for l in range(0,i):
        print(' ',end=' ')
    for m in range(0,i+1):
        print('*',end=' ')
    for o in range(0,2*(n-i)-2):
        print(' ',end=' ')
    for p in range(0,i+1):
        print('*',end=' ')
    for q in range(0,i):
        print(' ',end=' ')
    for r in range(0,2*(n-i)):
        print('*',end=' ')
    for s in range(0,i):
        print(' ',end=' ')               
    print()

for i in range(0,n-1):
    print(' ',end=' ')
print(' *',end='')    
    
for i in range(0,n):
    print(' ',end=' ')

for i in range(0,2*n):
    print('*',end=' ')

for i in range(0,n-1):
    print(' ',end=' ')    
print(' *')    

for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ',end=' ')
    for k in range(0,2*i):
        print('*',end=' ')
    for l in range(0,n-i):
        print(' ',end=' ')
    for m in range(0,n-i+1):
        print('*',end=' ')
    for o in range(0,2*i-2):
        print(' ',end=' ')
    for p in range(0,n-i+1):
        print('*',end=' ')
    for q in range(0,n-i):
        print(' ',end=' ')
    for r in range(0,2*i):
        print('*',end=' ')
    for s in range(0,n-i):
        print(' ',end=' ')          
    print() 

