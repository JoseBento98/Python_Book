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
print("Carregando...")
time.sleep(1)

    #Operadores de comparação
BALANCE = 1000
WITHDRAW = 1000

print(BALANCE == WITHDRAW) #Igualdade
print(BALANCE != WITHDRAW) #Diferença
print(BALANCE > WITHDRAW) #Maior_Que
print(BALANCE >= WITHDRAW) #Maior_ou_Igual
print(BALANCE < WITHDRAW) #Menor_que
print(BALANCE <= WITHDRAW) #Menor_ou_igual

    #Atribuição
    #red_stone = 100 #simples
    #red_stone += 100 #atribuição com Adição

    #red_stone = 100 #Com_Subtração
    #red_stone -= 100

    #red_stone = 100 #Com_Multiplicação
    #red_stone *= 100

    #red_stone = 100 #Com_divisão
    #red_stone /= 100

    #red_stone = 100 #Com_Sdivisão inteira
    #red_stone //= 100

    #red_stone = 100 #Com_Modulo(Resto da divisão)
    #red_stone %= 100

    #red_stone = 100 #Com_exponenciação(Square_Root)
    #red_stone **= 100

    #Comparação (e) AND
    #as 2 condições tem que ser TRUE para que a comparação sera TRUE
BALANCE = 1000
WITHDRAW = 1000
LIMIT = 1200

BALANCE >= WITHDRAW and WITHDRAW <= LIMIT

    #Comparação (ou) or
    #uma das condições sendo TRUE o resultado sera TRUE
    #preciso que as 2 seja FALSE para dar FALSE
BALANCE = 1000
WITHDRAW = 1000
LIMIT = 1200

BALANCE >= WITHDRAW or WITHDRAW <= LIMIT

    #comparação (negação) not
    #inverte os valores das condições de TRUE para FALSE...
BALANCE = 1000
WITHDRAW = 1000
LIMIT = 1200

not BALANCE > LIMIT

    #Operador de Identidade IS (é ou não é)
#FOOD = "Barbecue"
#MY_FAVORITE_FOOD = FOOD

#FOOD is MY_FAVORITE_FOOD
#FOOD is not MY_FAVORITE_FOOD

    #Operações Associadas diz se é True Or False elementos pesquisados em listas
profit = "my profit of the month"
food = ["meat", "fruits", "vegetables"]
money = [500,600,1200]

print("month" in profit)

print("Barbecue" not in food)

print(700 in money) 


#Condições


#Repetições
#Lista,Dicionarios,tupulas e conjuntos
#Trabalhando com Strings
#Funções
#Arquivos
#Classes e Objetos
#Banco de Dados