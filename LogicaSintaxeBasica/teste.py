valor = int(input())

vet = [100, 50, 20, 10, 5, 2, 1]

for i in range(0,7):
    qtdd_notas = int(valor) // vet[i]
    valor %= vet[i]
    print(f"{qtdd_notas} nota (s) de R$ {vet[i]},00")    