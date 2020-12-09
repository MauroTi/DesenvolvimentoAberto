# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""


from flask import Flask, render_template, request, redirect, session, flash, url_for
from Cadastro import Cadastro
app = Flask(__name__)


clientes = []


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Acompanha_pedidos")
def pedidos():
    return render_template('fila_pedidos.html')

@app.route("/Cadastro_cliente")
def cadastro_clientes():
    return render_template('cadastro_clientes.html')

@app.route("/Cadastro_pedido")
def cadastro_pedidos():
    return render_template('pedidos.html')

@app.route("/Cardapio")
def cardapio():
    return render_template('cardapio.html')

@app.route("/Login")
def login():
    return render_template('login.html')

@app.route("/Sobre")
def sobre():
    return render_template('sobre.html')





@app.route('/salvar', methods=['post',])
def salvar():
    nome = request. form['nome']
    endereco = request. form['endereco']
    cpf = request. form['cpf']
    telefone = request. form['telefone']
    email = request. form['email']
    cadastro = Cadastro(nome, endereco,cpf, telefone, email)
    
    clientes.append(cadastro)    
    return redirect(url_for('index'))


@app.route('/entrar', methods=['POST',])
def entrar():
    return redirect(url_for('index'))

@app.route('/salvar_pedidos', methods=['post',])
def salvar_pedidos():
        xsalada = request. form['xsalada']
        xcalabresa = request. form['xcalabresa']
       	xlombo = request. form['xlombo']
       	xcoracao = request. form['xcoracao']
       	hsimples = request. form['hsimples']
       	hcasa = request. form['hcasa']
       	csimples = request. form['csimples']
       	ccasa = request. form['ccasa']
       	fritasp = request. form['fritasp']
       	fritasg = request. form['fritasg']
       	refril = request. form['refril'] 
       	refrig = request. form['refrig']
    
       
        return redirect(url_for('index'))

app.run()




# =============================================================================
# Pré-requisitos
# ▹ Um ambiente de programação Python 3.
# ▹ Verifique a versão do python
# 
# python3 --version
# 
# ▹ Atualizando os Pacotes Python(PIP)
# ▹ python -m pip install -- upgrade pip
# 
# Python – MicroFramework Flask
# 
# 23
# 
# ▸ Pré-requisitos
# ▹ Criar um diretório para o projeto virtual
# ▹ python3 -m venv venv
# ▹ Dentro do ambiente ativado, use o
# seguinte comando para instalar o Flask:
# ▹ pip install Flask
# 
# Python – MicroFramework Flask
# 
# 24
# 
# ▸ Testando o ambiente do Flask
# ▹ Para verificar se o Flask foi instalado
# corretamente, inicie o interpretador Python e
# tentando importá-lo:
# 
# >>> import flask
# 
# 25
# 
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
# return 'Hello, World!'
# =============================================================================





"""
class Circulo:
    def _init_(self):
        
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.raio = raio
                
    def diametro_f(self,diametro):   
            diametro = raio*2
    def comprimento_circunferencia_f(self,comprimento_circunferencia):
            comprimento_circunferencia = 2*3,14*raio
    def area_f(self,area):
            area = 3,14*(raio*raio)
        
from Circulo import Circulo
eixo_x = int(input("Digite valor para o eixo X: "))
eixo_y = int(input("Digite valor para o eixo Y: "))
raio = int(input("Digite valor para o raio do círculo: "))
if eixo_x >= raio and eixo_y >= raio:
    print("\nEscolha a opção desejada:\n1 - Para descobrir o diâmetro\n2 - Para descobrir o comprimento da circunferência\n3 - Para descobrir o diâmetro")
    escolha = int(input(""))
    if escolha == 1:
        
        c = Circulo()
        print("O diâmetro é ",c.diametro_f())
        
    
else:
    print("O valor do raio não pode ser menor que o valor dos eixos!")
    

"""

