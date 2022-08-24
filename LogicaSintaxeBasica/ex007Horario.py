# Faça um programa que pergunte a hora ao usuário e,baseando-se no horário
# descrito,exiba a saudação apropriada.
# Ex.: Bom dia 0-11,Boa tarde 12-17 e Boa noite 18-23.

horario = input("Digite o horario(hh:mm): ")

try:
    horario = horario.split(":")
    horas = int(horario[0])
    minutos = int(horario[1])
    if(horas >= 0 and horas < 12 and minutos < 60):
        print("Bom dia!")
    elif(horas >= 0 and horas < 18 and minutos < 60):
        print("Boa tarde!")
    elif(horas >= 0 and horas <= 23 and minutos < 60):
        print("Boa noite!")
    else:
        print("Horário inválido!")
except:
    print("Horario inválido!")