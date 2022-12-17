"""
rankJ1.py

For (M,N), whether the rank of J_1(M,MN)(\Q(\zeta_M)) = 0 or not?
By my paper, its rank over \Q(\zeta_M) is 0 iff that one of it over \Q is 0,
and only what we need to compute is (3,7), (3,14), (3,16), (4,5), (4,9), (6,4), and (12,1).

We compute that these ranks are 0 except (M,N) = (4,9).

202212101756


"""

from sage.all import *


S = [ [3,7], [3,14], [3,16], [4,5], [4,9], [6,4], [12,1] ]

for a in S:
    m = a[0]
    n = a[1]
    print("For each normalized eigenform f of level Gamma_1(%d, %d), is L(f,1) = 0?" % (m,m*n))

    for d in divisors(m*m*n):
        NF = Newforms(Gamma1(d), names='a')
        for f in NF:
            if m*n % f.character().conductor() == 0:
                A = f.abelian_variety()
                L = A.lseries()
                van = L.vanishes_at_1()
                print(van)
                if van:
                    print("L(f,1) = 0 for f = ", f)




################################################
# OUTPUT
################################################

"""
For each normalized eigenform f of level Gamma_1(3, 21), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(3, 42), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(3, 48), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(4, 20), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(4, 36), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
False
False
False
False
True
L(f,1) = 0 for f =  q - a2*q^3 + (2*a2 - 6)*q^5 + O(q^6)
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(6, 24), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
False
False
False
False
False
For each normalized eigenform f of level Gamma_1(12, 12), is L(f,1) = 0?
False
False
False
False
False
False
False
False
False

"""