"""
def inserir_atendimento():
    arq = open('veterinaria.txt','a+')
    numero = int(input("Digite o número do atendimento: "))
    data = input("Digite a data do atendimento: ")
    horario = input("Digite a data do atendimento: ")
    medico = input("Digite o nome do médico do atendimento: ")
    solicitante = input("Digite o nome do solicitante do atendimento: ")
    animal = input("Digite o tipo de animal do atendimento: ")
    observacoes = input("Observações: ")
    arq.write('numero:'+str(numero)+'\n')
    arq.write('data:'+str(data)+'\n')
    arq.write('horario:'+str(horario)+'\n')
    arq.write('medico:'+str(medico)+'\n')
    arq.write('solicitante:'+str(solicitante)+'\n')
    arq.write('animal:'+str(animal)+'\n')
    arq.write('observacoes:'+str(observacoes)+'\n\n')
    arq =  open('veterinaria.txt', 'r')
    print(arq.read())
    arq.close()

def pesquisa_atendimento(atendimento):
    espaco = None
    arq = open('veterinaria.txt','r')
    arq_leitura = arq.readlines()
    encontrou = False
    exibeatendimento = False
    for linha in arq_leitura:
        if (linha.find('numero') != -1):
            exibeatendimento = False
            cod = linha.split(':')
            if(int(cod[1])) == int(atendimento):
                exibeatendimento = True
                encontrou = True
        if(exibeatendimento == True):           
            if espaco == None:
                print("\n")
            espaco = 1
            print(linha)
    if(encontrou == False):
        print("Atendimento não encontrado.")
        return encontrou
    arq.close()

def altera_atendimento(atendimento):
    arq = open('veterinaria.txt', 'r')
    leitura_arq = arq.readlines()
    encontrou = False
    novo_arq = ""
    for linha in leitura_arq:
        if (linha.find('numero') != -1):
            cod = linha.split(':')
            if (int(cod[1]) == int(atendimento)):
                encontrou = True
        if (encontrou == True):
            if (linha.find('numero') != -1):
                numero_novo = input('Digite o novo numero: ')
                novo_arq = 'numero: ' + str(numero_novo) + '\n'
            elif (linha.find('data') != -1):
                data = input('Digite nova data: ')
                novo_arq = novo_arq + 'data: ' + str(data) + '\n'
            elif (linha.find('horario') != -1):
                horario = input('Digite o novo horario: ')
                novo_arq = novo_arq + 'horario: ' + str(horario) + '\n'
            elif (linha.find('medico') != -1):
                medico = input('Digite o novo medico: ')
                novo_arq = novo_arq + 'medico: ' + str(medico) + '\n'  
            elif (linha.find('solicitante') != -1):
                solicitante = input('Digite o novo solicitante: ')
                novo_arq = novo_arq + 'solicitante: ' + str(solicitante) + '\n'
            elif (linha.find('animal') != -1):
                animal = input('Digite o novo animal: ')
                novo_arq = novo_arq + 'animal: ' + str(animal) + '\n' 
            elif (linha.find('observacoes') != -1):
                observacoes = input('Digite a nova observação: ')
                novo_arq = novo_arq + 'observacoes: ' + str(observacoes) + '\n'                  
            else:
               novo_arq = novo_arq + linha
        else:
            novo_arq = novo_arq + linha
                        
    arq = open('veterinaria.txt', 'w+')
    arq.write(novo_arq)    
    arq.close() 
    
    
while True:
    print("Escolha uma das opções abaixo: \n\n1 - Inserir novo atendimento \n2 - Pesquisar atendimento \n3 - Alterar atendimento")
    escolha = int(input("Digite o número da opção pretendida: "))
    if escolha == 1:
        inserir_atendimento()
    elif escolha == 2:
        pesquisa_atendimento(input('Digite o atendimento que deseja pesquisar: '))
    elif escolha == 3:
        altera_atendimento(input('Digite o atendimento que deseja alterar: '))
    elif escolha == 0:
        break
    else:
        print("Escolha inválida...Tente novamente!")    
"""       
"""
def altera(atendimento):
    arq = open('veterinaria.txt', 'r')
    arq_leitura = arq.readlines()
    encontrou = False
    novo_arq = ""
    for linha in arq_leitura:
        if(linha.find('numero') != -1):
            cod = linha.split(':')
            if(int(cod[1])) == int(atendimento):
                encontrou = True
        if(encontrou == True):
            if (linha.find('numero') != -1):
                numero_novo = input('Digite o novo numero: ')
                novo_arq = 'numero:' + str(numero_novo) + '\n'
            elif (linha.find('data') != -1):
                data = input("Digite a nova data: ")
                novo_arq = 'data:' + str(data) + '\n'
            elif (linha.find('horario') != -1):
                horario = input('Digite o novo horario: ')
                novo_arq = novo_arq + 'horario:' + str(horario) + '\n'
            elif (linha.find('medico') != -1):
                medico = input('Digite o novo medico: ')
                novo_arq = novo_arq + 'medico:' + str(medico) + '\n'  
            elif (linha.find('solicitante') != -1):
                solicitante = input('Digite o novo solicitante: ')
                novo_arq = novo_arq + 'solicitante:' + str(solicitante) + '\n'
            elif (linha.find('animal') != -1):
                animal = input('Digite o novo animal: ')
                novo_arq = novo_arq + 'animal:' + str(animal) + '\n' 
            elif (linha.find('observacoes') != -1):
                observacoes = input('Digite a nova observação: ')
                novo_arq = novo_arq + 'observacoes:' + str(observacoes) + '\n'                  
            else:
               novo_arq = novo_arq + linha
        else:
            novo_arq = novo_arq + linha

    arq = open('Veterinaria.txt', 'w+')
    arq.write(novo_arq)    
    arq.close() 

"""



