A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if(A < B and A < C and B < C):

    a = C
    b = B
    c = A

elif(A < B and A < C and C < B):

    a = B
    b = C
    c = A

elif(B < A and B < C and A < C):

    a = C
    b = A
    c = B

elif(B < A and B < C and C < A):

    a = A
    b = C
    c = B

elif(C < A and C < B and A < B):

    a = B
    b = A
    c = C

elif(C < A and C < B and B < A):

    a = A
    b = B
    c = C

elif(A == B and A < C):

    a = C
    b = A
    c = A

elif(A == B and C < A):

    a = A
    b = A
    c = C

elif(A == C and A < B):

    a = B
    b = A
    c = A

elif(A == C and B < A):

    a = A
    b = B
    c = A

elif(B == C and B < A):

    a = A
    b = B
    c = B

elif(B == C and A < B):

    a = B
    b = A
    c = B

else:

    a = A
    b = B
    c = C


if(a >= b + c):

    print("NAO FORMA TRIANGULO")
    
    exit()

if((a * a) == b * b + c * c):

    print("TRIANGULO RETANGULO")

elif((a * a) > b * b + c * c):

    print("TRIANGULO OBTUSANGULO")

elif((a * a) < b * b + c * c):

    print("TRIANGULO ACUTANGULO")

if(a == b and b == c):

    print("TRIANGULO EQUILATERO")

    exit()

if(a == b or a == c or b == c):

    print("TRIANGULO ISOSCELES")