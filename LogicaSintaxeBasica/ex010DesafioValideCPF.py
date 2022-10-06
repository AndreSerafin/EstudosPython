chars = ".-"
cpf = "021.133.461-84".translate(str.maketrans('','',chars))

for i in cpf:
    print(i)