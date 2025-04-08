candidatos = {
    0 : {"nome": "nulo","voto":0}
}

eleitores = {}

def candidato():
    nome = input("Digite o nome que deseja registrar").lower
    numero = int(input("Digite um :numero a ser ultilizado"))

    if numero<10:
        print("Digite ao menos 2 numeros")
    elif numero in candidato:
        print("Esse numero ja esta sendo ultilizado")
    else:
        print("Digite um caractere valido")
        if nome in candidato:
            print("esse nome esta sendo ultilizado")
        elif  int:
            print("Digite somente letras")
        else :
            candidatos[numero] = {"nome": nome, "voto":0}
            print(f'{nome} foi registrado como candidato')
def eleitor():

    nome = input('digite seu nome: ') 
    matricula = int(input('numero de matricula: '))
    eleitores[matricula] = {"nome":nome}
    for nomes, items in candidatos.items():
        print('Candidato:', items['nome'],' número: ',nomes)
    numero = int(input('digite o numero do seu candidato: '))
    if numero in candidatos:
        candidatos[numero]['voto'] +=1
        print('Votação concluída com sucesso!')
    else:
        print('o numero do candidato não existe!')

def mostrar_tudo():
    for nomes, items in candidatos.items():
        print('Candidato: ',items['nome'],'número: ',nomes)
    for nomes, items in eleitores.items():
        print('eleitor: ', items['nome'],' Titulo: ',nomes)
while True:
    cargo = input('1 para se candidatar\n2 para ser eleitor\n3 mostrar os candidatos e os eleitores\n4 para terminar eleição ')
    
    if cargo == '1':
        candidato()
    elif cargo == '2':
        eleitor()
    elif cargo == '3':
        mostrar_tudo()
    elif cargo == '4':
        for nome, items in candidatos.items():
            print('Candidato: ', items['nome'],' | Votos: ',items["voto"])
        break
    else:
        print('coloque apenas uma das opções')