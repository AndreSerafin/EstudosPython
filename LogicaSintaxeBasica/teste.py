valor = float(input())

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for i in range(1,6):
    qtdd_notas = int(valor) // notas[i]
    valor %= notas[i]
    print(f"{qtdd_notas} nota(s) de R$ {int(notas[i]):.2f}")    

moedas = [1,0.5,0.25,0.10,0.05,0.01]

print("MOEDAS:")
for i in range(1,6):
    valor = round(valor,2)
    qtdd_notas = valor / moedas[i]
    valor -= qtdd_notas * moedas[i]
    print(f"{int(qtdd_notas)} moeda(s) de R$ {moedas[i]:.2f}")    
    