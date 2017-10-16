A1,B1,C1 = map(float,input().split())
A2,B2,C2 = map(float,input().split())

valora = B1*C1
valorb = B2*C2

valor = valora+valorb

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))
