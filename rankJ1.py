"""
rankJ1.py

This is a part of the proof of the Main Theorem.

For each of (M,N) = (3,7), (3,14), (3,16), (4,5), (4,9), (6,4), and (12,1).
and for each newform of level dividing MMN and of conductor dividing MN,
we compute whether the value of its L function at s = 1 is zero or not.

202212101952


"""

from sage.all import *


S = [ [3,7], [3,14], [3,16], [4,5], [4,9], [6,4], [12,1] ]

for a in S:
    m = a[0]
    n = a[1]
    print("For each newform f of level dividing %d and of conductor dividing %d, is L(f,1) = 0?" % (m*m*n,m*n))

    for d in divisors(m*m*n):
        NF = Newforms(Gamma1(d), names='a')
        for i in range(0,len(NF)):
            f = NF[i]
            if m*n % f.character().conductor() == 0:
                A = f.abelian_variety()
                L = A.lseries()
                van = L.vanishes_at_1()
                print(van)
                if van:
                    print("L(f,1) = 0 for f = Newforms(Gamma1(%d), names='a')[%d], whose conductor is %d" % (d, i, f.character().conductor()) )




################################################
# OUTPUT
################################################

"""
For each newform f of level dividing 63 and of conductor dividing 21, is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
For each newform f of level dividing 126 and of conductor dividing 42, is L(f,1) = 0?
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
For each newform f of level dividing 144 and of conductor dividing 48, is L(f,1) = 0?
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
For each newform f of level dividing 80 and of conductor dividing 20, is L(f,1) = 0?
False
False
False
False
False
False
False
False
False
For each newform f of level dividing 144 and of conductor dividing 36, is L(f,1) = 0?
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
L(f,1) = 0 for f = Newforms(Gamma1(144), names='a')[2], whose conductor is 36
False
False
False
False
False
False
False
False
False
For each newform f of level dividing 144 and of conductor dividing 24, is L(f,1) = 0?
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
For each newform f of level dividing 144 and of conductor dividing 12, is L(f,1) = 0?
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