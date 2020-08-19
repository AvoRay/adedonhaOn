#import mechanicalsoup

import mysql.connector
from time import sleep
mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953'
    )
cursor = mydb.cursor()
name = 'Rick'
pt = 90


cursor.execute('UPDATE versus SET jogador1 = "PLAY1",jogador2 = "PLAY2"')
mydb.commit()
cursor.execute('UPDATE resposta SET resp = "VAZIO",jogador = "VAZIO"')

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

    cursor.execute('UPDATE  charada SET frase = (%s)',[frase])
    mydb.commit()

    print('A pergunta foi lançada')
    sleep(10)

    '''
    mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953'
    )
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM resposta')
    respostas = cursor.fetchall()'''
    
    
    
    

    

    

