tabela = [["31/08/2019", "6125", "397800", "401550", "26400"],
          ["31/08/2019", "6283", "408300", "412950", "13500"],
          ["31/08/2019", "6402", "412050", "417300", "16350"],
          ["31/08/2019", "6527", "424650", "430650", "35100"],
          ["31/08/2019", "6568", "431250", "436500", "37200"],
          ["31/08/2019", "6595", "429150", "434550", "35850"],
          ["31/08/2019", "6522", "421800", "427200", "31050"],
          ["31/08/2019", "6960", "389550", "397650", "73050"],
          ["31/08/2019", "6483", "420750", "426000", "29400"],
          ["31/08/2019", "6635", "430500", "435600", "31050"],
          ["01/09/2019", "8482", "565800", "582450", "61050"],
          ["01/09/2019", "8482", "569550", "585750", "61350"],
          ["01/09/2019", "8395", "565200", "581250", "57900"],
          ["01/09/2019", "8432", "564600", "581100", "58500"],
          ["01/09/2019", "8552", "568200", "585150", "58650"],
          ["01/09/2019", "8587", "570150", "587250", "59100"],
          ["01/09/2019", "8625", "573450", "590400", "61500"],
          ["01/09/2019", "8646", "579300", "595350", "61650"],
          ["01/09/2019", "8692", "582900", "599100", "64950"],
          ["01/09/2019", "8605", "580800", "596400", "63600"],
          ["01/09/2019", "8166", "551100", "565650", "59700"],
          ["01/09/2019", "7990", "537450", "551850", "58650"],
          ["01/09/2019", "7988", "535650", "550350", "59850"],
          ["01/09/2019", "8027", "538650", "553650", "60600"],
          ["01/09/2019", "8258", "554400", "570000", "63450"],
          ["01/09/2019", "8098", "541650", "556950", "66000"],
          ["01/09/2019", "8061", "539250", "554400", "66900"],
          ["01/09/2019", "8083", "537600", "552750", "66150"],
          ["01/09/2019", "8016", "534600", "549450", "58950"],
          ["01/09/2019", "8312", "552900", "568800", "60150"],
          ["01/09/2019", "8460", "563550", "579750", "61650"],
          ["01/09/2019", "8519", "569850", "585900", "62850"],
          ["01/09/2019", "8269", "549300", "565050", "59250"],
          ["01/09/2019", "7968", "530100", "544800", "56250"],
          ["01/09/2019", "7945", "529500", "544050", "55500"],
          ["01/09/2019", "7939", "529200", "543750", "55950"],
          ["01/09/2019", "8265", "555750", "570900", "59550"],
          ["01/09/2019", "7934", "534600", "549000", "54900"],
          ["01/09/2019", "7733", "520500", "534000", "49500"],
          ["01/09/2019", "7809", "525750", "539850", "56850"],
          ["01/09/2019", "7965", "536850", "551250", "61050"],
          ["01/09/2019", "8052", "543300", "558150", "57600"],
          ["01/09/2019", "8234", "555750", "570300", "59400"],
          ["01/09/2019", "8281", "560400", "575100", "61350"],
          ["01/09/2019", "8275", "553800", "568200", "57000"],
          ["01/09/2019", "8055", "536400", "550350", "51450"],
          ["01/09/2019", "8068", "534600", "548850", "51150"],
          ["01/09/2019", "8029", "531000", "545100", "52950"],
          ["01/09/2019", "8063", "533550", "548250", "53550"],
          ["01/09/2019", "8141", "539850", "554700", "54300"],
          ["01/09/2019", "8186", "541800", "556800", "57000"],
          ["01/09/2019", "8762", "581850", "599250", "60900"],
          ["01/09/2019", "8792", "585750", "602850", "65100"],
          ["01/09/2019", "8708", "583800", "600600", "65250"],
          ["01/09/2019", "8740", "584400", "601050", "62700"]]
def retira_meses_repetidos(meses):
    meses_filtrados = []
    for i in range(len(meses)):
        if (meses[i])[3:5] not in meses_filtrados:
            meses_filtrados.append((meses[i])[3:5])
    return meses_filtrados

def mes_corrente(matriz):
    meses = []
    medias = []
    for i in range(len(matriz)):
        meses.append(matriz[i][0])
    meses_filtrados = retira_meses_repetidos(meses)
    for i in range(len(meses_filtrados)):
        soma_mes = 0
        meses_iguais = 0
        for x in range(len(matriz)):
            if (matriz[x][0])[3:5] == meses_filtrados[i]:
                soma_mes += int(matriz[x][1])
                meses_iguais += 1
        media_mes = soma_mes/meses_iguais
        medias.append(media_mes)
    maior = 0
    for i in range(len(medias)):
        if medias[i] > maior:
            maior = medias[i]
    maior_mes = meses_filtrados[i]
    if maior_mes == "01":
        mes_extenco = "Janeiro"
    elif maior_mes == "02":
        mes_extenco = "Fevereiro"
    elif maior_mes == "03":
        mes_extenco = "Março"
    elif maior_mes == "04":
        mes_extenco = "Abril"
    elif maior_mes == "05":
        mes_extenco = "Maio"
    elif maior_mes == "06":
        mes_extenco = "Junho"
    elif maior_mes == "07":
        mes_extenco = "Julho"
    elif maior_mes == "08":
        mes_extenco = "Agosto"
    elif maior_mes == "09":
        mes_extenco = "Setembro"
    elif maior_mes == "10":
        mes_extenco = "Outubro"
    elif maior_mes == "11":
        mes_extenco = "Novembro"
    elif maior_mes == "12":
        mes_extenco = "Dezembro"
    return mes_extenco

def maior_força_reativa(matriz):
    maior = 0
    for i in range(len(matriz)):
        if int(matriz[i][4]) > maior:
            maior = int(matriz[i][4])
            index = i
    return matriz[index][2],matriz[index][4]
    
def menor_forca_aparente(matriz):
    menor = int(matriz[0][3])
    for i in range(len(matriz)):
        if int(matriz[i][3]) < menor:
            menor = int(matriz[i][3])
            index = i
    return matriz[index][1],matriz[index][3]

questao_2 = maior_força_reativa(tabela)
questao_3 = menor_forca_aparente(tabela)

print(F"Questão 1 : A mes com maior media foi {mes_corrente(tabela)} ")
print(F"Questão 2 : A maior força reativa é {questao_2[1]} e sua força é de {questao_2[0]}")
print(F"Questão 3 : A menor força aparente é {questao_3[1]} e sua corrente é de {questao_3[0]}")