"""
def pesquisa(atendimento):
    arq = open('veterinaria.txt', 'r')
    arq_leitura = arq.readlines()
    encontrou = False
    exibeatendimento = False
    for linha in arq_leitura:
        if(linha.find('numero') != -1):
            exibeatendimento = False
            cod = linha.split(':')
            if(int(cod[1])) == int(atendimento):
                exibeatendimento = True
                encontrou = True
        if(exibeatendimento == True):
            print(linha)
    if(encontrou == False):
        print("Atendimento não encontrado!")
        return encontrou
    arq.close()


def insere_dados():
    arq_grava =  open('veterinaria.txt', 'a+')
    numero = int(input("Digite o número do atendimento: "))
    data = input("Digite a data do atendimento: ")
    horario = input("Digite o horário do atendimento: ")
    medico = input("Digite o nome do médico do atendimento: ")
    solicitante = input("Digite o nome do solicitante do atendimento: ")
    animal = input("Digite o tipo de animal do atendimento: ")
    observacoes = input("Observações: ")
    arq_grava.write('numero:'+ str(numero)+'\n')
    arq_grava.write('data:'+ str(data)+'\n')
    arq_grava.write('horario:'+ str(horario)+'\n')
    arq_grava.write('medico:'+ str(medico)+'\n')
    arq_grava.write('solicitante:'+ str(solicitante)+'\n')
    arq_grava.write('animal:'+ str(animal)+'\n')
    arq_grava.write('observacoes:'+ str(observacoes)+'\n'+'\n')
    arq_grava =  open('veterinaria.txt', 'r')
    print(arq_grava.read())
    arq_grava.close()
    print("Dados inseridos com sucesso! ")
    

    

def altera(atendimento):
    arq = open('veterinaria.txt', 'r')
    arq_leitura = arq.readlines()
    encontrou = False
    novo_arq = ""
    for linha in arq_leitura:
        if(linha.find('numero') != -1):
            cod = linha.split(':')
            if(int(cod[1])) == int(atendimento):
                encontrou = True
        if(encontrou == True):
            if (linha.find('numero') != -1):
                numero_novo = input('Digite o novo numero: ')
                novo_arq = 'numero:' + str(numero_novo) + '\n'
            elif (linha.find('data') != -1):
                data = input("Digite a nova data: ")
                novo_arq = 'data:' + str(data) + '\n'
            elif (linha.find('horario') != -1):
                horario = input('Digite o novo horario: ')
                novo_arq = novo_arq + 'horario:' + str(horario) + '\n'
            elif (linha.find('medico') != -1):
                medico = input('Digite o novo medico: ')
                novo_arq = novo_arq + 'medico:' + str(medico) + '\n'  
            elif (linha.find('solicitante') != -1):
                solicitante = input('Digite o novo solicitante: ')
                novo_arq = novo_arq + 'solicitante:' + str(solicitante) + '\n'
            elif (linha.find('animal') != -1):
                animal = input('Digite o novo animal: ')
                novo_arq = novo_arq + 'animal:' + str(animal) + '\n' 
            elif (linha.find('observacoes') != -1):
                observacoes = input('Digite a nova observação: ')
                novo_arq = novo_arq + 'observacoes:' + str(observacoes) + '\n'                  
            else:
               novo_arq = novo_arq + linha
        else:
            novo_arq = novo_arq + linha

    arq = open('Veterinaria.txt', 'w+')
    arq.write(novo_arq)    
    arq.close() 


    
while True:    
    
    print("Qual sua ação no Sistema? 
          
    1 - Inserir atendimento
    2 - Alterar um atendimento      
    3 - Pesquisar um atendimento
    
    0 - Sair")


    escolha = int(input("Escolha o que desejar: ")) 
    if escolha == 1:
        insere_dados()
    elif escolha == 2:
        altera(input('Digite o atendimento que deseja alterar: ')) 
    elif escolha == 3:
        pesquisa((input('Digite o atendimento que deseja pesquisar: '))        
    elif escolha == 0:
        break
    else:
        print("Escolha inválida!")
     
      
"""







