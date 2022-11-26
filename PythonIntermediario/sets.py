# Criando um set
# set(iterável) ou {1,2,3}

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}

s3 = s1 | s2 # Uniao | une os dois sets
s4 = s1 & s2 # Intersecção & itens presentes nos dois sets
s5 = s1 - s2 # Diferença - itens presentes apenas no set da esquerda
s6 = s1 ^ s2 # Diferença simétrica ^ Itens que não estão em ambos

print(s3)
print(s4)
print(s5)
print(s6)
