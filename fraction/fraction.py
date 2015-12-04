
def get_fraction(num,den):
    i = num
    while num % i != 0 or den % i != 0:
        i -= 1
    return num/i, den/i

num = float(input(''))
den = 10000

if num >= 0.0001 and num <= 0.9999:
    num = num * den
    num, den = get_fraction(num,den)
    print(str(num)+"/"+str(den))
