#Para representar uma data, temos as variáveis dia, mes e ano:
#Sem alterar as variáveis e sem passar nenhuma string adicional à função print(), 
#como faríamos para ter como resultado da impressão, uma data formatada:

dia = 15
mes = 10
ano = 2015

print(dia, mes, ano, sep='/')
#ou
print("{}/{}/{}".format(dia,mes,ano))
#ou
print(f"{dia}/{mes}/{ano}")

