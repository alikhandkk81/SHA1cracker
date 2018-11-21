from urllib.request import urlopen, hashlib

#Primeiro, pegue o hash do usuário para obter o hash sha1 para quebrar

sha1hash = input("Por favor, insira o hash para crack.\n>")

#Em segundo lugar, vamos abrir um arquivo cheio de palpites de senha

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

#Terceiro, vamos adivinhar a lista de senhas que abrimos e dividir por linha

for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):

#Em quarto lugar, vamos adivinhar o que achamos da lista de senhas para que possamos compará-la com o hash que o usuário nos deu

    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()

#Quinto, vamos comparar o hash que o usuário nos deu para a versão com hash do palpite de senha e determinar se eles são iguais

    if hashedGuess == sha1hash:

#Em sexto lugar, informaremos ao programa o que fazer se a adivinhação de senha coincidir, que é imprimir a estimativa atual e sair do programa.
#Também informaremos ao programa o que fazer se a adivinhação de senha não corresponder, que é retornar à etapa 3 para obter uma nova senha da lista.

        print("A senha é ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Palpite de senha ",str(guess)," não combina, tentando próximo...")

#Na sétima e última etapa, informaremos ao programa o que fazer se passarmos pela lista de senhas sem encontrar uma correspondência.
print("Senha não no banco de dados, vamos pegá-los da próxima vez.")