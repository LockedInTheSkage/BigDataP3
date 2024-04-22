import math

def calc_psi(x,b,m):
    return x*(1-math.e**(-(1-m/b)))


print(calc_psi(1,55,0))
print(calc_psi(10,50,10))