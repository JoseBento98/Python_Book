#Objetivo: fazer um pequeno programa contendo conceitos basicos do python
import time
#biblioteca usada para fazer o código rodar de maneira mais natural

#Variaveis e entrada de dados
    #Pdrão Sanke_case
print("Então o Sr(a). vai me falar")
first_name = input("Seu primeiro nome: ")
second_name = input("Seu segundo nome: ")
print("Carregando...")
time.sleep(2)

age = int(input(f"Qual é a idade do Sr(a).{first_name}: "))
print("Carregando...")
time.sleep(2)
    #Entrada de Dados Pessoais
print(f"Seja bem vindo Sr.(a){first_name} {second_name} é um prazer lhe conhecer")
print(f"Agora sei que você tem {age} anos de Idade!")
print("Passando para Proxima Fase...")
time.sleep(2)

print(f"Agora me diga Sr.(a):{first_name} {second_name}, Qaunto você ganha por mês? ")
remnuneration = float(input("Quanto você recebe mensalmente? "))
print("Carregando...")
time.sleep(1)

    #Entrata de dados para função
worked_days = int(input("Quantos dias do Mês você trabalha? "))
worked_hours = float(input("Quantas Horas por dia? "))
print("Carregando...")
time.sleep(1)

    #Função para calculo do valor da remuneração por hora
earnings_per_hour = (remnuneration / worked_days) / worked_hours

print(f"Sr(a) {first_name} {second_name} ganha aproximadamente {earnings_per_hour:2.2f} $ por Hora trabalhada!")
print("Seu Nick Name é: ", first_name, age, sep="#",end="@" )


#Condições
#Repetições
#Lista,Dicionarios,tupulas e conjuntos
#Trabalhando com Strings
#Funções
#Arquivos
#Classes e Objetos
#Banco de Dados