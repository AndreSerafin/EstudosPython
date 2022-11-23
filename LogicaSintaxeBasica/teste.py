import ast

perguntas = open('LogicaSintaxeBasica/perguntas.txt', 'r')
p = perguntas.read()

dic = ast.literal_eval(p)

print(dic)