"""
arq = open('lista.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores')
arq.writelines(texto)
arq = open('lista.txt', 'r')
print(arq.read())

arq.close()

"""


"""
def PesquisarAtendimento(atendimento):   
    arq = open('Atendimentos.txt', 'r')
    leitura_arq = arq.readlines()
    encontrou = False
    for linha in leitura_arq:
        if (linha.find('numero') != -1):
            exibeatendimento = False
            cod = linha.split(':')
            if (int(cod[1]) == int(atendimento)):
                exibeatendimento = True
                encontrou = True
        if (exibeatendimento==True):
            print(linha)
    if (encontrou == False):
        print('Atendimento não encontrado!')
        return encontrou
    arq.close()

def InserirAtendimento():    
    arq_grava = open('Atendimentos.txt', 'a+')
    numero = int(input('Digite o número do Atendimento: '))
    data = input('Digite a data do Atendimento: ')
    horario = input('Digite a horário do Atendimento: ')
    medico = input('Digite o nome do médico do Atendimento: ')
    solicitante = input('Digite o nome do solicitante do Atendimento: ')
    animal = input('Digite o animal que será Atendido: ')
    observacoes = input('Digite as observações do Atendimento: ')
    arq_grava.write('numero:' + str(numero) + '\n')
    arq_grava.write('data:' + str(data) + '\n')
    arq_grava.write('horario:' + str(horario) + '\n')
    arq_grava.write('medico:' + str(medico) + '\n')
    arq_grava.write('solicitante:' + str(solicitante) + '\n')
    arq_grava.write('animal:' + str(animal) + '\n')
    arq_grava.write('observacoes:' + str(observacoes) + '\n')
    arq_grava.close()
    print('Atendimento inserido com sucesso!')

def AlterarAtendimento(atendimento):
    arq = open('Atendimentos.txt', 'r')
    leitura_arq = arq.readlines()
    encontrou = False
    novo_arq = ""
    for linha in leitura_arq:
        if (linha.find('numero') != -1):
            cod = linha.split(':')
            if (int(cod[1]) == int(atendimento)):
                encontrou = True
        if (encontrou == True):
            if (linha.find('numero') != -1):
                numero_novo = input('Digite o novo numero: ')
                novo_arq = 'numero:' + str(numero_novo) + '\n'
            elif (linha.find('data') != -1):
                data = input('Digite nova data: ')
                novo_arq = novo_arq + 'data:' + str(data) + '\n'
            elif (linha.find('horario') != -1):
                horario = input('Digite o novo horario: ')
                novo_arq = novo_arq + 'horario:' + str(horario) + '\n'
            elif (linha.find('medico') != -1):
                medico = input('Digite o novo medico: ')
                novo_arq = novo_arq + 'medico:' + str(medico) + '\n'  
            elif (linha.find('solicitante') != -1):
                solicitante = input('Digite o novo solicitante: ')
                novo_arq = novo_arq + 'solicitante:' + str(solicitante) + '\n'
            elif (linha.find('animal') != -1):
                animal = input('Digite o novo animal: ')
                novo_arq = novo_arq + 'animal:' + str(animal) + '\n' 
            elif (linha.find('observacoes') != -1):
                observacoes = input('Digite a nova observação: ')
                novo_arq = novo_arq + 'observacoes:' + str(observacoes) + '\n'                  
            else:
               novo_arq = novo_arq + linha
        else:
            novo_arq = novo_arq + linha
                        
    arq = open('Atendimentos.txt', 'w+')
    arq.write(novo_arq)    
    arq.close() 

while True:
    print("Qual sua ação no Sistema? 
          
    1 - Inserir atendimento
    2 - Alterar um atendimento      
    3 - Pesquisar um atendimento
    
    0 - Sair")
    
    menu = int(input("Digite sua ação desejada: "))
    if menu == 0:
        break        
    elif menu == 1:
        InserirAtendimento() 
    elif menu == 2:
        AlterarAtendimento(input('Digite o atendimento que deseja alterar: '+'\n'))
    elif menu == 3:
        PesquisarAtendimento(input('Digite o atendimento que deseja pesquisar: '+'\n'))
    else:
        print("Valor incorreto! Não foi possível identificar sua ação.")






"""



