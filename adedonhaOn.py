import mechanicalsoup

import mysql.connector

mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953'
    )
cursor = mydb.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jogador (nome VARCHAR(255),pontos INTEGER(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS charada (frase VARCHAR(255))')

name = 'John'
pt = 55

cursor.execute('INSERT INTO jogador (nome,pontos) VALUES(%s,%s)',(name,pt))
mydb.commit()

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

    frase = '\nAdedoooonhaaa !!! nome de {} com a letra {} \n'.format(assunto,alfa)
    print(frase)
    
    
    cursor.execute('SELECT * FROM charada')
    if cursor.fetchall() == []:# se o banco estiver vazio
        cursor.execute('INSERT INTO charada (frase) VALUES (%s)',[frase])
        mydb.commit()
    else:# se ja tiver uma frase no banco
        cursor.execute('UPDATE  charada SET frase = (%s)',[frase])
        mydb.commit()
    
    
    #mydb.commit()
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
