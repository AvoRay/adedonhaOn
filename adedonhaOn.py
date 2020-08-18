import mechanicalsoup

import mysql.connector

mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953'
    )
print(mydb)

''' CRIAR UM MODULO PARA ISSO DEPOIS
browser = mechanicalsoup.Browser()
pagina = browser.get('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil')


links = pagina.soup.find_all('li')

def Pesquisa(pesquisa):
    for x in links:
        if '(' in x.text:#filtrar melhor as cidades
            if pesquisa.lower() in x.text.lower():
                print(x.text)

'''
from random import choice 
from time import sleep
 
pt1 = 0
pt2 = 0
while True:
    alfa = str(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])).upper()
    assunto = (str(choice(['comidas','cidade','frutas','pessoas','objetos','filmes','animais']).upper()))

    print('\nAdedoooonhaaa !!! nome de {} com a letra {} \n'.format(assunto,alfa))
    #if assunto == 'CIDADE':
        #Pesquisa(input('Qual nome da Cidade ? '))
    
    sleep(8)
 
    player=['LehMae','Ceceda']
    vence = input('Quem Ganho ? \n1 = {}\n2 = {}\n'.format(player[0],player[1]))
    
    if vence =='1':
        pt1+=1
    elif vence =='2':
        pt2+=1
    
    print('\nPontuaçao\n{} = {} Pontod\n{} = {} Pontos'.format(player[0],pt1,player[1],pt2))