"""
cadastro1 = ["teste"]
cadastro = []
dados = []
j = 0

for k in range(1,3):
    for i in range(0,1):
      nome = input("Digite o nome do %dª cliente: "%kiy)
      idade = input("Digite a idade do %dª cliente: "%k)
      cpf = input("Digite o cpf do %dª cliente: "%k)
      dados.insert(i,nome) 
      dados.append(idade) 
      dados.append(cpf) 
      cadastro.append(dados)
      dados = []
      arq = open('cadastro.txt','a+')
      arq.write(str(cadastro[j]))
      print(j)
      j += 1
      arq = open('cadastro.txt','r')
      print(arq.read())
      arq.close()
"""


#def imprimir(nome,telefone):
#             print("\n+==================================================+")
#             print("|  Nome                    |Telefone               |")
#             print("+==================================================+")
#             for nome, telefone in sorted(agenda.items()): 
#              print(f'|  {nome: <24}|{telefone: <23}|')                   
#              print("+--------------------------------------------------+")





# =============================================================================
# nome = None
# arq_nome_nota = None
# arquivo = None
# 
# def insere_nome_notas(nome, nota):
#     arq_nome_nota = open('arquivo_nomes_notas.txt','a+')
#     arq_nome_nota.write(str(nome))
#     arq_nome_nota.write(" ")
#     arq_nome_nota.write(str(nota))
#     arq_nome_nota.write(" ")
#     
# 
# nome = input("Digite o nome do aluno: ")
# nota = input("Digite a nota do aluno: ")    
# insere_nome_notas(nome, nota)
# print(arq_nome_nota)
# =============================================================================

