
def maxim(*args):
    maxn = 0
    for a in args:
        if a > maxn:
            maxn = a
    return maxn
    

print('Entrada1')
num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))

maxn = maxim(num1, num2, num3)
print('Maximo numero: '+str(maxn))
while maxn%num1 != 0 or maxn%num2 != 0 or maxn%num3 != 0:
    maxn+=1

print('')
print('')
print('')
print(maxn)
