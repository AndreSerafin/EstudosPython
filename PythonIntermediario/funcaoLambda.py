def executa (funcao, *args):
    return(funcao(*args))


print(executa(lambda x, y: x + y, 2, 3), executa(lambda x, y: x + y, 5, 6))

duplica = executa(lambda m: lambda n : n * m, 2)

print(duplica(3))


print(executa(lambda *args: sum(args),12,3,4,))

