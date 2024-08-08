import os
os.system ('cls') 

opcao_escolhida = int (input ('Escolha um número:') )
if opcao_escolhida %2 == 0:
    print ('Esse número é par')
else:
    print ('Esse numero é impar')        

idade = int (input ('Qual sua idade?'))
if idade <= 12:
    print ('Você é criança')
elif idade < 18:
    print ('Você é adolescente')
else:
    print ('você é adulto') 

usuario_correto = 'scarfax'
senha_correta = '00666'

user = input ('Digite seu usuário:')
senha = input ('Digite sua senha:')

if user == usuario_correto and senha == senha_correta:
    print ('Acesso liberado')
else:
    print ('Credenciais inválidas. Tente novamente')    