#print(f'|  {nome: <24}|{nota: <23}|')








"""
def separa_pares_impares (num):
    if num%2 == 0:
        arq_par = open('arquivo_pares.txt','a+')
        arq_par.write(str(num))
        arq_par.write(",")
        
    else:
        arq_imp = open('arquivo_impares.txt','a+')
        arq_imp.write(str(num))
        arq_imp.write(",")
        

escolha = None
while escolha != 0:
    num = int(input("Digite um número: "))
    separa_pares_impares(num)
    escolha = int(input("Digite 1 para continuar ou 0 para sair: "))

arq_par = open('arquivo_pares.txt','r')
arq_imp = open('arquivo_impares.txt','r')

print("\nOs números pares são ", arq_par.read())
print("Os números impares são ", arq_imp.read())

arq_par.close()
arq_imp.close()
"""










"""
nome = None
notas = []
lista = []
alunos =  []
maior = 0
menor = 10
x = 0
i = 0

for j in range(1,3):
  nome = input("Digite o nome do %dª aluno: "%j)
  lista.insert(x,nome)
  for i in range(1,3):
    nota = float(input("Digite a  %dª nota: " %i))
    if nota > maior:
        maior = nota
        nome_maior = nome
    if nota < menor:
        menor = nota
        nome_menor = nome
    notas.append(nota)
  lista.append(notas)
  alunos.append(lista)
  notas = []
  lista = []
    
print("\nA maior nota é do aluno ", nome_maior," e sua nota foi ",maior,".")
print("A menor nota é do aluno ", nome_menor," e sua nota foi ",menor,".")
"""

"""
nome = None
notas = []
lista = []

x = 0
i = 0
z = 0

for i in range(1,11):
    nome = input("Digite o nome do %dª aluno: "%i)
    
    lista.insert(x,nome)
    
    print(lista)
    for i in range(1,11):
        nota = float(input("Digite a  %dª nota: " %i))
        lista[z].append(nota)
       
        z = z + 1
    x = x + 1
    print(lista)

"""





# =============================================================================
# nomes = []
# notas = []
# i = 0
# 
# for i in range(1,11):
#     nome = input("Digite o nome do %dª aluno: "%i)
#     nomes.append(nome)
#     print(nomes)
#     for i in range(1,11):
#         nota = float(input("Digite a  %dª nota: " %i))
#         notas.append(nota)
# =============================================================================










# =============================================================================
# matriz = [['nome','telefone','sexo'],['nome','telefone','sexo']]
# 
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if coluna == 0:
#             matriz[linha][coluna] = input("nome: ")
#         elif coluna == 1:
#             matriz[linha][coluna] = input("fone: ")
#         else:
#             matriz[linha][coluna] = input("sexo: ")
#     print(matriz)
# =============================================================================





# =============================================================================
# numeros = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# 
# print(numeros[0:2])
# =============================================================================





# =============================================================================
# exemplo = [[1,2,3],[4,5,6],[7,8,9]]
# 
# for lin in range(len(exemplo)):
#     for col in range(len(exemplo[lin])):
#         print(exemplo[lin][col],end = '\t')
#     print()
# =============================================================================






