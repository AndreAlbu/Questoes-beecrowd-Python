N = 1

while(N != 0):

    N = int(input())

    if(N != 0):

        coutA = 0
        coutB = 0

        for i in range(N):

            A, B = map(int, input().split())

            if(A > B):

                coutA = coutA + 1

            else:

                coutB = coutB + 1
            
        print(coutA, coutB)