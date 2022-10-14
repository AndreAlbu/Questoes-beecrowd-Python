StrDi = input().split()
StrHi = input().split()
StrDf = input().split()
StrHf = input().split()
di,df = int(StrDi[1]),int(StrDf[1])
hhi,mmi,ssi = int(StrHi[0]),int(StrHi[2]),int(StrHi[4])
hhf,mmf,ssf = int(StrHf[0]),int(StrHf[2]),int(StrHf[4])

min_seg = 60
hora_seg = 3600
dia_seg = 86400

ini = ssi + mmi*min_seg + hhi*hora_seg + di*dia_seg
fim = ssf + mmf*min_seg + hhf*hora_seg + df*dia_seg

if ini < fim:
    t = fim - ini
    W = int(t/dia_seg)
    t = t%dia_seg
    X = int(t/hora_seg)
    t = t%hora_seg
    Y = int(t/min_seg)
    t = t%min_seg
    Z = t

print("%d dia(s)" %W)
print("%d hora(s)" %X)
print("%d minuto(s)" %Y)
print("%d segundo(s)" %Z)
