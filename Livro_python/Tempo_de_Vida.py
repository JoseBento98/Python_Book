#Objetivo
#criar um Código que calcula o tempo de vida de um Fumante

#Objective
#create a Code that calculates the lifetime of a Smoker

import time 

#1- Quais os Dados de Entrada Necessário 
#2- O que devo fazer com esses dados
#3- Quais as Restrições deste problema
#4- Qual Resultado Esperado
#5- Qual A sequencia de passos a ser feita para chegar ao resultado esperado

print("Vejamos Quanto tempo de vida vc tem !!")
time.sleep(1)

age_person = int(input("Quantos Anos Você Tem ?"))
BASE_YEARS = 85
TIME_LEFT = 0
smoker = input("Voce Fuma? [S/N]")

if smoker == "n" or "N": 
    TIME_LEFT = BASE_YEARS - age_person
    print(f"Seu Tempo restante de vida é: {TIME_LEFT}")
else: 
    smoker == "s" or "S"
    cigarettes_a_day = int(input("Quantos Cigarros você fuma por dia? "))