# =============================================================================
# telefone = None
# nome = None
# escolha = None
# cria_agenda = None
# agenda = {'mauro': '999', 'ooo': '888', 'ppp': '666'}
# 
# 
# while cria_agenda != 0:
#     cria_agenda = int(input("Digite 1 para criar agenda ou 0 para sair: "))
#     if cria_agenda == 1:
#          #agenda = {}
#          agenda = {'mauro': '999', 'ooo': '888', 'ppp': '666'}
#          
#          def imprimir(nome,telefone):
#             print("\n+==================================================+")
#             print("|  Nome                    |Telefone               |")
#             print("+==================================================+")
#             for nome, telefone in sorted(agenda.items()): 
#              print(f'|  {nome: <24}|{telefone: <23}|')                   
#              print("+--------------------------------------------------+")
#          
#          
#          def inserir(nome,telefone):
#             while True:
#                 nome = input("Digite o nome: ").strip().lower()
#                 if nome in agenda:
#                     print("Nome já cadastrado!")            
#                 telefone = input("Digite o telefone: ").strip().lower()
#                 if nome not in agenda:
#                     agenda[nome] = telefone
#                     if nome in agenda:
#                         print("Contato inserido com sucesso!")  
#                         break
#                 else:
#                     print("Ocorreu um erro, tente novamente!")
#            
#          def pesquisar(nome):
#             nome = input("Digite o nome desejado: ").lower()
#             if nome in agenda:
#                 resultado = agenda[nome]
#                 print("O telefone é ",resultado)
#             else:
#                 print("Não encontrado")
#                 
#          def excluir(nome):
#             sair = None
#             while sair != 0:
#                 nome = input("Digite o nome para excluir: ").lower()
#                 if nome not in agenda:
#                     sair = int(input("Nome não encontrado. Digite 1 para tentar novamente ou digite 0 para voltar ao menu principal! "))                                        
#                     if sair == 0:
#                         break
#                    
#                 elif nome in agenda:
#                     del agenda[nome]
#                     if nome not in agenda:
#                         print("Contato apagado com sucesso")
#                         break
#                     else:
#                             print("Ocorreu um erro, tente novamente!")               
#                     
#         
#          while escolha != 0:
#             escolha = int(input("Digite uma das opções abaixo: \n1 - Inserir novo contato\n2 - Pesquisar contato\n3 - Excluir contato\n4 - Imprimir agenda\n0 - Sair "))
#          
#             if escolha == 1:
#                  inserir(nome,telefone)   
#             if escolha == 2:
#                 pesquisar(nome)
#             if escolha == 3:
#                 excluir(nome)
#             if escolha == 4:
#                 imprimir(nome,telefone)
#             if escolha == 0:
#                 cria_agenda = int(0)
#                 print("\nAdeus!")
#                 break
#     elif cria_agenda == 0:
#          print("\nVocê não criou uma agenda! Adeus....")
#          break
#     else:
#          print("Escolha entre 1 ou 0! ")
# =============================================================================
         
                                
    
    
        

# =============================================================================
# nome = None
# notas = []
# lista = [[nome,notas]]
# 
# 
# i = 0
# 
# for i in range(1,11):
#     nome = input("Digite o nome do %dª aluno: "%i)
#     x = 0
#     lista[x][0].append(nome)
#     print(lista[x][0][i])
#     for i in range(1,11):
#         nota = float(input("Digite a  %dª nota: " %i))
#         lista[i][1][i].append(nota)
#     print(lista[i][1])
# =============================================================================


# =============================================================================
# nomes = []
# notas = []
# i = 0
# 
# for i in range(1,11):
#     nome = input("Digite o nome do %dª aluno: "%i)
#     nomes.append(nome)
#     print(nomes)
#     for i in range(1,11):
#         nota = float(input("Digite a  %dª nota: " %i))
# =============================================================================
        
        
        

# =============================================================================
# Aula assíncrona 7 letra b
# 
# lista_a = [4,2,8,6,5]
# lista_b = lista_a
# lista_b[3] = 999
# print(lista_a)
# 
# lista_a = [4,2,8,6,5]
# lista_b = lista_a[:]
# lista_b[3] = 999
# print(lista_a)
# =============================================================================









# notas = []
# encerra = None
# soma_notas = 0
# nome = input("Digite o nome do aluno: ")

