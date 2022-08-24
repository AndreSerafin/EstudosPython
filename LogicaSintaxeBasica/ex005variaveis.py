nome = "andre".capitalize()
peso = 80.0
altura = 1.7
idade = 22
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"""Nome: {nome}
Idade: {idade}
Ano atual: {ano_atual}
Ano de nascimento: {ano_nascimento}
Peso: {peso:.2f} Kg
Altura: {altura:.2f}
IMC: {imc:.2f}""")
