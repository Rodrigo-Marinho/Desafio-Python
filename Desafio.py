lista = []
n = int (input ('Quais são o número de vagas?'))
m = int (input ('Qual o número esperado de clientes?'))
if 1<=n<=1000 and 1<=m<=1000:
    for i in range (1,m+1):
        v_i = input ('Qual vaga?')
        if v_i not in lista:
            lista.append(v_i)
else:
    print ('Um dos números é invalido')
x = len(lista)
print (x)
