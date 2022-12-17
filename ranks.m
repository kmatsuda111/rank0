

/*
The proof of Lemma 3.5.

202212101907
*/




S0 := {1..36} join {38..42} join {44..52} join {54,55,56,59,60,62,63,64,66,68,69,70,71,72,75,76,78,80,81,84,87,90,94,95,96,98,100,104,105,108,110,119,120,126,132,140,144,150,168,180};
// The set of N such that the rank of J_0(N)(Q) is zero.
S00 := S0 diff {63,80,95,104,105,126,144};
// The set of N such that the rank of J_1(N)(Q) is zero.

// See Derickx, Etropolski, van Hoeij, Zureick-Brown, Sporadic cubic torsion


S := [{ 0 }];
for M in [2..12] do;
S[M] := { N : N in [1..180*M^2] | M^2 * N in S0 and M * N in S00};
    M, S[M];
end for;
// If the rank of J_1(M,MN)(Q(zeta_M)) is zero then the ranks of J_0(M^2N)(Q) and one of J_1(MN)(Q) are zero.


for M in [2..12] do;
S[M] := { N : N in [1..180*M^2] | M^2 * N in S00};
    M, S[M];
end for;
// If the rank of J_1(M^2N)(Q) is zero then the rank of J_1(M,MN)(Q(zeta_M)) is zero.



/*

////////////////////////////////////
//OUTPUT
////////////////////////////////////


2 { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
24, 25, 26, 27, 30, 33, 35, 36, 42, 45 }
3 { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20 }
4 { 1, 2, 3, 4, 5, 6, 9 }
5 { 1, 2, 3, 4, 6 }
6 { 1, 2, 3, 4, 5 }
7 { 1, 2 }
8 { 1 }
9 { 1 }
10 { 1 }
11 {}
12 { 1 }
2 { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24,
25, 27, 30, 33, 35, 42, 45 }
3 { 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 20 }
4 { 1, 2, 3, 4, 6 }
5 { 1, 2, 3, 4, 6 }
6 { 1, 2, 3, 5 }
7 { 1, 2 }
8 { 1 }
9 { 1 }
10 { 1 }
11 {}
12 {}


*/