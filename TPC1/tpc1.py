def ler_info (ficheiro): 
    with open(ficheiro) as f:
        next(f)         #1 linha nao interessa

        dados = []      #matriz com os dados

        for linha in f:
            campos = linha.strip().split(",")
            id = campos[0]
            index = int(campos[1])
            dataEMD = campos[2]
            primNome = campos[3]
            ultNome = campos[4]
            idade = int(campos[5])
            genero = campos[6]
            morada = campos[7]
            modalidade = campos[8]
            clube = campos[9]
            email = campos[10]
            federado = True if campos[11] == "false" else False
            resultado = True if campos[12] == "true" else False

            dic_dados = {'_id': id,
                         'index': index,
                         'dataEMD': dataEMD,
                         'nome/primeiro': primNome,
                         'nome/último': ultNome,
                         'idade': idade,
                         'género': genero,
                         'morada': morada,
                         'modalidade': modalidade,
                         'clube': clube,
                         'email': email,
                         'federado': federado,
                         'resultado': resultado
                         }
            dados.append(dic_dados)         
    return dados

#Lista ordenada alfabeticamente das modalidades desportivas
def ord_mod(dados):
    modalidades = []

    for linha in dados:
        modalidade = linha['modalidade']       #como posso por isto, sendo que ja tenho o dic definido em cima
        if modalidade not in modalidades:
            modalidades.append(modalidade)
    modalidades.sort()    #ordena alfabeticamente

    return modalidades



#A função ord_mod recebe os dados como entrada.
#Iteramos sobre os dados, extrairmos as modalidades e as adicionamos à lista modalidades, garantindo que não haja duplicatas.
#Ordenamos a lista de modalidades alfabeticamente.
#Por fim, retornamos a lista ordenada das modalidades.
#Dessa forma, ao chamar a função ord_mod com seus dados, você obterá uma lista ordenada alfabeticamente das modalidades desportivas presentes nesses dados.


# Percentagens de atletas aptos e inaptos para a prática desportiva;
def percentagem_atletas(dados):
    aptos=0
    inaptos=0
    total=len(dados)

    for linha in dados:
        resultado = linha['resultado']
        if resultado:
            aptos += 1
        else :
            inaptos +=1

    if total==0:
        return 0            

    perc_aptos =  (aptos/total)*100
    perc_inaptos = (inaptos/total)*100

    return (perc_aptos,perc_inaptos)  


# Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
def idade_min(dados):
    min=1000
    for linha in dados:
        if linha['idade']<min:
            min = linha['idade']
    return min

def idade_max(dados):
    max=0
    for linha in dados:
        if linha['idade']>max:
            max=linha['idade']
    return max

def escalao(idademin, idademax):
    escaloes=[]
    for i in range((idademin // 5) * 5, (idademax//5 + 1) * 5, 5):
        escaloes.append((i,i+4))
    return escaloes

def dist_escalao(dados,escaloes):
    array=[]
    for e in escaloes:
        min = e[0]
        max = e[1]
        c = 0
        for i in dados:
            if i['idade'] >= min and i['idade']<= max:
                c+=1
        array.append(c)
    return array

def dist_atletasEsc(dados,escaloes):
    array=[]
    for e in escaloes:
        min = e[0]
        max = e[1]
        c = 0
        for i in dados:
            if i['idade']>=min and i['idade']<=max and i['federado'] == True:
                c+=1
        array.append(c)
    return array        


def main():
    ficheiro = 'emd.csv'
    dados = ler_info(ficheiro)

    print (f'A lista ordenada alfabeticamente das modalidades desportivas é: {ord_mod(dados)}')

    percentagem = percentagem_atletas(dados)

    print ('A percentagem de atletas aptos é: ', percentagem[0], '%')
    print ('A percentagem de atletas inaptos é: ', percentagem[1], '%')

    idadeMin = idade_min(dados)
    #print(idadeMin)

    idadeMax = idade_max(dados)
    #print(idadeMax)

    escaloesIdade = escalao(idadeMin,idadeMax)
    escaloesIdade = escalao(idadeMin,idadeMax)
    # print(f"{idadeMin = } {idadeMax = } {escaloesIdade = }")

    for esc, numAtletas in zip(escaloesIdade, dist_escalao(dados, escaloesIdade)):
        print(f"{esc}: {numAtletas}")

    # print (dist_escalao(dados,escaloesIdade))
    # print (dist_atletasEsc(dados,escaloesIdade))

if __name__ == '__main__':
    main()    