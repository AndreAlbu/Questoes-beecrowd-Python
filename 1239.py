bold, italic = ["<b>", "</b>"], ["<i>", "</i>"]
while True:
    try:
        n,n1 = False, False
        pal = input()
        for i in pal:
            if i == '*':
                if n:
                    print(bold[1], end="")
                    n = False
                else:
                    print(bold[0], end="")
                    n = True
            elif i == '_':
                if n1:
                    print(italic[1], end="")
                    n1 = False
                else:
                    print(italic[0], end="")
                    n1 = True
            else:
                print(i, end="")
        print()
                
    except EOFError:
        break

