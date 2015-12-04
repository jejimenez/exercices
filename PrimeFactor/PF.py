
def get_prime_factor(num):
    i = 2
    pf = ''
    if num == 1:
        return str(num);
    while i != num:
        if num % i == 0:
            pf = pf + ' ' + str(i)
            num = num / i
            i = 2
        else:
            i += 1
    pf = pf + ' ' + str(i)
    return pf

num1 = int(input(''))

for i in range(num1):
    test = int(input(''))
    print(get_prime_factor(test))