# while encerra != 0:
#     nota_individual = float(input("Digite a nota do aluno: "))
#     notas.append(nota_individual)
#     encerra = int(input("Digite 1 para adicionar outra nota ou 0 para sair: "))
#     if encerra < 0 or encerra > 1:
#         print("Só são aceitos 0 ou 1 para encerrar ou continuar.")
# soma_notas = sum(notas)
# quantidade_notas = len(notas)
# media = soma_notas/quantidade_notas
# print("\nA média do aluno ", nome, "é  %.1f" % media, ".")
    
    
    



# =============================================================================
# digitados = []
# sorteados = []
# acertos = []
# i = 1
# numero = None
# import random
# 
# # Fazer apostas
# while len(digitados) < 6:
#     numero = int(input ("Digite a %dª dezena: "%i))
#     teste = numero in digitados
#     if numero <= 60 and numero > 0 and teste == False:
#         digitados.append(numero)
#         i = i + 1
#     elif numero > 60 or numero == 0:
#         print("Número inválido. Só números de 1 a 60.")
#     elif teste == True:
#         print("Número já existente. Digite outro número.")
# digitados_ordenados = sorted(digitados)
# digitados_imprimir = [str(a) for a in digitados]
# print("\nNúmeros apostados: ",",".join(digitados_imprimir))
# print("\n")
# 
# 
# #Sorteio
# #for i in range(1,7):
#     #sorteio = random.randint(1,60)
#     #sorteados.append(sorteio)
#     
# while len(sorteados) != 6:
#     sorteio = random.randint(1, 60)
#     if sorteio not in sorteados:
#         sorteados.append(sorteio)    
# sorteados_ordenados = sorted(sorteados)
# sorteados_imprimir = [str(a) for a in sorteados_ordenados]  
# print ("Os numeros sorteados foram:","\n",",".join(sorteados_imprimir))
# 
# 
# # Conferencia
# print ("\n---- Resultado Final --------")
# for i in range(0,6):
#     if sorteados[i] in digitados:
#         acertos.append(sorteados[i])
# if len(acertos) == 6:
#     print ("Parabéns, você é foi premiado.")
# else:   
#     acertos_ordenados = sorted(acertos)
#     acertos_imprimir = [str(a) for a in acertos_ordenados]
# if acertos_ordenados != []:
#     print ("\nNão foi dessa vez. Os numeros acertados foram:","\n",",".join(acertos_imprimir))
# else:
#     print("\nNão foi dessa vez. Nenhum acerto.")
# =============================================================================
    














  
"""for i in range(1,fim):  
    numero = int(input ("informe a %dª dezena: "%i))
    if numero <= 60:
        digitados.append(numero)
    elif numero > 60:
        fim = fim + 1
        i = i - 2
        print("Número inválido.")
       
         

print(digitados)       
        
#else:
   # print("Número inválido. Só são válidos números entre 0 e 60!")
        
"""
    
"""# -*- coding: cp1252 -*-
import random; # importar as funcoes do random
random.seed(); # inicializar o contador
sorteados = []; # lista de numeros sorteados
digitados = []; # lista de numeros digitados
# realização dos sorteios
for i in range(1,7):
    sorteio = random.randint(1,60); #sortear um numero
    sorteados.append(sorteio); #adicionar na lista

# digitação dos números
for i in range(1,7):
    numero = input ("informe a %dª dezena: "%i);
    digitados.append(numero);

#2- verificação dos acertos: apenas os numeros
print "---- 1 verificação ---------"
acertos2 = [];
for i in range(0,6):
    if sorteados[i] in digitados:
        acertos2.append(sorteados[i]);
if len(acertos2) == 6: ## sorteados.len
    print "parabéns.... você é um milionário"
else:
    print "vc foi roubado. Os numeros sorteados foram:";
    print sorteados;
    print "os numeros acertados foram: "
    print acertos2;
    
    
    https://sites.google.com/site/andrealfaintprogramacao/plano-de-aulas/exerccio-python-nmeros-sorteados
"""


    


